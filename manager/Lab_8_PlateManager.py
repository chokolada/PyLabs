from typing import List

from models.Lab_8_Plate import Plate
from models.Lab_8_SoupPlate import SoupPlate
from models.Lab_8_SaladPlate import SaladPlate
from models.Lab_8_DessertPlate import DessertPlate
from models.Lab_8_MeatPlate import MeatPlate


class PlateManager:
    def __init__(self):
        self.plates: List[Plate] = []

    def add_plate(self, plate):
        self.plates.append(plate)

    def add_plates(self, plates):
        self.plates.extend(plates)

    def find_all_with_weight_greater_than(self, weight):
        return list(filter(lambda plate: plate.get_max_food_weight() > weight, self.plates))

    def find_by_form(self, shape):
        return list(filter(lambda plate: isinstance(plate, SaladPlate) and plate.shape == shape, self.plates))

    def main(self):
        soup_plate = SoupPlate(10, "ceramic", "blue", 5, "tomato soup")
        salad_plate = SaladPlate(12, "glass", "transparent", "round", True)
        meat_plate = MeatPlate(8, "steel", "orange", 6, "porch")
        dessert_plate = DessertPlate(9, "ceramic", "red", "blueberry", "ice cream")

        plates = [soup_plate, salad_plate, meat_plate, dessert_plate]

        self.add_plate(soup_plate)
        self.add_plate(salad_plate)
        self.add_plate(meat_plate)
        self.add_plate(dessert_plate)

        plates_with_weight_greater_than_50 = self.find_all_with_weight_greater_than(50)
        print("Plates with weight greater than 50:")
        for plate in plates_with_weight_greater_than_50:
            print(plate)

        plates_by_form = self.find_by_form()
        print("\nPlates by form:")
        for plate in plates_by_form:
            print(plate)


manager = PlateManager()
manager.main()
