#!/usr/bin/env python3

import os
import sys
import json

devices_dir = os.path.abspath('./devices')

crosscompiler_packages = []

devices = os.listdir(devices_dir)

for device in devices:
    device_dir_path = os.path.join(devices_dir, device)
    if not os.path.isdir(device_dir_path):
        continue

    try:
        with open(os.path.join(device_dir_path, 'device_metadata.json')) as f:
            device_metadata = json.load(f)
    except FileNotFoundError:
        continue


    try:
        crosscompiler_packages.append(device_metadata["cross-compiler-package"])
    except KeyError:
        raise Exception(f"Device {device} has no cross-compiler-package specified in device_metadata.json")


print(f'ALL_CROSSCOMPILERS={",".join(crosscompiler_packages)}')
