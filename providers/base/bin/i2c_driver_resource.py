#!/usr/bin/env python3

import os
import subprocess

result = subprocess.check_output(
    ["i2cdetect", "-l"], universal_newlines=True
)
busses = result.splitlines()
for bus in busses:
    fields = bus.split("\t") 
    print("id: %s" % fields[0])
    print("protocol: %s" % fields[1])
    print("name: %s" % fields[2])
    print("type: %s" % fields[3])
    print("")
