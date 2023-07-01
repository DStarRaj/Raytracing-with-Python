from .hittable import HitRecord, Hittable, copyHitRecord
from .ray import Ray


class HittableList(Hittable):
    objects: list[Hittable] = []

    def __init__(self, object: Hittable = None) -> None:
        super().__init__()
        if object:
            self.objects.append(object)

    def clear(self) -> None:
        self.objects: list[Hittable] = []

    def add(self, object: Hittable) -> None:
        self.objects.append(object)

    def hit(self, r: Ray, t_min: float, t_max: float, rec: HitRecord) -> bool:
        temp_rec: HitRecord = HitRecord()
        hit_anything: bool = False
        closest_so_far: float = t_max
        for object in self.objects:
            if object.hit(r, t_min, closest_so_far, temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                copyHitRecord(rec, temp_rec)

        return hit_anything
