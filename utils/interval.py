from .utilities import INFINITY


class Interval:
    def __init__(self, _min: float = None, _max: float = None) -> None:
        if _min == None:
            self.min = INFINITY
        self.min = _min
        if _max == None:
            self.max = -INFINITY
        self.max = _max

    def contains(self, x: float) -> bool:
        return self.min <= x and x <= self.max

    def surrounds(self, x: float) -> bool:
        return self.min < x and x < self.max
