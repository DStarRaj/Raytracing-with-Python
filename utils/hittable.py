from .point import Point
from .vector import Vector
from .ray import Ray
from . import material


class HitRecord:
    p: Point
    normal: Vector
    mat_ptr: "material.Material"
    t: float
    front_face: bool

    def set_face_normal(self, r: Ray, outward_normal: Vector):
        self.front_face: bool = r.direction.dot(outward_normal) < 0
        self.normal: Vector = outward_normal if self.front_face else -outward_normal


class Hittable:
    def hit(self, r: Ray, t_min: float, t_max: float, rec: HitRecord) -> bool:
        return False


def copyHitRecord(dest: HitRecord, source: HitRecord) -> None:
    dest.p = source.p
    dest.normal = source.normal
    dest.mat_ptr = source.mat_ptr
    dest.t = source.t
    dest.front_face = source.front_face
