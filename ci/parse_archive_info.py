#!/usr/bin/env python3

import json
import os
import sys

DATA_FILE = "./gpl-dump-archive.json"

try:
    file_path = sys.argv[1]
except IndexError:
    file_path = None

try:
    with open(DATA_FILE) as f:
        data = json.load(f)
except FileNotFoundError as e:
    raise FileNotFoundError(f"data file {DATA_FILE} not found") from e

archive_name = data["name"]
archive_download_baseurl = f"https://archive.org/download/{archive_name}"
archive_torrent_url = f"{archive_download_baseurl}/{archive_name}_archive.torrent"
archive_file_data_url = f"{archive_download_baseurl}/{archive_name}_files.xml"

with open(os.environ.get("GITHUB_OUTPUT", False), "a") as f:
    f.write(f"archive-name={archive_name}\n")
    f.write(f"archive-download-baseurl={archive_download_baseurl}\n")
    f.write(f"archive-torrent-url={archive_torrent_url}\n")
    f.write(f"archive-file-data-url={archive_file_data_url}\n")

    if file_path:
        f.write(f"firmware-http-url={archive_download_baseurl}/{file_path}\n")
