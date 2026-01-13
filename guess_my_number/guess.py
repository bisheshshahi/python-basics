import random

num = random.randrange(1,101)
print(num)

while True:
  try:
    user_num = int(input("Enter a number(integer):"))
    if user_num<num:
      print("The number is smaller.")
    elif user_num>num:
      print("The number is bigger.")
    else:
      print("Congratulations you guessed the number correctly.")
      break
  except Exception:
    print("Enter numbers only")