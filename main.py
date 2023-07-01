from utils.color import Color
from utils.ray import Ray
from utils.vector import Vector, random_in_hemisphere
from utils.point import Point
from utils.image import WImage
from utils.hittable import HitRecord
from utils.hittableList import HittableList
from utils.sphere import Sphere
from utils.camera import Camera
from utils.material import Lambertian, Metal
from typing import Type
from utils.utilities import *


def hit_sphere(center: Point, radius: float, r: Ray) -> float:
    oc: Vector = r.origin - center
    a: float = r.direction.length_sq
    half_b: float = oc.dot(r.direction)
    c: float = oc.length_sq - radius**2
    discriminant: float = half_b**2 - a * c
    if discriminant < 0:
        return -1
    else:
        return (-half_b - discriminant**0.5) / a


def ray_color(r: Ray, world: HittableList, depth: int) -> Color:
    rec: HitRecord = HitRecord()

    if depth <= 0:
        return Color(0, 0, 0)

    if world.hit(r, 0.001, INFINITY, rec):
        scattered: Ray = Ray()
        attenuation: Color = Color()
        if rec.mat_ptr.scatter(r, rec, attenuation, scattered):
            return attenuation * ray_color(scattered, world, depth - 1)
        return Color(0, 0, 0)

    unit_direction: Vector = r.direction.unit
    t: float = 0.5 * (unit_direction.y + 1)
    return (1 - t) * Color(1, 1, 1) + t * Color(0.5, 0.7, 1)


def main() -> None:
    ## Image
    aspect_ratio: float = 16 / 9
    image_width: int = 400
    image_height: int = int(image_width / aspect_ratio)
    samples_per_pixel: int = 20
    max_depth: int = 50

    ## World
    world: HittableList = HittableList()

    material_ground: Lambertian = Lambertian(Color(0.8, 0.8, 0))
    material_center: Lambertian = Lambertian(Color(0.7, 0.3, 0.3))
    # material_center = Metal(Color(1, 0, 0))
    material_left: Metal = Metal(Color(0.8, 0.8, 0.8), 0.3)
    material_right: Metal = Metal(Color(0.8, 0.6, 0.2), 1)

    world.add(Sphere(Point(0, -100.5, -1), 100, material_ground))
    world.add(Sphere(Point(0, 0, -1), 0.5, material_center))
    world.add(Sphere(Point(-1, 0, -1), 0.5, material_left))
    world.add(Sphere(Point(1, 0, -1), 0.5, material_right))

    ## Camera
    cam: Camera = Camera()

    ## Render
    image = WImage(image_width, image_height, "image_test.ppm")
    j: int = image_height - 1
    while j >= 0:
        print(f"Scanlines Remaning: {j}")
        i: int = 0
        while i < image_width:
            pixel_color: Color = Color(0, 0, 0)
            for _ in range(samples_per_pixel):
                u: float = (i + random_double()) / (image_width - 1)
                v: float = (j + random_double()) / (image_height - 1)
                r: Ray = cam.get_ray(u, v)
                pixel_color += ray_color(r, world, max_depth)
            image.add_data_array(pixel_color, samples_per_pixel)
            i += 1
        j -= 1

    image.write_image()


if __name__ == "__main__":
    main()
