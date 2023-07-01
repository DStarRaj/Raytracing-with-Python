from .vector import Vector


class Point(Vector):
    def __init__(
        self, x: int | float = 0, y: int | float = 0, z: int | float = 0
    ) -> None:
        super().__init__(x, y, z)
