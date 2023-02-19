#!/usr/bin/env python3

import json
import os

devices_dir = os.path.abspath("./devices")

matrix_combinations = []


devices = os.listdir(devices_dir)
for device in devices:
    device_dir_path = os.path.join(devices_dir, device)
    if not os.path.isdir(device_dir_path):
        continue

    firmwares = os.listdir(device_dir_path)
    if not firmwares:
        continue

    try:
        with open(os.path.join(device_dir_path, "device_metadata.json")) as f:
            device_metadata = json.load(f)
    except FileNotFoundError as e:
        raise Exception(f"Device {device} has no device_metadata.json") from e

    for firmware in firmwares:
        firmware_dir_path = os.path.join(device_dir_path, firmware)
        if not os.path.isdir(firmware_dir_path):
            continue

        matrix_combinations.append(
            {
                "device": device,
                "firmware": firmware,
            }
        )

matrix = {"include": matrix_combinations}
print(f"matrix={json.dumps(matrix)}")
