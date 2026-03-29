#User will input (2numbers).Write a program to swap the numbers

print("Program to swap two numbers")
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

print(f"The numbers are {num1} and {num2} ")

num3 = num1
num1 = num2
num2 = num3

print(f"Swapped numbers are {num1} and {num2}")