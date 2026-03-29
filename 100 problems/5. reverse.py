#Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

user_num = int(input("Enter 4 digit number: "))

a = str(user_num)

print("The reversed number is",int(a[::-1]))
