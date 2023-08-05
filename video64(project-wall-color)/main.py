import math


def calculate_number_cans(height, width, covrage):
    area_of_wall = height*width
    number_of_cans = area_of_wall/covrage
    return (math.ceil(number_of_cans))


try:
    wall_height = int(input("Enter wall height? "))
    wall_width = int(input("Enter wall width? "))
    covrage = int(input("Enter covrage each cans? "))
except:
    print("not valid")
else:
    print(calculate_number_cans(wall_height, wall_width, covrage))
