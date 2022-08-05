#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """ method that determines if all the boxes can be opened."""
    if boxes is None or len(boxes) == 0:
        return False

    status = ["T"]

    for box in range(1, len(boxes)):
        status.append("F")

    for box in range(0, len(boxes)):
        if (status[box] == "T" or box == 0):
            for key in boxes[box]:
                if int(key) < len(boxes) and status[key] == "F":
                    for k in boxes[key]:
                        if k < len(boxes):
                            status[k] = "T"
                if key < len(boxes):
                    status[key] = "T"

    if "F" in status:
        return False
    return True


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
