import pytest
from src.area import calculate_area_square
from src.area import calculate_area_triangle


def test_calculate_area_square():
    assert calculate_area_square(2) == 4
    assert calculate_area_square(2.5) == 6.25
    assert calculate_area_square(3) == 9


def test_calculate_area_square_negative():
    with pytest.raises(TypeError):
        calculate_area_square(-2)


def test_calculate_area_square_string():
    with pytest.raises(TypeError):
        calculate_area_square("2")


def test_calculate_area_square_list():
    with pytest.raises(TypeError):
        calculate_area_square([2])


def test_calcuate_area_triangle():
    assert calculate_area_triangle(5, 10) == 25
    assert calculate_area_triangle(2, 4) == 4
    assert calculate_area_triangle(1, 1) == 0.5


def test_calculate_area_triangle_negative():
    with pytest.raises(TypeError):
        calculate_area_triangle(-2, 5)
    with pytest.raises(TypeError):
        calculate_area_triangle(2, -5)
    with pytest.raises(TypeError):
        calculate_area_triangle(-2, -5)
