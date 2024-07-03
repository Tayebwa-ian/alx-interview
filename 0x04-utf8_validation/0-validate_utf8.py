#!/usr/bin/python3
"""
UFT-8 Complaince check
"""


def validUTF8(data):
    """Checks if it is UTF-8 valid data
    Arg:
        data: a list of integers representing the data
    """
    data_length = len(data)
    if data_length > 1:
        if data[0] < 128 and data_length == 1:
            return True
        elif data[0] > 127 and data_length < 2:
            return False
        elif data[0] > 247:
            return False
        elif data[0] > 127 and data[0] < 248:
            for i in data[1:4]:
                if i > 191 or i < 128:
                    return False
        if data[4:]:
            return validUTF8(data[4:])
        else:
            for i in data:
                if i > 127:
                    return False
            return True
    return True
