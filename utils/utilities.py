import sys
import random


INFINITY: float = sys.float_info.max
PI: float = 3.1415926535897932385


def degrees_to_radians(degrees: float):
    return degrees * PI / 180


def random_double(min: float = None, max: float = None) -> float:
    if min != None and max != None:
        return random.uniform(min, max)
    else:
        return random.random()


def clamp(x: float, min: float, max: float) -> float:
    if x < min:
        return min
    if x > max:
        return max
    return x
