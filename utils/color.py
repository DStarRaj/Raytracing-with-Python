from .vector import Vector


class Color(Vector):
    def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        super().__init__(x, y, z)


def copyColor(dest: Color, source: Color) -> None:
    dest.x = source.x
    dest.y = source.y
    dest.z = source.z
