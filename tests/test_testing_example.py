import pytest
import math
from testing_example.main import(
     save_dict, 
     square_area, 
     square, 
     circle_area, 
     circle, 
     triangle_area,
)
from testing_example import __version__


def test_version():
    assert __version__ == '0.1.0'

def test_save_dict_exists(): 
    assert save_dict 

def test_square_area_exists(): 
    assert square_area

def test_square_area_happy_path(): 
    expected = 2, 4 
    actual = square_area(2)
    assert actual == expected

def test_square_area_zero(): 
    expected = 0, 0
    actual = square_area(0)
    assert actual == expected

def test_square_area_negative(): 
    expected = -2, 4
    actual = square_area(-2)
    assert actual == expected

def test_square_area_string(): 
    with pytest.raises(TypeError): 
        square_area("Wrong")

def test_square_area_is_tup(): 
    expected = tuple 
    actual = type(square_area(1)) 
    assert actual == expected

def test_add_to_square_to_save_dict(): 
    square = {}
    save_dict((2, 4), square)
    assert len(square.keys()) == 1

def test_add_to_square_to_save_dict_val(): 
    square = {}
    save_dict((2,4), square)
    assert square[2] == 4

def test_circle_area_exists(): 
    assert circle_area

def test_circle_area_happy_path(): 
    expected = (5, 19.63) 
    actual = circle_area(5)
    assert actual == expected 

def test_circle_area_zero():
    expected = (0, 0)
    actual = circle_area(0) 
    assert actual == expected

def test_circle_area_negative(): 
    expected = (-5, 19.63)
    actual = circle_area(-5)
    assert actual == expected

def test_circle_area_string(): 
    with pytest.raises(TypeError): 
        circle_area("should not work")

def test_circle_dict_exists(): 
    assert circle == {}

def test_square_dict_exists(): 
    assert square == {}

def test_add_circle_to_save_dict(): 
    circle = {} 
    save_dict((5, 19.63), circle)
    expected = 1 
    actual = len(circle)
    assert actual == expected 

def test_add_circle_to_save_dict_val(): 
    circle = {}
    save_dict((5, 19.63), circle) 
    expected = 19.63 
    actual = circle[5]
    assert actual == expected

def test_triangle_area_exists(): 
    assert triangle_area

def test_triangle_area_happy_path(): 
    expected = 4, 3, 6
    actual = triangle_area(4, 3)
    assert actual == expected

def test_triangle_zero():
    expected = 0, 0, 0
    actual = triangle_area(0, 0) 
    assert actual == expected

def test_triangle_negatives_both(): 
    # expected behavior or something to correct?   
    expected = -4, -3, 6
    actual = triangle_area(-4, -3)
    assert actual == expected

def test_triangle_negatives_one(): 
    # feature or something to correct? 
    expected = -4, 3, -6
    actual = triangle_area(-4, 3)
    assert actual == expected 

def test_triangle_string(): 
    with pytest.raises(TypeError): 
        triangle_area("why is this getting a string?")

def test_add_triangle_to_save_dict(): 
    triangle = {}
    save_dict(((4, 3), 6,), triangle)
    assert len(triangle) == 1

def test_add_triangle_to_save_dict_val():
    triangle = {}
    save_dict(((4, 3), 6), triangle)
    assert triangle[4,3] == 6 