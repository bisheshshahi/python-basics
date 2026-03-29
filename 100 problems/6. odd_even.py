#Write a program that will tell whether the number entered by the user is odd or even.

user_num = int(input("Enter one number: "))

if user_num == 0:
  print("Wrong input")

else:
  if user_num % 2 == 0:
    print(f"The number {user_num} is even")
  else:
    print(f"The number {user_num} is odd")
