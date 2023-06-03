from abc import ABC, abstractmethod


class PlateException(Exception):
    pass


class Plate(ABC):
    def __init__(self, diameter, material, color):
        self.diameter = diameter
        self.material = material
        self.color = color
        self.pattern = None

    @abstractmethod
    def get_max_food_weight(self):
        pass

    def dictionary_list(self, value_type=None):
        print('dictionary_list')
        if value_type is not None:
            if not isinstance(value_type, type):
                raise PlateException("Invalid value_type provided. Expected a type.")

            person_dict = {key: value for key, value in self.__dict__.items() if isinstance(value, value_type)}
            print(person_dict)

    def __str__(self):
        return f"Plate: diameter={self.diameter}, material={self.material}, color={self.color}"
