from models.lab_8_plate import Plate


class MeatPlateException(Exception):
    pass


class MeatPlate(Plate):
    def __init__(self, diameter, material, color, height, meat_type):
        super().__init__(diameter, material, color)
        self.height = height
        self.meat_type = meat_type
        self.pattern = {"spike", "flower", "heart"}

    def get_max_food_weight(self):
        volume = self.diameter * self.diameter * self.height
        return volume

    def __str__(self):
        return f"SoupPlate: diameter={self.diameter}, material={self.material}, color={self.color}," \
               f" height={self.height}, meat_type={self.meat_type}"

    def set_pattern(self, new_pattern):
        if not isinstance(new_pattern, list):
            raise MeatPlateException("Invalid pattern. Expected a list.")
        self.pattern = new_pattern
