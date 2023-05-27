import math

from models.Lab_8_Plate import Plate


class DessertPlate(Plate):
    def __init__(self, diameter, material, color, topping, dessert_type):
        super().__init__(diameter, material, color)
        self.topping = topping
        self.dessert_type = dessert_type

    def get_max_food_weight(self):
        volume = math.pi * self.diameter/2 * 1.8
        return volume

    def __str__(self):
        return f"SoupPlate: diameter={self.diameter}, material={self.material}, color={self.color}," \
               f" topping={self.topping}, dessert_type={self.dessert_type}"
