#!/usr/bin/env python

import hashlib
import json
import pathlib
import sys

import jinja2
from pkg_resources import parse_version

release_tag = sys.argv[1]

firmwares = json.loads(sys.argv[2])
firmwares.sort(key=parse_version, reverse=True)

modules_output_directory = pathlib.Path(sys.argv[3]).resolve()

my_output_directory = pathlib.Path("text_files_out")
my_output_directory.mkdir(exist_ok=True)

setup_script_path = my_output_directory / "setup_macvlan.sh"
release_notes_path = my_output_directory / "release_notes.md"
checksums_path = my_output_directory / "checksums.txt"

template_directory = pathlib.Path(__file__).parent.resolve() / "templates"

checksums = {}

for firmware in firmwares:
    filename = f"{firmware}-macvlan.ko"

    sha256_hash = hashlib.sha256()
    with open(modules_output_directory / filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    checksums[f"{firmware}-macvlan.ko"] = sha256_hash.hexdigest()



templateLoader = jinja2.FileSystemLoader(searchpath=template_directory)
templateEnv = jinja2.Environment(loader=templateLoader, autoescape=True)
setup_script_template = templateEnv.get_template("setup_macvlan.sh.j2")
release_template = templateEnv.get_template("release_template.md.j2")
checksums_template = templateEnv.get_template("checksums.txt.j2")

setup_script_rendered = setup_script_template.render(
    release_tag=release_tag
)
setup_script_path.write_text(setup_script_rendered + "\n")

checksums["setup_macvlan.sh"] = hashlib.sha256(
    setup_script_path.read_bytes()).hexdigest()


checksums_rendered = checksums_template.render(
    checksums=checksums
)
checksums_path.write_text(checksums_rendered + "\n")

release_notes_rendered = release_template.render(
    release_tag=release_tag,
    firmwares=firmwares,
    checksums=checksums
)

release_notes_path.write_text(release_notes_rendered + "\n")

print(f"""Created:
  - {setup_script_path}
  - {release_notes_path}
  - {checksums_path}

Calculated SHA256 Checksums:""")

for file, checksum in checksums.items():
  print(f"  - file: {file}")
  print(f"    checksum: {checksum}")
