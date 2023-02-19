#!/usr/bin/env python3

import json
import os
import sys


def check_attr_in_device_metadata(device, device_metadata, attr):
    if attr not in device_metadata or not device_metadata[attr]:
        raise Exception(
            f"Device {device} has no {attr} specified in device_metadata.json"
        )


device = sys.argv[1]
device_dir_path = os.path.abspath(os.path.join("./devices", device))

with open(os.path.join(device_dir_path, "device_metadata.json")) as f:
    device_metadata = json.load(f)
    check_attr_in_device_metadata(device, device_metadata, "architecture")
    check_attr_in_device_metadata(device, device_metadata, "cross-compiler")
    check_attr_in_device_metadata(device, device_metadata, "cross-compiler-package")

print(f"json={json.dumps(device_metadata)}")
