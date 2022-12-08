#!/usr/bin/env python

import json
import sys

import jinja2
from pkg_resources import parse_version

release_tag = sys.argv[1]

firmwares = json.loads(sys.argv[2])
firmwares.sort(key=parse_version, reverse=True)

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader, autoescape=True)
template = templateEnv.get_template("release_template.md.j2")

output = template.render(release_tag=release_tag, firmwares=firmwares)

print(output)
