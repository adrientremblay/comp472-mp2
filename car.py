class Car:
    def __init__(self, name, coord1, coord2, horizontal, fuel):
        self.name = name
        self.coord1 = coord1
        self.coord2 = coord2
        self.horizontal = horizontal
        self.fuel = fuel

    def __repr__(self):
        print_list = [self.name, self.coord1, self.coord2, self.horizontal, self.fuel]
        return print_list.__repr__()
