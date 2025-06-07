from src.rectangle import Rectangle
from src.square import Square
import pytest


@pytest.mark.parametrize(
    "type_of_number", ["integer", "float"], ids=["integer", "float"]
)
def test_rectangle_area_positive(api_server, type_of_number):
    side_a, side_b, area = api_server(type_of_number=type_of_number)
    r = Rectangle(side_a, side_b)
    assert r.get_area() == area


@pytest.mark.parametrize(
    ("side_a", "side_b"), [(0, 5), (-1, 5.5)], ids=["zero value", "negative value"]
)
def test_rectangle_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


@pytest.mark.parametrize(
    ("side_a", "side_b", "expected_perimeter"),
    [
        (3, 4, 14),
        (5.5, 2, 15.0),
    ],
    ids=["integer", "float"],
)
def test_rectangle_perimeter(side_a, side_b, expected_perimeter):
    r = Rectangle(side_a, side_b)
    assert r.get_perimeter() == expected_perimeter


def test_rectangle_add_area():
    r = Rectangle(3, 4)
    s = Square(5)
    total_area = r.add_area(s)
    assert total_area == r.get_area() + s.get_area()


def test_rectangle_add_area_invalid():
    r = Rectangle(3, 4)
    with pytest.raises(ValueError):
        r.add_area("not a figure")
