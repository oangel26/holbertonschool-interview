#!/usr/bin/python3
"""
Log parsing
"""


import sys
import json
import time


counter = 0
status_dict = {}
file_size = 0
try:
    for line in sys.stdin:
        counter += 1
        chunk = line.split()
        status_code = json.loads(chunk[7])
        file_size += int(chunk[8])
        if (isinstance(status_code, int) and status_code in status_dict):
            status_dict[status_code] += 1
        else:
            status_dict[status_code] = 1
        if counter % 10 == 0:
            print(f"File size: {file_size}")
            for k, v in sorted(status_dict.items()):
                print(f"{k}: {v}")
except KeyboardInterrupt:
    print(f"File size: {file_size}")
    for k, v in sorted(status_dict.items()):
        print(f"{k}: {v}")
    sys.exit(0)
