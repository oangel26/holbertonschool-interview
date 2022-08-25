#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """ Determines if a given data set represents a valid UTF-8 encoding
    """
    try:
        for i in data:
            if i > 255 or i < 0:
                return False
        return True
    except:
        return False


if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))

    data = [0, None, 65, 127]
    print(validUTF8(data))

    data = [229, 255, 127]
    print(validUTF8(data))
