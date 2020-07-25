import math

square = {}
circle = {}
triangle = {}

def save_dict(tup, dict): 
    dict[tup[0]] = tup[1]

def square_area(val): 
    area = val**2
    return val, area

def circle_area(diam): 
    rad = diam/2 
    area = (rad**2) * math.pi 
    area = round(area, 2)
    return diam, area

def triangle_area(base, height): 
    area = (base * height)/2 
    return base, height, area 

def area_by_shape(shape, size, tri_val=0): 
    if shape == "Circle": 
        circle_tup =  circle_area(size)
        circ_area = circle_tup[1]
        return circ_area
    elif shape == "Square": 
        square_tup = square_area(size)
        squ_area = square_tup[1]
        return squ_area
    elif shape == "Triangle": 
        tri_tup = triangle_area(size, tri_val)
        tri_area = tri_tup[2]
        return tri_area