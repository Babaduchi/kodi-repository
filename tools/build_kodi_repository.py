#!/usr/bin/env python3
import argparse
import hashlib
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = ROOT / "repository.babaduchi.ersatztv"


def version(addon_dir):
    return ET.parse(addon_dir / "addon.xml").getroot().attrib["version"]


def zip_addon(addon_dir, destination):
    with ZipFile(destination, "w", ZIP_DEFLATED) as package:
        for path in sorted(addon_dir.rglob("*")):
            if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc":
                package.write(path, (Path(addon_dir.name) / path.relative_to(addon_dir)).as_posix())


def digest(path, algorithm):
    hasher = hashlib.new(algorithm)
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


def build(output, addon_dirs):
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    addons = [REPOSITORY] + addon_dirs
    index_root = ET.Element("addons")
    for addon_dir in addons:
        addon_xml = addon_dir / "addon.xml"
        if not addon_xml.is_file():
            raise FileNotFoundError("Missing {}".format(addon_xml))
        index_root.append(ET.parse(addon_xml).getroot())

        target = output / addon_dir.name
        target.mkdir()
        archive = target / "{}-{}.zip".format(addon_dir.name, version(addon_dir))
        zip_addon(addon_dir, archive)
        (target / (archive.name + ".sha256")).write_text(
            digest(archive, "sha256") + "\n", encoding="ascii"
        )
        shutil.copy2(addon_xml, target / "addon.xml")

        metadata = ET.parse(addon_xml).getroot().find("extension[@point='xbmc.addon.metadata']")
        if metadata is not None:
            for asset in metadata.findall("./assets/*"):
                relative = Path((asset.text or "").strip())
                source = addon_dir / relative
                if relative.parts and source.is_file():
                    destination = target / relative
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(source, destination)

    tree = ET.ElementTree(index_root)
    ET.indent(tree, space="  ")
    index = output / "addons.xml"
    tree.write(index, encoding="UTF-8", xml_declaration=True)
    (output / "addons.xml.md5").write_text(digest(index, "md5") + "\n", encoding="ascii")
    (output / "index.html").write_text(
        "<!doctype html><title>Babaduchi Kodi Repository</title>"
        "<h1>Babaduchi Kodi Repository</h1>"
        "<p>Install the repository ZIP below once, then install Babaduchi add-ons in Kodi.</p>"
        '<p><a href="repository.babaduchi.ersatztv/repository.babaduchi.ersatztv-{}.zip">Download repository installer</a></p>'.format(version(REPOSITORY)),
        encoding="utf-8",
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("addons", nargs="+", type=Path)
    args = parser.parse_args()
    build(args.output.resolve(), [path.resolve() for path in args.addons])


if __name__ == "__main__":
    main()
