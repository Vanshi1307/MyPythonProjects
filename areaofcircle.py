import math

try:
    radius = float(input("Enter the radius of the circle: "))
    if radius < 0:
        print("Error: Radius cannot be negative.")
    else:
        area = math.pi * radius ** 2
        print(f"The area of the circle with radius {radius} is: {area:f}")
except ValueError:
    print("Error: Please enter a valid number for the radius.")
