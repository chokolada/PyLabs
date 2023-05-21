from models.Lab_8_Plate import Plate


class SaladPlate(Plate):
    def __init__(self, diameter, material, color, shape, dishwasher_safe):
        super().__init__(diameter, material, color)
        self.shape = shape
        self.dishwasher_safe = dishwasher_safe

    def get_max_food_weight(self):
        volume = (3.14 * (self.diameter / 2) ** 2 * self.diameter) / 3
        return volume

    def __str__(self):
        return f"SaladPlate: diameter={self.diameter}, material={self.material}, color={self.color}, shape={self.shape}, dishwasher_safe={self.dishwasher_safe}"
