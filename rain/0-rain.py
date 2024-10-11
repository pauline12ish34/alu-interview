#!/usr/bin/python3
import pep8
"""trapped rain
"""


def rain(walls):
    """calculating rain """
    if not walls or len(walls) < 3:
        return 0

    rain = 0
    for i in range(1, len(walls) - 1):
        left = max(walls[:i])
        right = max(walls[i + 1:])
        min_wall = min(left, right)
        if walls[i] < min_wall:
            rain += min_wall - walls[i]
    return rain
