from utils.color import Color
from utils.point import Point
from utils.hittableList import HittableList
from utils.sphere import Sphere
from utils.camera import Camera
from utils.material import Lambertian, Metal, Dielectric
from utils.utilities import *
from utils.vector import Vector
from math import cos


def main() -> None:
    ## World
    world: HittableList = HittableList()

    R: float = cos(PI / 4)

    # material_left: Lambertian = Lambertian(Color(0, 0, 1))
    # material_right: Lambertian = Lambertian(Color(1, 0, 0))

    material_ground: Lambertian = Lambertian(Color(0.8, 0.8, 0))
    material_center: Lambertian = Lambertian(Color(0.1, 0.2, 0.5))
    material_left: Dielectric = Dielectric(1.5)
    material_right: Metal = Metal(Color(0.8, 0.6, 0.2), 0)

    # world.add(Sphere(Point(-R, 0, -1), R, material_left))
    # world.add(Sphere(Point(R, 0, -1), R, material_right))

    world.add(Sphere(Point(0, -100.5, -1), 100, material_ground))
    world.add(Sphere(Point(0, 0, -1), 0.5, material_center))
    world.add(Sphere(Point(-1, 0, -1), 0.5, material_left))
    world.add(Sphere(Point(-1, 0, -1), -0.4, material_left))
    world.add(Sphere(Point(1, 0, -1), 0.5, material_right))

    ## Camera
    cam: Camera = Camera()
    cam.aspect_ratio = 16.0 / 9.0
    cam.image_width = 400
    cam.samples_per_pixel = 20
    cam.max_depth = 50
    cam.vfov = 20
    cam.lookfrom = Point(-2, 2, 1)
    cam.lookat = Point(0, 0, -1)
    cam.vup = Vector(0, 1, 0)
    cam.render(world)


if __name__ == "__main__":
    main()
