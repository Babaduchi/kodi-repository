# Babaduchi Kodi Repository

This repository owns the Kodi installation repository, its installer, package index, checksums, and GitHub Pages deployment.

Add-on source remains independently maintained in:

- [Babaduchi/ersatztv-kodi](https://github.com/Babaduchi/ersatztv-kodi)
- [Babaduchi/multi-update-kodi](https://github.com/Babaduchi/multi-update-kodi)
- [Babaduchi/radio-generator-kodi](https://github.com/Babaduchi/radio-generator-kodi)
- [Babaduchi/kodi-chibi-club](https://github.com/Babaduchi/kodi-chibi-club)
- [Babaduchi/visualization.droneshow](https://github.com/Babaduchi/visualization.droneshow)

The publishing workflow checks out those repositories, validates their add-ons,
builds separate Windows x64 Chibi Club plus Windows x64 and Linux x86_64
Drone Show visualizations for Kodi 21 Omega and Kodi 22 Piers, and packages them without
duplicating their source here.

## Install

Download the current `repository.babaduchi` release ZIP, then use **Kodi → Add-ons → Install from ZIP file**.

Versions through 1.2.7 used the legacy ID `repository.babaduchi.ersatztv`. Because Kodi treats the add-on ID as its unique identity, install `repository.babaduchi-1.3.0.zip` manually once when migrating from that legacy repository add-on.
