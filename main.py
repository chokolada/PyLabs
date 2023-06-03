from manager.lab_8_plate_manager import PlateManager
from models.lab_8_meat_plate import MeatPlate
from models.lab_8_salad_plate import SaladPlate
from models.lab_8_soup_plate import SoupPlate
from models.lab_8_dessert_plate import DessertPlate
from decorators.lab8_plate_decorator import logged


@logged(Exception, mode="console")
def main():
    plate_manager = PlateManager()

    soup_plate = SoupPlate(10, "ceramic", "blue", 5, "tomato soup")
    salad_plate = SaladPlate(12, "glass", "transparent", "round", True)
    meat_plate = MeatPlate(8, "steel", "orange", 6, "porch")
    dessert_plate = DessertPlate(9, "ceramic", "red", "blueberry", "ice cream")

    plate_manager.add_plate(soup_plate)
    plate_manager.add_plate(salad_plate)
    plate_manager.add_plate(meat_plate)
    plate_manager.add_plate(dessert_plate)

    print(plate_manager.list_of_weights())
    plate_manager.indexed_list()
    plate_manager.numeric_list()
    print(plate_manager.check_condition_all_any(5))

    plates_with_weight_greater_than_50 = plate_manager.find_all_with_weight_greater_than(50)
    print("Plates with weight greater than 50:")
    for plate in plates_with_weight_greater_than_50:
        print(plate)

    plates_by_form = plate_manager.find_by_form("round")
    print("\nPlates by form:")
    for plate in plates_by_form:
        print(plate)


# Call the main function
main()
