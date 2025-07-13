from math import pi
from src.figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def get_area(self):
        return pi * self.radius**2

    def get_perimeter(self):
        return 2 * pi * self.radius
