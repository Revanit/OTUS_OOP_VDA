import pytest
from math import sqrt
from src.triangle import Triangle


@pytest.mark.parametrize(
    ("a", "b", "c", "expected_area"),
    [
        (3, 4, 5, 6.0),
        (7, 8, 9, sqrt(12 * (12 - 7) * (12 - 8) * (12 - 9))),
    ],
    ids=["right triangle", "scalene triangle"],
)
def test_triangle_area(a, b, c, expected_area):
    t = Triangle(a, b, c)
    assert t.get_area() == pytest.approx(expected_area)


@pytest.mark.parametrize(
    ("a", "b", "c", "expected_perimeter"),
    [
        (3, 4, 5, 12),
        (7, 8, 9, 24),
    ],
    ids=["right triangle", "scalene triangle"],
)
def test_triangle_perimeter(a, b, c, expected_perimeter):
    t = Triangle(a, b, c)
    assert t.get_perimeter() == expected_perimeter


@pytest.mark.parametrize(
    ("a", "b", "c"),
    [
        (1, 2, 3),
        (10, 1, 1),
        (0, 5, 5),
        (-1, 5, 5),
    ],
    ids=["invalid sides (sum)", "invalid (too long)", "zero side", "negative side"],
)
def test_triangle_invalid(a, b, c):
    with pytest.raises(ValueError):
        Triangle(a, b, c)


def test_triangle_add_area():
    t1 = Triangle(3, 4, 5)
    t2 = Triangle(6, 8, 10)
    expected = t1.get_area() + t2.get_area()
    assert t1.add_area(t2) == pytest.approx(expected)


def test_triangle_add_area_invalid():
    t = Triangle(3, 4, 5)
    with pytest.raises(ValueError):
        t.add_area("not a figure")
