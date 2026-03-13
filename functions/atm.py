#Simple software for atm

class Atm:

    def __init__(self):
      self.pin = ""
      self.balance = 0
      self.menu()

    def menu(self):
      while True:
        user_input = input("""
                          Hello, How are you!
                          1. Enter 1 to create your pin.
                          2. Enter 2 to deposit amount.
                          3. Enter 3 to withdraw amount.
                          4. Enter 4 to view your balance.
                          5. Enter 5 to exit.
                          """)
        if user_input == "1":
          self.create_pin()
        
        elif user_input == "2":
          self.deposit()

        elif user_input == "3":
          self.withdraw()
        
        elif user_input == "4":
          self.check_balance()
        
        elif user_input == "5":
          print("GoodBye")
          break
        
        else:
          print("Invalid option!")
      
    def create_pin(self):
      if self.pin:
        print("Pin already set.")
        return
      self.pin = input("Create your pin: ")
      print("Pin created successfully.")

    def deposit(self):
      temp = input("Enter your pin: ")
      if temp == self.pin:
        amount = int(input("Enter the amount you want to deposit: "))
        self.balance += amount
      else:
        print("Incorrect pin!")

    def withdraw(self):
      temp = input("Enter your pin: ")
      if temp == self.pin:
        amount = int(input("Enter the amount you want to withdraw: "))
        if amount<=self.balance:
          self.balance -= amount
          print("Withdrawal successful.")
        else:
          print("Insufficient amount.")
      else:
        print("Incorrect pin!")
    
    def check_balance(self):
      temp = input("Enter your pin: ")
      if temp == self.pin:
        print(self.balance)
      
      else:
        print("Incorrect pin!")
      



bishesh = Atm()