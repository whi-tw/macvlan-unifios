#!/usr/bin/env python3

import base64
import json
import os
import sys


def check_attr_in_firmware_metadata(device, firmware_metadata, attr):
    if attr not in firmware_metadata or not firmware_metadata[attr]:
        raise Exception(
            f"Firmware {firmware_version} for device {device} "
            "has no {attr} specified in firmware_metadata.json"
        )


device = sys.argv[1]
firmware_version = sys.argv[2]

device_dir_path = os.path.abspath(os.path.join("./devices", device))
firmware_dir_path = os.path.abspath(os.path.join(device_dir_path, firmware_version))

with open(os.path.join(firmware_dir_path, "firmware_metadata.json")) as f:
    firmware_metadata = json.load(f)
    check_attr_in_firmware_metadata(device, firmware_metadata, "kernel-url")
    check_attr_in_firmware_metadata(device, firmware_metadata, "kernel-sha256sum")
    firmware_metadata["kernel-url-base64"] = base64.b64encode(
        firmware_metadata["kernel-url"].encode("utf-8")
    ).decode("utf-8")


print(f"json={json.dumps(firmware_metadata)}")
