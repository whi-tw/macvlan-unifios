#!/usr/bin/env python3

import base64
import json
import os
import sys

import jsonschema


def validate_against_schema(data, device, firmware_version):
    with open("./.schemas/firmware_metadata.schema.json") as f:
        schema = json.load(f)
    try:
        jsonschema.validate(instance=data, schema=schema)
    except jsonschema.exceptions.ValidationError as e:
        raise Exception(
            f"Invalid firmware_metadata.json for {device}/{firmware_version}: "
            f"{e.message}"
        ) from e


try:
    device = sys.argv[1]
    firmware_version = sys.argv[2]
except IndexError as e:
    raise Exception("No device / firmware version specified.") from e

device_dir_path = os.path.abspath(os.path.join("./devices", device))
firmware_dir_path = os.path.abspath(os.path.join(device_dir_path, firmware_version))

with open(os.path.join(firmware_dir_path, "firmware_metadata.json")) as f:
    firmware_metadata = json.load(f)
    validate_against_schema(firmware_metadata, device, firmware_version)
    firmware_metadata["kernel-archive-path-base64"] = base64.b64encode(
        firmware_metadata["kernel-archive-path"].encode("utf-8")
    ).decode("utf-8")
    firmware_metadata.pop("$schema", None)

with open(os.environ.get("GITHUB_OUTPUT", False), "a") as f:
    f.write(f"json={json.dumps(firmware_metadata)}\n")
    f.write(f"firmware-directory={firmware_dir_path}\n")
