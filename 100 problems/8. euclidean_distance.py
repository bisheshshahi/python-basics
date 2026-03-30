#Write a program to find the euclidean distance between two coordinates.
import math

x1,y1 = 10,20
x2,y2 = 30,40

euclidean_distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
print("Distance: ", euclidean_distance)