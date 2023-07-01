from typing import Type
from typing_extensions import Self


class Vector:
    def __init__(
        self, x: int | float = 0, y: int | float = 0, z: int | float = 0
    ) -> None:
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self) -> int | float:
        return self._x

    @x.setter
    def x(self, val: int | float) -> None:
        self._x = val

    @property
    def y(self) -> int | float:
        return self._y

    @y.setter
    def y(self, val: int | float) -> None:
        self._y = val

    @property
    def z(self) -> int | float:
        return self._z

    @z.setter
    def z(self, val: int | float) -> None:
        self._z = val

    @property
    def length_sq(self) -> int | float:
        return self.x**2 + self.y**2 + self.z**2

    @property
    def length(self) -> int | float:
        return self.length_sq**0.5

    @property
    def unit(self) -> Self:
        return unit_vector(self)

    def dot(self, vec: Self) -> int | float:
        return dot_product(self, vec)

    def cross(self, vec: Self) -> Self:
        return cross_product(self, vec)

    def __add__(self, vec: Self) -> Self:
        if isinstance(vec, Vector):
            res_v = Vector()
            res_v.x = self.x + vec.x
            res_v.y = self.y + vec.y
            res_v.z = self.z + vec.z
            return res_v
        else:
            raise TypeError(f"Type of '{type(vec).__qualname__}' isn't supported")

    def __sub__(self, vec: Self) -> Self:
        if isinstance(vec, Vector):
            res_v = Vector()
            res_v = self + -vec
            return res_v
        else:
            raise TypeError(f"Type of '{type(vec).__qualname__}' isn't supported")

    def __neg__(self) -> Self:
        return self * -1

    def __pos__(self) -> Self:
        return self

    def __mul__(self, vec: Self | int | float) -> Self:
        if isinstance(vec, Vector):
            res_v = Vector()
            res_v.x = self.x * vec.x
            res_v.y = self.y * vec.y
            res_v.z = self.z * vec.z
            return res_v
        elif isinstance(vec, (int, float)):
            res_v = Vector()
            res_v.x = self.x * vec
            res_v.y = self.y * vec
            res_v.z = self.z * vec
            return res_v
        else:
            raise TypeError(f"Type of '{type(vec).__qualname__}' isn't supported")

    def __rmul__(self, vec: int | float) -> Self:
        if isinstance(vec, (int, float)):
            res_v = Vector()
            res_v.x = self.x * vec
            res_v.y = self.y * vec
            res_v.z = self.z * vec
            return res_v
        else:
            raise TypeError(f"Type of '{type(vec).__qualname__}' isn't supported")

    def __truediv__(self, val: int | float) -> Self:
        if isinstance(val, (int, float)):
            res_v = Vector()
            res_v = self * (1 / val)
            return res_v
        else:
            raise TypeError(f"Type of '{type(val).__qualname__}' isn't supported")

    def __str__(self) -> str:
        return f"< {self.x}, {self.y}, {self.z} >"


def dot_product(vecA: Type[Vector], vecB: Type[Vector]) -> int | float:
    if isinstance(vecA, Vector) and isinstance(vecB, Vector):
        return (vecA.x * vecB.x) + (vecA.y * vecB.y) + (vecA.z * vecB.z)
    else:
        raise TypeError(
            f"Type of '{type(vecA).__qualname__}' and '{type(vecB).__qualname__}' isn't supported"
        )


def cross_product(vecA: Type[Vector], vecB: Type[Vector]) -> Type[Vector]:
    if isinstance(vecA, Vector) and isinstance(vecB, Vector):
        res_v = Vector()
        res_v.x = (vecA.y * vecB.z) - (vecA.z * vecB.y)
        res_v.y = (vecA.z * vecB.x) - (vecA.x * vecB.z)
        res_v.z = (vecA.x * vecB.y) - (vecA.y * vecB.x)
        return res_v
    else:
        raise TypeError(
            f"Type of '{type(vecA).__qualname__}' and '{type(vecB).__qualname__}' isn't supported"
        )


def unit_vector(vec: Type[Vector]) -> Vector:
    if isinstance(vec, Vector):
        return vec / vec.length
    else:
        raise TypeError(f"Type of '{type(vec).__qualname__}' isn't supported")


if __name__ == "__main__":
    a = Vector(-2, 4, -4)
    b = Vector(1, 1, 1)
    a = a.unit.cross(5)
    print(a)
