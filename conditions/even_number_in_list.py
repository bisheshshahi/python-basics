#Write a program to find if there is user given number in list and trhe number is even 
a=[1,2,3,4,8,9,10]
num = int(input("Enter one number to check if that number is in list or not\n"))

if num in a:
  if num%2==0:
    print("The number is in the list and is even")
  else:
    print("The number is in the list but is not even")  
else:
    print("The number is not in the list")  