#Write a program that take a user input of three angles and will find out whether it can form a triangle or not.

first_angle = int(input("Enter 1st angle: "))
second_angle = int(input("Enter 2nd angle: "))
third_angle = int(input("Enter 3rd angle: "))

if first_angle+second_angle+third_angle != 180:
  print("The angles cannot form a triangle")
else:
  print("The angles can form a triangle")