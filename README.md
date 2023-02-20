# macvlan.ko for UniFi OS Devices (UDR, UDM*)

Ubiquiti stopped including the macvlan kernel module into recent UniFi OS releases. This brings it back.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Install](#install)
- [Update](#update)
- [Uninstall](#uninstall)
- [Update frequency](#update-frequency)
- [Support](#support)
- [UniFi OS Models](#unifi-os-models)
- [Compatibility disclaimer](#compatibility-disclaimer)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Install

1. Get the file `setup_macvlan.sh` from the [latest release](https://github.com/whi-tw/macvlan-unifios/releases/latest) and transfer it to your device.
1. Run it on the device via ssh `bash ./setup_macvlan.sh`
1. Run the script `/data/on_boot.d/01-load-macvlan-module.sh`
1. Continue what you were doing before that relied on having `macvlan` available

## Update

There should be no reason to update the module while you are on a single firmware, as the built module can't really be improved in any way.

The fun starts when you change to a new firmware.

I haven't yet tried this process, but the general steps would be identical to those in [Install](#install).

1. Check the [latest release](https://github.com/whi-tw/macvlan-unifios/releases/latest) includes the Kernel Module for your device's model and firmware version.
   - If it does, you're golden and can carry on
   - If it does not, you should probably avoid updating at this point. If there is not currently an [Issue](https://github.com/whi-tw/macvlan-unifios/issues) open, please open one using the 'New Firmware Request' template.
1. Update your device's firmware to the new release
1. After rebooting, run back through the steps in [Install](#install) and reboot your device.

## Uninstall

1. `rm /data/on_boot.d/01-load-macvlan-module.sh`
1. **Optional** Remove files from `/data/macvlan-module`
1. Reboot

## Update frequency

This project relies on the GPL archives provided by Ui. Unfortunately, these need to be requested manually for every firmware release. This means that there's no good automatic way of keeping it updated.

The script which loads the module will only load the module for your current running firmware. This is important, as a mismatch could cause your device to enter a permanent reboot loop, with the kernel crashing when the `macvlan` module is used. If you decide to rename module files to force it to load the wrong version, you could end up in a world of pain, so if you don't know what you are doing, please avoid messing with things.to update off, so this doesn't happen.

If I haven't noticed a new firmware release, please raise an issue with the **New Firmware Request** template and I'll get onto UI to get the GPL dump out.

Theoretically, the module will work on any firmware release with the same kernel version (eg. the dump for UDR firmware 2.2.12, builds a working module for versions up to 3.0.13 as they use the same kernel). If you test a new version and it works fine, let me know and I'll short-circuit the update process.

## Support

I don't _really_ have time to provide any support for this project. If I spot an issue that I can help with, I may be able to respond and assist. However, it is likely that this module itself won't require any support.

## UniFi OS Models

This was initially created for the UDR, but it [seems](https://github.com/whi-tw/macvlan-unifios/issues/12) that Ubiquiti have stopped including the module on all recent Unifi OS devices. If your device isn't listed in the [latest release](https://github.com/whi-tw/macvlan-unifios/releases/latest), raise an issue, using the 'New Firmware Request' template.

## GPL Archive Archive

> Yes, the heading is correct, this is an archive or archives!

I am archiving the GPL archives requested from UniFi on archive.org: [UniFi OS GPL Archives](https://archive.org/details/unifi-udr-gpl-archives). 

## Compatibility disclaimer

As stated in the GPL-3 License, no liability or warranty is provided for these kernel module builds. I have tested them on my own USR and am using them in production, but the same may not be the case for you.

So long as you are using the correct module build for your device's model and firmware, you _should_ not have any issues, but as we are building non-standard modules, there's no 100% guarantee.
