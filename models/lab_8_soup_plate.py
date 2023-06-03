from models.lab_8_plate import Plate


class SoupPlateException(Exception):
    pass


class SoupPlate(Plate):
    def __init__(self, diameter, material, color, depth, soup_type):
        super().__init__(diameter, material, color)
        self.depth = depth
        self.soup_type = soup_type
        self.pattern = {"spoon", "fork", "kitchen"}

    def get_max_food_weight(self):
        return (3.14 * (self.diameter / 2) ** 2 * self.depth) / 2

    def __str__(self):
        return f"SoupPlate: diameter={self.diameter}, material={self.material}, color={self.color}, depth={self.depth}, soup_type={self.soup_type}"

    def funny_exception(self):
        if not isinstance(self, SoupPlate):
            raise SoupPlateException("How is that even possible!?")
