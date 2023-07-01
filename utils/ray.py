from .point import Point
from .vector import Vector
from typing import Type
from typing_extensions import Self


class Ray:
    def __init__(self, origin: Type[Point], direction: Type[Vector]) -> None:
        self._origin = origin
        self._direction = direction

    @property
    def origin(self) -> Type[Point]:
        return self._origin

    @property
    def direction(self) -> Type[Vector]:
        return self._direction

    def at(self, val: int | float) -> Type[Point]:
        return self.origin + val * self.direction
