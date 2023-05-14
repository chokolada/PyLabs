class Plate:
    instance = None  # static field

    def __str__(self):
        return f"Plate(diameter={self.diameter}, material='{self.material}', color='{self.color}', isClean={self.isClean}, hasFood={self.hasFood})"

    def __init__(self, diameter, material, color, isClean=False, hasFood=False):
        self.diameter = diameter
        self.material = material
        self.color = color
        self.isClean = isClean
        self.hasFood = hasFood

    def wash(self):
        self.isClean = True

    def dirty(self):
        self.isClean = False

    def eat(self):
        self.hasFood = False
        self.dirty()

    def add_food(self):
        self.hasFood = True

    @staticmethod
    def get_instance():
        if Plate.instance is None:
            Plate.instance = Plate(10, "ceramic", "blue")
        return Plate.instance


plate = Plate.get_instance()
print(plate)
