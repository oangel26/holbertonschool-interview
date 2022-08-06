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

    keys_dict = {0: True}

    for i in range(1, len(boxes)):
        keys_dict[i] = False

    while (True):
        dict1 = keys_dict.copy()
        for k, v in keys_dict.items():
            if (v == True):
                for key in boxes[k]:
                    keys_dict[key] = True

        dict2 = keys_dict.copy()

        if (dict1 == dict2):
            break

    if (False in keys_dict.values()):
        return False
    return True


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
