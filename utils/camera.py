from .point import Point
from .vector import Vector
from .ray import Ray


class Camera:
    aspect_ratio: float = 16 / 9
    viewport_height: float = 2.0
    viewport_width: float = aspect_ratio * viewport_height
    focal_length: float = 1.0

    __origin: Point = Point(0, 0, 0)
    __horizontal: Vector = Vector(viewport_width, 0, 0)
    __vertical: Vector = Vector(0, viewport_height, 0)
    __lower_left_corner: Vector = (
        __origin - __horizontal / 2 - __vertical / 2 - Vector(0, 0, focal_length)
    )

    def get_ray(self, u: float, v: float):
        return Ray(
            self.__origin,
            self.__lower_left_corner
            + u * self.__horizontal
            + v * self.__vertical
            - self.__origin,
        )
