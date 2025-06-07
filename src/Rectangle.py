from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Should be a Figure")
        return self.get_area + other_figure.get_area


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Rectangle sides can't be less than 0")
        self.side_a = side_a
        self.side_b = side_b

    @property
    def get_area(self):
        return self.side_a * self.side_b

    @property
    def get_perimeter(self):
        return (self.side_a + self.side_b) * 2


class Square(Rectangle):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("Square sides can't be less than 0")
        super().__init__(side_a, side_a)


r = Rectangle(3, 5)
s = Square(5)
print(r.add_area(s))
print(s.add_area(r))








# r = Rectangle(3, 5)
# s = Square(5)
# print(r.add_area(s))

# class Example:
#
#     def __init__(self, number: int, name: str):
#         self.number = number
#         self.name = name
#
#     def __str__(self):
#         return f'Class with {self.number} and {self.name}'
#
#
# a = Example(number=15, name='John')
# print(a)


#
#
# class Figure(ABC):
#
#     def __init__(self, name):
#         self.name = name
#
#     @abstractmethod
#     def get_area(self):
#         pass
#
#     @abstractmethod
#     def get_perimeter(self):
#         pass
#
#     def add_area(self, other_figure):
#         if not isinstance(other_figure, Figure):
#             raise ValueError("Нужен класс Figure")
#         return self.get_area() + other_figure.get_area()
#
#
# class Rectangle(Figure):
#
#     def __init__(self, side_a: int, side_b: int):
#         super().__init__(name="Rectangle")
#         if side_a <= 0 or side_b <= 0:
#             raise ValueError("side_a and aide_b should be greate than 0")
#         self.side_a = side_a
#         self.side_b = side_b
#
#     @property
#     def get_area(self):
#         return self.side_a * self.side_b
#
#     @property
#     def get_perimeter(self):
#         return 2 * (self.side_a + self.side_b)
#
#
# class Square(Rectangle):
#     def __init__(self, side_a):
#         if side_a <= 0:
#             raise ValueError("...")
#         super().__init__(side_a, side_a)
#         self.name = "Square"
#
#
# r = Rectangle(3, 5)
# print(r.get_area)
