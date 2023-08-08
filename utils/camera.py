from .point import Point
from .vector import Vector, random_in_unit_disk
from .ray import Ray
from .hittable import Hittable, HitRecord
from .color import Color
from .interval import Interval, INFINITY
from .image import WImage
from .utilities import random_double, degrees_to_radians
from math import tan


class Camera:
    aspect_ratio: float = 1.0
    image_width: int = 100
    image_height: int
    center: Point
    pixel00_loc: Point
    pixel_delta_u: Vector
    pixel_delta_v: Vector
    u: Vector
    v: Vector
    w: Vector
    defocus_disk_u: Vector
    defocus_disk_v: Vector
    samples_per_pixel: int = 10
    max_depth: int = 10
    vfov: float = 90
    lookfrom: Point = Point(0, 0, -1)
    lookat: Point = Point(0, 0, 0)
    vup: Vector = Vector(0, 1, 0)
    defocus_angle: float = 0
    focus_dist: float = 10

    def initialize(self) -> None:
        self.image_height: int = int(self.image_width / self.aspect_ratio)
        self.image_height = 1 if self.image_height < 1 else self.image_height
        self.center = self.lookfrom

        # Determine viewport dimensions.
        # focal_length: float = (self.lookfrom - self.lookat).length
        theta: float = degrees_to_radians(self.vfov)
        h = tan(theta / 2)
        viewport_height = 2 * h * self.focus_dist
        viewport_width: float = viewport_height * (self.image_width / self.image_height)

        # Calculate the u,v,w unit basis vectors for the camera coordinate frame.
        self.w = (self.lookfrom - self.lookat).unit
        self.u = self.vup.cross(self.w).unit
        self.v = self.w.cross(self.u)

        # Calculate the vectors across the horizontal and down the vertical viewport edges.
        viewport_u: Vector = viewport_width * self.u
        viewport_v: Vector = viewport_height * -self.v

        # Calculate the horizontal and vertical delta vectors from pixel to pixel.
        self.pixel_delta_u = viewport_u / self.image_width
        self.pixel_delta_v = viewport_v / self.image_height

        # Calculate the location of the upper left pixel.
        viewport_upper_left: Point = (
            self.center - (self.focus_dist * self.w) - viewport_u / 2 - viewport_v / 2
        )
        self.pixel00_loc = viewport_upper_left + 0.5 * (
            self.pixel_delta_u + self.pixel_delta_v
        )

        # Calculate the camera defocus disk basis vectors.
        defocus_radius = self.focus_dist * tan(
            degrees_to_radians(self.defocus_angle / 2)
        )
        self.defocus_disk_u = self.u * defocus_radius
        self.defocus_disk_v = self.v * defocus_radius

    def render(self, world: Hittable) -> None:
        self.initialize()
        image = WImage(self.image_width, self.image_height, "image_test.ppm")
        j: int = 0
        while j < self.image_height:
            print(f"Scanlines Remaning: {self.image_height - j}")
            i: int = 0
            while i < self.image_width:
                pixel_color = Color(0, 0, 0)
                for _ in range(self.samples_per_pixel):
                    r: Ray = self.get_ray(i, j)
                    pixel_color += self.ray_color(r, self.max_depth, world)
                image.add_data_array(pixel_color, self.samples_per_pixel)
                i += 1
            j += 1
        image.write_image()

    def ray_color(self, r: Ray, depth: int, world: Hittable) -> Color:
        rec: HitRecord = HitRecord()
        if depth <= 0:
            return Color(0, 0, 0)
        if world.hit(r, Interval(0.001, INFINITY), rec):
            scattered: Ray = Ray()
            attenuation: Color = Color()
            if rec.mat_ptr.scatter(r, rec, attenuation, scattered):
                return attenuation * self.ray_color(scattered, depth - 1, world)
            return Color(0, 0, 0)
        unit_direction: Vector = r.direction.unit
        a: float = 0.5 * (unit_direction.y + 1.0)
        return (1.0 - a) * Color(1.0, 1.0, 1.0) + a * Color(0.5, 0.7, 1.0)

    def get_ray(self, i: int, j: int) -> Ray:
        pixel_center: Point = (
            self.pixel00_loc + (i * self.pixel_delta_u) + (j * self.pixel_delta_v)
        )
        pixel_sample = pixel_center + self.pixel_sample_square()
        ray_origin = (
            self.center if (self.defocus_angle <= 0) else self.defocus_disk_sample()
        )
        ray_direction = pixel_sample - ray_origin

        return Ray(ray_origin, ray_direction)

    def pixel_sample_square(self) -> Vector:
        px = -0.5 + random_double()
        py = -0.5 + random_double()
        return (px * self.pixel_delta_u) + (py * self.pixel_delta_v)

    def defocus_disk_sample(self) -> Point:
        p: Vector = random_in_unit_disk()
        return self.center + (p.x * self.defocus_disk_u) + (p.y * self.defocus_disk_v)
