import random

num = random.randrange(1,101)
print(num)
count = 0
while True:
  try:
    user_num = int(input("Enter a number(integer):"))
    count= count+1
    if user_num<num:
      print("The number is smaller.")
    elif user_num>num:
      print("The number is bigger.")
    else:
      print("Congratulations you guessed the number correctly.")
      print("You guessed the number in",count,"tries.")
      break
  except Exception:
    print("Enter numbers only")