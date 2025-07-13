from math import sqrt
from src.figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if min(side_a, side_b, side_c) <= 0:
            raise ValueError("Triangle sides must be positive")

        if (
            side_a + side_b <= side_c
            or side_a + side_c <= side_b
            or side_b + side_c <= side_a
        ):
            raise ValueError("Triangle inequality violated")

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        return sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
