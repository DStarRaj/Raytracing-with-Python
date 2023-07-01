from utils.color import Color
from utils.ray import Ray
from utils.vector import Vector
from utils.point import Point
from utils.image import WImage
from utils.hittable import HitRecord
from utils.hittableList import HittableList
from utils.sphere import Sphere
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


def ray_color(r: Ray, world: HittableList) -> Color:
    rec: HitRecord = HitRecord()
    if world.hit(r, 0, INFINITY, rec):
        return 0.5 * (rec.normal + Color(1, 1, 1))
    unit_direction: Vector = r.direction.unit
    t: float = 0.5 * (unit_direction.y + 1)
    return (1 - t) * Color(1, 1, 1) + t * Color(0.5, 0.7, 1)


def main() -> None:
    ## Image
    aspect_ratio: float = 16 / 9
    image_width: int = 1920
    image_height: int = int(image_width / aspect_ratio)

    ## World
    world: HittableList = HittableList()
    world.add(Sphere(Point(0, 0, -1), 0.5))
    world.add(Sphere(Point(0, -100.5, -1), 100))

    ## Camera
    viewport_height: float = 2.0
    viewport_width: float = aspect_ratio * viewport_height
    focal_length: float = 1.0

    origin: Point = Point(0, 0, 0)
    horizontal: Vector = Vector(viewport_width, 0, 0)
    vertical: Vector = Vector(0, viewport_height, 0)
    lower_left_corner: Vector = (
        origin - horizontal / 2 - vertical / 2 - Vector(0, 0, focal_length)
    )

    ## Render
    image = WImage(image_width, image_height, "image_test.ppm")
    j: int = image_height - 1
    while j >= 0:
        i: int = 0
        while i < image_width:
            u: float = i / (image_width - 1)
            v: float = j / (image_height - 1)
            r: Ray = Ray(
                origin, lower_left_corner + u * horizontal + v * vertical - origin
            )
            pixel_color: Color = ray_color(r, world)
            image.add_data_array(pixel_color)
            i += 1
        j -= 1

    image.write_image()


if __name__ == "__main__":
    main()
