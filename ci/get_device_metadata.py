#!/usr/bin/env python3

import json
import os
import sys

import jsonschema


def validate_against_schema(data, device):
    with open("./.schemas/device_metadata.schema.json") as f:
        schema = json.load(f)
    try:
        jsonschema.validate(instance=data, schema=schema)
    except jsonschema.exceptions.ValidationError as e:
        raise Exception(
            f"Invalid device_metadata.json for {device}: {e.message}"
        ) from e


device = sys.argv[1]
device_dir_path = os.path.abspath(os.path.join("./devices", device))

with open(os.path.join(device_dir_path, "device_metadata.json")) as f:
    device_metadata = json.load(f)
    validate_against_schema(device_metadata, device)
    device_metadata.pop("$schema", None)

with open(os.environ.get("GITHUB_OUTPUT", False), "a") as f:
    f.write(f"json={json.dumps(device_metadata)}\n")
