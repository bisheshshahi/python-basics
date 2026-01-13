import random

#prints random number from 1 to 100
num = random.randrange(1,101)
print(num)
count = 0

#loop
while True:
  try:
    user_num = int(input("Enter a number(integer):"))
    count = count+1     #no. of attempts
    if user_num<num:
      print("The number is smaller.\n","No. of attempts=",count)
    elif user_num>num:
      print("The number is bigger.\n","No. of attempts=",count)
    else:
      print("Congratulations you guessed the number correctly.")
      print("You guessed the number in",count,"tries.")
      break
  except Exception:
    print("Enter numbers only")