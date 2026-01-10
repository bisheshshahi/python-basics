#Simple calculator for 2 numbers
print("This is the program for addition, multiplication or division")

num1 = float(input("Enter 1st number:"))
num2 = float(input("Enter 2nd number:"))

add = num1 + num2
multiply = num1 * num2
divide = num1 / num2

check = int(input("Enter 1 to add both numbers,2 to multiply and 3 to divide:"))
if check == 1:
  print("The sum of",num1,"and",num2,"is",add)
elif check == 2:
  print("The multiplication of",num1,"and",num2,"is",multiply)
elif check == 3:
  print("The division of",num1,"and",num2,"is",divide)
else:
  print("Please enter a valid choice:1,2,3")