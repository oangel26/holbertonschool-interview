#!/usr/bin/python3
"""
Log parsing
"""


import sys
import json
import time


def print_stats(file_size: int, status_dict: dict) -> None:
    """ Function which prints stats """
    print(f"File size: {file_size}")
    for s_code, s_number in sorted(status_dict.items()):
        print(f"{s_code}: {str(s_number)}")


counter = 0
status_dict = {}
file_size = 0
try:
    for line in sys.stdin:
        counter += 1
        chunk = line.split()
        status_code = json.loads(chunk[7])
        file_size += int(chunk[8])

        # Creates status dictionary
        if (status_code in status_dict):
            status_dict[status_code] += 1
        else:
            status_dict[status_code] = 1

        if counter % 10 == 0:
            print_stats(file_size, status_dict)

except KeyboardInterrupt:
    print_stats(file_size, status_dict)
    raise