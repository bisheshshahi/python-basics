#Palin as palindrome

def palin(check,original):
  if len(check)<=1:
    print(f"The given text '{original}' is palindrome.")
  else:
    if check[0] == check[-1]:
      palin(check[1:-1],original)
    else:
      print(f"The given text '{original}' is not a palindrome.")

while True:
  text = input("Enter the word to check whether the word is palindrome or not (or type 'exit' to quit): ")
  if text.lower().strip() == "exit":
    break
  palin(text,text)