#!/usr/bin/python3
"""
Log parsing
"""


import sys


counter = 0
status_dict = {}
file_size = 0
try:
    for line in sys.stdin:
        counter += 1
        chunk = line.split()
        file_size += int(chunk[8])
        if chunk[7] in status_dict:
            status_dict[chunk[7]] += 1
        else:
            status_dict[chunk[7]] = 1
        if counter % 10 == 0:
            print(f"File size: {file_size}")
            for k, v in sorted(status_dict.items()):
                print(f"{k}: {v}")
except KeyboardInterrupt:
    print(f"File size: {file_size}")
    for k, v in sorted(status_dict.items()):
        print(f"{k}: {v}")
        sys.exit(0)
