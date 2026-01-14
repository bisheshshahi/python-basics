import random

#prints random number from 1 to 100
num = random.randrange(1,101)
print(num)
count = 0       #initialized attempt counter

print("Guess the number between 1 and 100")

#infinite loop, stops after user guesses the number
while True:
  try:
    user_num = int(input("Enter a number(integer):"))

      #Ask for valid input
    if not (user_num>=1 and user_num<=100):
      print("Please enter a number between 1 to 100.")
      continue

    count = count+1     #no. of attempts
    
    if user_num<num:    
      print(f"The secret number is bigger than this.\nNo. of attempts={count}")

    elif user_num>num:
      print(f"The secret number is smaller than this.\nNo. of attempts={count}")

    else:
      print("Congratulations you guessed the number correctly.")
      print(f"You guessed the number in {count} tries.")
      break       #exits the loop

  except Exception:       #handle invalid input
    print("Enter numbers only") 