#Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.

import math

radius = float(input("Enter radius(in cm): "))
height = float(input("Enter height(in cm): "))

volume_cm3 = math.pi * r * r * h

# convert to litres
volume_litres = volume_cm3 / 1000

cost = volume_litres * 40

print("Volume of cylinder:", volume_cm3, "cm^3")
print("Volume in litres:", volume_litres, "L")
print("Cost of milk: Rs.", cost)