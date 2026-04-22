#Write  a program that will tell whether the given number is divisible by 3 & 6.
try:
  user_num = int(input("Enter one number(integer) to check if it is divisible by 3 and 6 or not: "))

  if user_num % 6 == 0:
    print(f"The number {user_num} is divisible both by 3 and 6.")
  else:
    print(f"The number {user_num} is not divisible by 3 and 6.")

except ValueError:
  print("Please enter correct data type")