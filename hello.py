#to find area of circle
import math
def area_of_circle(radius):
    return math.pi * radius * radius 

try:
    radius = float(input("Enter the radius of the circle: "))
    if radius >= 0:
        area = area_of_circle(radius)   
        print(f"The area of the circle with radius {radius} is {area}")
    else: 
        print("Radius cannot be negative.")
except ValueError:
    print("Please enter a valid number for the radius.")     
