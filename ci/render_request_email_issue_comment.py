#!/usr/bin/env python3
import sys

import jinja2

template_directory = "ci/templates"
templateLoader = jinja2.FileSystemLoader(searchpath=template_directory)
templateEnv = jinja2.Environment(loader=templateLoader, autoescape=True)

request_template = templateEnv.get_template("gpl_archive_request_email_comment.md.j2")

print(request_template.render(device_name=sys.argv[1], firmware_version=sys.argv[2]))
