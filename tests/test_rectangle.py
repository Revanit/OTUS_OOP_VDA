from src.Rectangle import Rectangle
import pytest


@pytest.mark.parametrize("type_of_number",
                         ["integer",
                          "float"],
                         id=["asd"])
def test_rectangle_area_positive(api_server, type_of_number):
    side_a, side_b, area = api_server(type_of_number=type_of_number)
    print(side_a, side_b, area)
    r = Rectangle(side_a, side_b)
    assert r.get_area == area


@pytest.mark.parametrize(
    ("side_a", "side_b"),
    [
        (0, 5),
        (-1, 5.5)
    ],
    ids=["zero value", "negative value"]
)
def test_rectangle_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)
