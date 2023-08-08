from typing import Type
from typing_extensions import Self
from .utilities import random_double
from math import sqrt


class Vector:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, val: float) -> None:
        self._x = val

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, val: float) -> None:
        self._y = val

    @property
    def z(self) -> float:
        return self._z

    @z.setter
    def z(self, val: float) -> None:
        self._z = val

    @property
    def length_sq(self) -> float:
        return self.x**2 + self.y**2 + self.z**2

    @property
    def length(self) -> float:
        return self.length_sq**0.5

    @property
    def unit(self) -> Self:
        return unit_vector(self)

    def dot(self, vec: Self) -> float:
        return dot_product(self, vec)

    def cross(self, vec: Self) -> Self:
        return cross_product(self, vec)

    def near_zero(self) -> bool:
        s: float = 1e-8
        return abs(self.x) < s and abs(self.y) < s and abs(self.z) < s

    @staticmethod
    def random(min: float = None, max: float = None) -> Self:
        return Vector(
            random_double(min, max),
            random_double(min, max),
            random_double(min, max),
        )

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

    def __mul__(self, vec: Self | float) -> Self:
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

    def __rmul__(self, vec: float) -> Self:
        if isinstance(vec, (int, float)):
            res_v = Vector()
            res_v.x = self.x * vec
            res_v.y = self.y * vec
            res_v.z = self.z * vec
            return res_v
        else:
            raise TypeError(f"Type of '{type(vec).__qualname__}' isn't supported")

    def __truediv__(self, val: float) -> Self:
        if isinstance(val, (int, float)):
            res_v = Vector()
            res_v = self * (1 / val)
            return res_v
        else:
            raise TypeError(f"Type of '{type(val).__qualname__}' isn't supported")

    def __str__(self) -> str:
        return f"< {self.x}, {self.y}, {self.z} >"


def dot_product(vecA: Type[Vector], vecB: Type[Vector]) -> float:
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


def random_in_unit_sphere() -> Vector:
    while True:
        p: Vector = Vector.random(-1, 1)
        if p.length_sq >= 1:
            continue
        return p


def random_unit_vector() -> Vector:
    return random_in_unit_sphere().unit


def random_in_hemisphere(normal: Vector) -> Vector:
    in_unit_sphere: Vector = random_in_unit_sphere()
    if in_unit_sphere.dot(normal) > 0:
        return in_unit_sphere
    else:
        return -in_unit_sphere


def reflect(v: Vector, n: Vector) -> Vector:
    return v - 2 * v.dot(n) * n


def refract(uv: Vector, n: Vector, etai_over_etat: float) -> Vector:
    cos_theta: float = min(dot_product(-uv, n), 1.0)
    r_out_perp: Vector = etai_over_etat * (uv + cos_theta * n)
    r_out_parallel: Vector = -sqrt(abs(1.0 - r_out_perp.length_sq)) * n
    return r_out_perp + r_out_parallel


if __name__ == "__main__":
    a = Vector(-2, 4, -4)
    b = Vector(1, 1, 1)
    a = a.unit.cross(5)
    print(a)
