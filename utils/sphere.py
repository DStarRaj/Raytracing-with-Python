from .point import Point
from .vector import Vector
from .ray import Ray
from .hittable import HitRecord, Hittable


class Sphere(Hittable):
    def __init__(self, center: Point, radius: float) -> None:
        super().__init__()
        self._center = center
        self._radius = radius

    @property
    def center(self) -> Point:
        return self._center

    @center.setter
    def center(self, p: Point) -> None:
        self._center = p

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, r: float) -> None:
        self._radius = r

    def hit(self, r: Ray, t_min: float, t_max: float, rec: HitRecord) -> bool:
        oc: Vector = r.origin - self.center
        a: float = r.direction.length_sq
        half_b: float = oc.dot(r.direction)
        c: float = oc.length_sq - self.radius**2
        discriminant: float = half_b**2 - a * c
        if discriminant < 0:
            return False
        sqrtd: float = discriminant**0.5
        root: float = (-half_b - sqrtd) / a
        if root < t_min or t_max < root:
            root: float = (-half_b + sqrtd) / a
            if root < t_min or t_max < root:
                return False

        rec.t = root
        rec.p = r.at(rec.t)
        outward_normal: Vector = (rec.p - self.center) / self.radius
        rec.set_face_normal(r, outward_normal)

        return True
