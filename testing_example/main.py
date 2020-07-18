import math

square = {}
circle = {}

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
