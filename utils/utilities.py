import sys

INFINITY: float = sys.float_info.max
PI: float = 3.1415926535897932385


def degrees_to_radians(degrees: float):
    return degrees * PI / 180
