#!/usr/bin/env python3

import sys
import os
import json
import jinja2

report = json.load(sys.stdin)
try:
    rootdir = sys.argv[1]
except:
    print("Usage : {} path/to/directory".format(sys.argv[0]), file=sys.stderr)
    sys.exit(1)

os.makedirs(rootdir, exist_ok=True)

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)

if_tpl = templateEnv.get_template("interface.html")

for interface in report["interfaces"]:
    html_filename = interface["name"] + ".html"
    with open(rootdir+"/"+html_filename, "w") as html_file:
        html_file.write(if_tpl.render(interface=interface))
