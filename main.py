from utils.color import Color, randomColor
from utils.point import Point
from utils.hittableList import HittableList
from utils.sphere import Sphere
from utils.camera import Camera
from utils.material import Lambertian, Metal, Dielectric, Material
from utils.utilities import *
from utils.vector import Vector


def main() -> None:
    ## World
    world: HittableList = HittableList()

    ground_material: Lambertian = Lambertian(Color(0.5, 0.5, 0.5))
    world.add(Sphere(Point(0, -1000, 0), 1000, ground_material))

    items = 5

    for a in range(-items, items):
        for b in range(-items, items):
            choose_mat: float = random_double()
            center: Point = Point(
                a + 0.9 * random_double(), 0.2, b + 0.9 * random_double()
            )

            if (center - Point(4, 0.2, 0)).length > 0.9:
                sphere_material: Material

                if choose_mat < 0.8:
                    # diffuse
                    albedo: Color = randomColor() * randomColor()
                    sphere_material = Lambertian(albedo)
                    world.add(Sphere(center, 0.2, sphere_material))
                elif choose_mat < 0.95:
                    # metal
                    albedo: Color = randomColor(0.5, 1)
                    fuzz: float = random_double(0, 0.5)
                    sphere_material = Metal(albedo, fuzz)
                    world.add(Sphere(center, 0.2, sphere_material))
                else:
                    # glass
                    sphere_material = Dielectric(1.5)
                    world.add(Sphere(center, 0.2, sphere_material))

    material1: Dielectric = Dielectric(1.5)
    world.add(Sphere(Point(0, 1, 0), 1, material1))

    material2: Lambertian = Lambertian(Color(0.4, 0.2, 0.1))
    world.add(Sphere(Point(-4, 1, 0), 1, material2))

    material3: Metal = Metal(Color(0.7, 0.6, 0.5), 0)
    world.add(Sphere(Point(4, 1, 0), 1, material3))

    cam: Camera = Camera()
    cam.aspect_ratio = 16.0 / 9.0
    cam.image_width = 400
    cam.samples_per_pixel = 10
    cam.max_depth = 5
    cam.vfov = 20
    cam.lookfrom = Point(13, 2, 3)
    cam.lookat = Point(0, 0, 0)
    cam.vup = Vector(0, 1, 0)
    cam.defocus_angle = 0.6
    cam.focus_dist = 10
    cam.render(world)


if __name__ == "__main__":
    main()
