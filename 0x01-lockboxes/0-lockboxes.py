#!/usr/bin/python3
"""
Lockboxes Modules
"""


def canUnlockAll(boxes) -> bool:
    """Check if all boxes can be unlocked
    Arg:
        boxes: a list of lists(boxes)
    return: true if all boxes can be unlocked otherwise false
    """
    for box_num in range(1, len(boxes)):
        unlocked = False
        for box in range(len(boxes)):
            for key in boxes[box]:
                if key == box_num and box != key:
                    unlocked = True
                    break
            if unlocked:
                break
        if not unlocked:  # one of the boxes can not be unlocked
            return False
    return True
