import numpy as np #np as alias

try:
  num_arr = int(input("Enter how many numbers are you going to store in the array: "))

  if num_arr<=0:
    print("Array cannot be empty")

  else:
    temp_list = []
    for i in range(0,num_arr):
      try:
        user_num = int(input(f"Enter number {i+1} to store in array of numpy: "))
        temp_list.append(user_num)
      except ValueError:
        print("Invalid input")
    print(np.array(temp_list))

except ValueError:
  print("Wrong data type")
  print("Please enter integer data type")
