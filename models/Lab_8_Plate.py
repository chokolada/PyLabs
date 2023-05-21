from abc import ABC, abstractmethod


class Plate(ABC):
    def __init__(self, diameter, material, color):
        self.diameter = diameter
        self.material = material
        self.color = color

    @abstractmethod
    def get_max_food_weight(self):
        pass

    def __str__(self):
        return f"Plate: diameter={self.diameter}, material={self.material}, color={self.color}"