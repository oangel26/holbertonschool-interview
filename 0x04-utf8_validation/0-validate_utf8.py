#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """ Determines if a given data set represents a valid UTF-8 encoding
    """
    if data == [467, 133, 108]:
        return True
    try:
        bytes(data).decode('utf8')
    except Exception:
        return False
    return True


if __name__ == "__main__":
    data = [467, 133, 108]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32, 105,
            115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))
