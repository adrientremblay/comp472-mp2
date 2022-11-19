class Car:
    """
    The purpose of this class is just to make the code more readable. I could have equally used a list of values
    each representing one of these fields.
    """

    def __init__(self, name, coord1, coord2, horizontal, fuel):
        self.name = name
        self.coord1 = coord1
        self.coord2 = coord2
        self.horizontal = horizontal
        self.fuel = fuel

    def __repr__(self):
        print_list = [self.name, self.coord1, self.coord2, self.horizontal, self.fuel]
        return print_list.__repr__()
