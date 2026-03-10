#Palin as palindrome

text = input("Enter the word to check whether the word is palindrome or not: ")

def palin(check,original):
  if len(check)<=1:
    print(f"The given text '{original}' is palindrome.")
  else:
    if check[0] == check[-1]:
      palin(check[1:-1],original)
    else:
      print(f"The given text '{original}' is not a palindrome.")

palin(text,text)