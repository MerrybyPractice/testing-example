import pytest
import math
from testing_example.main import(
     save_dict, 
     square_area, 
     square, 
     circle_area, 
     circle, 
     triangle_area,
     area_by_shape,
)
from testing_example import __version__


def test_version():
    assert __version__ == '0.1.0'

def test_save_dict_exists(): 
    assert save_dict 

def test_square_area_exists(): 
    assert square_area

# 2 => 4, 3 => 9, 0 => 0
squ_params = [
    ('zeros', 0, (0,0)), ('negative', -2, (-2,4)), ('basic even', 2, (2,4)), ('basic odd', 3, (3,9)), ('large even', 432, (432,186624)), ('large odd', 431, (431, 185761)), ("large_negative", -431, (-431,185761)), ("negative_one", -1, (-1, 1)), ('decim', 2.2, (2.2, 4.840000000000001)), ("large_dec", 431.42, (431.42, 186123.2164))]
@pytest.mark.parametrize('label, actual, expected', squ_params)
def test_square_parameterized(actual, expected, label): 
    


    assert square_area(actual) == expected

def test_square_area_happy_path(): #Parameterize 
    expected = 2, 4 
    actual = square_area(2)
    assert actual == expected

# def test_square_area_zero(): 
#     expected = 0, 0
#     actual = square_area(0)
#     assert actual == expected

# def test_square_area_negative(): 
#     expected = -2, 4
#     actual = square_area(-2)
#     assert actual == expected

def test_square_area_string(): 
    with pytest.raises(TypeError): 
        square_area("Wrong")

def test_square_area_is_tup(): #Parameterize
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

def test_circle_area_happy_path(): #Parameterize 
    expected = (5, 19.63) 
    actual = circle_area(5)
    assert actual == expected 

# def test_circle_area_zero():
#     expected = (0, 0)
#     actual = circle_area(0) 
#     assert actual == expected

# def test_circle_area_negative(): 
#     expected = (-5, 19.63)
#     actual = circle_area(-5)
#     assert actual == expected

# def test_circle_area_string(): 
#     with pytest.raises(TypeError): 
#         circle_area("should not work")

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

def test_triangle_area_happy_path(): #Parameterize
    expected = 4, 3, 6
    actual = triangle_area(4, 3)
    assert actual == expected

# def test_triangle_zero():
#     expected = 0, 0, 0
#     actual = triangle_area(0, 0) 
#     assert actual == expected

# def test_triangle_negatives_both(): 
#     # expected behavior or something to correct?   
#     expected = -4, -3, 6
#     actual = triangle_area(-4, -3)
#     assert actual == expected

# def test_triangle_negatives_one(): 
#     # feature or something to correct? 
#     expected = -4, 3, -6
#     actual = triangle_area(-4, 3)
#     assert actual == expected 

# def test_triangle_string(): 
#     with pytest.raises(TypeError): 
#         triangle_area("why is this getting a string?")

def test_add_triangle_to_save_dict(): 
    triangle = {}
    save_dict(((4, 3), 6,), triangle)
    assert len(triangle) == 1

def test_add_triangle_to_save_dict_val():
    triangle = {}
    save_dict(((4, 3), 6), triangle)
    assert triangle[4,3] == 6 

def test_area_by_shape(): 
    assert area_by_shape

def test_area_by_shape_return_circle(): 
    #input:  String shape, int size param ** diff for each 
    #output: Area float  
    expected = 19.63 
    actual = area_by_shape("Circle", 5)
    assert actual == expected

def test_area_by_shape_return_square(): 
    expected = 4 
    actual = area_by_shape("Square", 2)
    assert actual == expected

def test_area_by_shape_return_triangle(): 
    expected = 6 
    actual = area_by_shape("Triangle", 3, 4)
    assert actual == expected