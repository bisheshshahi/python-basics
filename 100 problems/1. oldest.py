#User will input (3ages).Find the oldest one

print("Check the oldest age")
num1 = float(input("Enter 1st age: "))
num2 = float(input("Enter 2nd age: "))
num3 = float(input("Enter 3rd age: "))

if num1>num2 and num1>num3:
   print(num1)

elif num2>num1 and num2>num3:
  print(num2)

else:
  print(num3)
