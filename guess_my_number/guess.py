import random
print("Guess the number game")
num = random.randrange(1,101)
print(num)
user_num = int(input("Guess the number(integer):"))

while(user_num!=num):
  # user_num = int(input("Guess the number:"))
  if user_num == num:
    print("Congratulations you guessed the correct number.")
  elif user_num<num:
    print("The number is smaller.")
    user_num = int(input("Guess the number:"))
  elif user_num>num:
    print("The number is bigger.")
    user_num = int(input("Guess the number:"))
  else:
    print("Please enter one positive integer")
    user_num = int(input("Guess the number:"))    