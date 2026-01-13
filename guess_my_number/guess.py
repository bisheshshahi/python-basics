import random

#prints random number from 1 to 100
num = random.randrange(1,101)
print(num)
count = 0

print("Guess the number between 1 and 100")

#loop
while True:
  try:
    user_num = int(input("Enter a number(integer):"))
    if not (user_num>=1 and user_num<=100):
      print("Please enter a number between 1 to 100.")
      continue
    count = count+1     #no. of attempts
    if user_num<num:
      print(f"The secret number is smaller than this.\nNo. of attempts={count}")
    elif user_num>num:
      print(f"The secret number is bigger than this.\nNo. of attempts={count}")
    else:
      print("Congratulations you guessed the number correctly.")
      print(f"You guessed the number in {count} tries.")
      break
  except Exception:
    print("Enter numbers only")