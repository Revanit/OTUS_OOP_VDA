from src.square import Square
from src.rectangle import Rectangle
import pytest


@pytest.mark.parametrize(
    ("side", "expected_area"),
    [
        (3, 9),
        (4.5, 20.25),
    ],
    ids=["integer side", "float side"],
)
def test_square_area_positive(side, expected_area):
    s = Square(side)
    assert s.get_area() == pytest.approx(expected_area)


@pytest.mark.parametrize(
    ("side", "expected_perimeter"),
    [
        (3, 12),
        (4.5, 18.0),
    ],
    ids=["integer side", "float side"],
)
def test_square_perimeter(side, expected_perimeter):
    s = Square(side)
    assert s.get_perimeter() == expected_perimeter


@pytest.mark.parametrize(
    "side", [0, -1, -3.5], ids=["zero side", "negative int", "negative float"]
)
def test_square_invalid_side(side):
    with pytest.raises(ValueError):
        Square(side)


def test_square_add_area_valid():
    s1 = Square(4)
    r = Rectangle(2, 5)
    expected_total = s1.get_area() + r.get_area()
    assert s1.add_area(r) == expected_total


def test_square_add_area_invalid():
    s = Square(3)
    with pytest.raises(ValueError):
        s.add_area("not a figure")
