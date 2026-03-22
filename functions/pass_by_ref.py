class Customer:
  def __init__(self,name,gender):
    self.name = name
    self.gender = gender

def greet(customer):
    
    if customer.gender == "Male":
     print("Hello", customer.name , "Sir")

    elif customer.gender == "Female":
     print("Hello", customer.name , "Ma'am")
    
    else:
     print("Hello", customer.name)


cust = Customer("Bishesh", "Male")
print(cust.name)

greet(cust)