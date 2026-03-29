#Write a program that will give you the sum of 3 digits

num = int(input("Enter 3 digit number: "))

if len(str(num))<4 and len(str(num))>2:
  last_digit = num%10

  num = num//10

  first_digit = num//10
  print("First digit is",first_digit)

  sec_digit = num%10
  print("Second digit is",sec_digit)
  print("Last digit is", last_digit)

  print(f"The sum of 3 digits is",first_digit+sec_digit+last_digit)

else:
  print("Wrong input")