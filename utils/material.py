from .ray import Ray, copyRay
from . import hittable
from .color import Color, copyColor
from .vector import Vector, random_unit_vector, reflect, random_in_unit_sphere


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
