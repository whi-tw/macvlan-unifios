#!/usr/bin/env python
import json
import sys

body_lines = sys.stdin.readlines()

body_sections = []

current_section = {}

for line in body_lines:
    line = line.strip()
    if not line:
        continue
    if line.startswith("###"):
        if current_section:
            body_sections.append(current_section)
        current_section = {"title": line.removeprefix("###").strip(), "lines": []}
    else:
        current_section["lines"].append(line)

issue_components = {
    "device": None,
    "firmware_version": None,
}

for section in body_sections:
    section_title = section["title"]
    match section_title:
        case "Device":
            issue_components["device"] = section["lines"][0].split(" ")[0]
        case "Firmware Version":
            issue_components["firmware_version"] = section["lines"][0]
        case _:
            component_name = section_title.lower().replace(" ", "_").replace("/", "")
            if section["lines"][0] == "_No response_":
                value = []
            else:
                value = section["lines"]
            issue_components[component_name] = json.dumps(value)

for key, value in issue_components.items():
    print("{}={}".format(key, value))
