class Car:
    def __init__(self, name, coord1, coord2, horizontal):
        self.name = name
        self.coord1 = coord1
        self.coord2 = coord2
        self.horizontal = horizontal

    def __repr__(self):
        print_list = [self.name, self.coord1, self.coord2, self.horizontal]
        return print_list.__repr__()
