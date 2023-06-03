from typing import List
from decorators.lab8_plate_decorator import measure_execution_time, print_iterable_length

from models.lab_8_plate import Plate
from models.lab_8_soup_plate import SoupPlate
from models.lab_8_salad_plate import SaladPlate
from models.lab_8_dessert_plate import DessertPlate
from models.lab_8_meat_plate import MeatPlate


class PlateManager:
    def __init__(self):
        self.plates: List[Plate] = []

    def __len__(self):
        return len(self.plates)

    def __getitem__(self, item):
        return self.plates.append(item)

    def __iter__(self):
        return iter(self.plates)

    def list_of_weights(self):
        print("list_of_weights")
        weighted_list = [plate.get_max_food_weight() for plate in self.plates]
        return weighted_list

    def indexed_list(self):
        print("Indexed_list:")
        for index, plate in enumerate(self.plates):
            print(index + 1, plate)

    def numeric_list(self):
        print("Numeric_list:")
        for object, function in zip(self.plates, self.list_of_weights()):
            print(object, function)

    def check_condition_all_any(self, value):
        print("All and Any:")
        all_satisfy = all(plate.diameter > value for plate in self.plates)
        any_satisfy = any(plate.diameter > value for plate in self.plates)
        return {"all": all_satisfy, "any": any_satisfy}

    def add_plate(self, plate):
        self.plates.append(plate)

    def add_plates(self, plates):
        self.plates.extend(plates)

    def find_all_with_weight_greater_than(self, weight):
        return list(filter(lambda plate: plate.get_max_food_weight() > weight, self.plates))

    def find_by_form(self, shape):
        return list(filter(lambda plate: isinstance(plate, SaladPlate) and plate.shape == shape, self.plates))