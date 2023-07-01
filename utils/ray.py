from .point import Point
from .vector import Vector
from typing import Type
from typing_extensions import Self


class Ray:
    _origin: Type[Point]
    _direction: Type[Point]

    def __init__(
        self, origin: Type[Point] = None, direction: Type[Vector] = None
    ) -> None:
        if origin:
            self._origin = origin
        if direction:
            self._direction = direction

    @property
    def origin(self) -> Type[Point]:
        return self._origin

    @property
    def direction(self) -> Type[Vector]:
        return self._direction

    def at(self, val: float) -> Type[Point]:
        return self.origin + val * self.direction


def copyRay(dest: Ray, source: Ray) -> None:
    dest._origin = source.origin
    dest._direction = source.direction
