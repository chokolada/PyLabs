from lab_8_plate_manager import PlateManager



class SetManager:
    def __init__(self, manager: PlateManager):
        self.manager = manager
        self.current_index = -1

    def __iter__(self):
        for plate in self.manager:
            for set_item in plate.pattern:
                yield set_item

    def __next__(self):
        self.current_index += 1
        if self.current_index >= len(self.manager):
            raise StopIteration
        return self.manager[self.current_index].pattern

    def __len__(self):
        length = 0
        for plates in self.manager:
            length += len(plates.pattern)
        return length

    def __getitem__(self, index):
        for plates in self.manager:
            item = plates[index].pattern
        return item
