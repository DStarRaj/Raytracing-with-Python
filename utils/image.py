from typing import Type
from .color import Color
from PIL import Image
from .utilities import clamp


class WImage:
    data = []

    def __init__(self, width: int, height: int, image_path: str) -> None:
        self.height = height
        self.width = width
        self.image_path = image_path + ".png"

    def add_data_array(self, pixel_color: Type[Color], samples_per_pixel: int) -> None:
        r = pixel_color.x
        g = pixel_color.y
        b = pixel_color.z

        scale = 1 / samples_per_pixel

        r = (scale * r) ** 0.5
        g = (scale * g) ** 0.5
        b = (scale * b) ** 0.5

        self.data.append(
            (
                int(256 * clamp(r, 0, 0.999)),
                int(256 * clamp(g, 0, 0.999)),
                int(256 * clamp(b, 0, 0.999)),
            )
        )

    def write_image(self) -> None:
        image = Image.new(mode="RGB", size=(self.width, self.height), color="black")
        data_itr = iter(self.data)
        pixel_map = image.load()
        for i in range(self.height):
            for j in range(self.width):
                d = next(data_itr)
                pixel_map[j, i] = d
        image.save(self.image_path, format="png")
