from typing import List

from models.lab_8_plate import Plate
from models.lab_8_salad_plate import SaladPlate


class PlateManagerException(Exception):
    pass


class PlateManager:
    def __init__(self):
        self.plates: List[Plate] = []

    def __len__(self):
        return len(self.plates)

    def __getitem__(self, item):
        return self.plates[item]

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
        if any_satisfy == False and all_satisfy == False:
            raise PlateManagerException("All of your checks are false try another value")
        return {"all": all_satisfy, "any": any_satisfy}

    def add_plate(self, plate):
        self.plates.append(plate)

    def add_plates(self, plates):
        self.plates.extend(plates)

    def find_all_with_weight_greater_than(self, weight):
        return list(filter(lambda plate: plate.get_max_food_weight() > weight, self.plates))

    def find_by_form(self, shape):
        return list(filter(lambda plate: isinstance(plate, SaladPlate) and plate.shape == shape, self.plates))
