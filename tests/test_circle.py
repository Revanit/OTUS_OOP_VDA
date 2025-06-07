import pytest
from math import pi
from src.circle import Circle


@pytest.mark.parametrize(
    ("radius", "expected_area"),
    [
        (1, pi),
        (2.5, pi * 2.5**2),
    ],
    ids=["int radius", "float radius"],
)
def test_circle_area(radius, expected_area):
    c = Circle(radius)
    assert c.get_area() == pytest.approx(expected_area)


@pytest.mark.parametrize(
    ("radius", "expected_perimeter"),
    [
        (1, 2 * pi),
        (2.5, 2 * pi * 2.5),
    ],
    ids=["int radius", "float radius"],
)
def test_circle_perimeter(radius, expected_perimeter):
    c = Circle(radius)
    assert c.get_perimeter() == pytest.approx(expected_perimeter)


def test_circle_invalid_radius():
    with pytest.raises(ValueError):
        Circle(0)


def test_circle_add_area():
    c1 = Circle(1)
    c2 = Circle(2)
    expected = c1.get_area() + c2.get_area()
    assert c1.add_area(c2) == pytest.approx(expected)


def test_circle_add_area_invalid():
    c1 = Circle(1)
    with pytest.raises(ValueError):
        c1.add_area("not a figure")
