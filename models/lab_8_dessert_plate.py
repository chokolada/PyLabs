import math

from models.lab_8_plate import Plate


class DessertPlateException(Exception):
    pass


class DessertPlate(Plate):
    def __init__(self, diameter, material, color, topping, dessert_type):
        super().__init__(diameter, material, color)
        self.topping = topping
        self.dessert_type = dessert_type
        self.pattern = {"square", "ball", "birb"}

    def get_max_food_weight(self):
        volume = math.pi * self.diameter / 2 * 1.8
        return volume

    def __str__(self):
        return f"DessertPlate: diameter={self.diameter}, material={self.material}, color={self.color}," \
               f" topping={self.topping}, dessert_type={self.dessert_type}"

    def set_topping(self, new_topping):
        if not isinstance(new_topping, str):
            raise DessertPlateException("Invalid topping. Expected a string.")
        self.topping = new_topping
