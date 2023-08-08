from .ray import Ray, copyRay
from . import hittable
from .color import Color, copyColor
from .vector import Vector, random_unit_vector, reflect, random_in_unit_sphere, refract
from .utilities import random_double
from math import sqrt


class Material:
    def __init__(self) -> None:
        pass

    def scatter(
        self, r_in: Ray, rec: "hittable.HitRecord", attenuation: Color, scattered: Ray
    ) -> bool:
        return False


class Lambertian(Material):
    albedo: Color

    def __init__(self, a: Color) -> None:
        super().__init__()
        self.albedo = a

    def scatter(
        self, r_in: Ray, rec: "hittable.HitRecord", attenuation: Color, scattered: Ray
    ) -> bool:
        scatter_direction: Vector = rec.normal + random_unit_vector()

        if scatter_direction.near_zero():
            scatter_direction = rec.normal

        copyRay(scattered, Ray(rec.p, scatter_direction))
        copyColor(attenuation, self.albedo)
        return True


class Metal(Material):
    albedo: Color
    fuzz: float

    def __init__(self, a: Color, f: float) -> None:
        super().__init__()
        self.albedo = a
        self.fuzz = f if f < 1 else 1

    def scatter(
        self, r_in: Ray, rec: "hittable.HitRecord", attenuation: Color, scattered: Ray
    ) -> bool:
        reflected: Vector = reflect(r_in.direction.unit, rec.normal)
        copyRay(scattered, Ray(rec.p, reflected + self.fuzz * random_in_unit_sphere()))
        copyColor(attenuation, self.albedo)
        return scattered.direction.dot(rec.normal) > 0


class Dielectric(Material):
    ir: float

    def __init__(self, index_of_refraction: float) -> None:
        super().__init__()
        self.ir = index_of_refraction

    @staticmethod
    def reflectance(cosine: float, ref_idx: float) -> float:
        r0 = (1 - ref_idx) / (1 + ref_idx)
        r0 = r0**2
        return r0 + (1 - r0) * (1 - cosine) ** 5

    def scatter(
        self, r_in: Ray, rec: "hittable.HitRecord", attenuation: Color, scattered: Ray
    ) -> bool:
        copyColor(attenuation, Color(1, 1, 1))
        refraction_ratio: float = (1.0 / self.ir) if rec.front_face else self.ir
        unit_direction: Vector = r_in.direction.unit
        cos_theta: float = min(-unit_direction.dot(rec.normal), 1.0)
        sin_theta: float = sqrt(1 - cos_theta**2)
        cannot_refract: bool = refraction_ratio * sin_theta > 1
        if (
            cannot_refract
            or self.reflectance(cos_theta, refraction_ratio) > random_double()
        ):
            direction = reflect(unit_direction, rec.normal)
        else:
            direction = refract(unit_direction, rec.normal, refraction_ratio)
        copyRay(scattered, Ray(rec.p, direction))

        return True
