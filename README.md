# macvlan.ko for Unifi UDR

Ui stopped including the macvlan kernel module for the UDR. This brings it back

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Installation](#installation)
- [Updates](#updates)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Installation

1. Get the file `setup_macvlan.sh` from the [latest release](https://github.com/whi-tw/macvlan-unifi-udr/releases/latest) and transfer it to the UDR
1. Run it on the UDR via ssh `bash ./setup_macvlan.sh`
1. Run the script `/data/on_boot.d/01-load-macvlan-module.sh`
1. Continue what you were doing before that relied on having `macvlan` available

## Updates

This relies on the GPL archives provided by Ui. Unfortunately, these need to be requested manually for every firmware release. This means that there's no good automatic way of keeping it updated.

There is a check in place - this will only attempt to load the module build for the current firmware, so if you update UnifiOS on the UDR, the module will stop loading. I'd recommend turning auto update off, so this doesn't happen.

If I haven't noticed a new firmware release, please raise an issue and I'll get onto UI to get the GPL dump out.

Theoretically, the module will work on any release with the same kernel version (eg. the current dump is for 2.2.12, but the module works on 3.0.13 as they use the same kernel.). If you test this and it works fine, let me know and I'll short-circuit the update process.
