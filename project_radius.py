#write a Python program which accepts the radius of a circle from the user and computes area

import math

radius = float(input("Input the radius of the circle: "))

area = math.pi * radius ** 2
print("The area of the circle with radius", radius, "is:", area)
