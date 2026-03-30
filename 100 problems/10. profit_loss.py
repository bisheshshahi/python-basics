#Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit

cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

if cost_price<selling_price:
  print("You've made profit")

elif cost_price>selling_price:
  print("You've made loss")

else:
  print("You gained nothing also lost nothing")