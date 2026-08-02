# Babaduchi Kodi Repository

This repository owns the Kodi installation repository, its installer, package index, checksums, and GitHub Pages deployment.

Add-on source remains independently maintained in:

- [Babaduchi/ersatztv-kodi](https://github.com/Babaduchi/ersatztv-kodi)
- [Babaduchi/multi-update-kodi](https://github.com/Babaduchi/multi-update-kodi)
- [Babaduchi/radio-generator-kodi](https://github.com/Babaduchi/radio-generator-kodi)

The publishing workflow checks out those repositories, validates their add-ons, and packages them without duplicating their source here.

## Install

Download the current `repository.babaduchi.ersatztv` release ZIP, then use **Kodi → Add-ons → Install from ZIP file**. The legacy add-on ID is intentionally retained so installations from the former ErsatzTV-hosted repository migrate automatically.
