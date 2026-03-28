# Simple software for ATM

class Atm:

    # Static variable
    __counter = 1

    def __init__(self):

        # Instance variables
        self.__pin = ""
        self.__balance = 0
        self.sno = Atm.__counter
        Atm.__counter += 1

    # Get the value of pin using method
    def get_pin(self):
        return self.__pin

    # Set the value of pin using method
    def set_pin(self, new_pin):
        if type(new_pin) == str:
            self.__pin = new_pin
            print("Pin changed")

    def menu(self):
        # Menu runs once per call — call it again manually for next interaction
        user_input = input("""
                              Hello, How are you!
                              1. Enter 1 to create your pin.
                              2. Enter 2 to deposit amount.
                              3. Enter 3 to withdraw amount.
                              4. Enter 4 to view your balance.
                              5. Enter 5 to exit.
                              6. Enter 6 to check your serial number.
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

        elif user_input == "6":
            print("Your serial number is" , self.sno)
        
        else:
            print("Invalid option!")

    def create_pin(self):
        if self.__pin:
            print("Pin already set.")
            return
        self.__pin = input("Create your pin: ").strip()
        print("Pin created successfully.")

    def deposit(self):
        temp = input("Enter your pin: ").strip()
        if temp == self.__pin:
            amount = float(input("Enter the amount you want to deposit: ").strip())
            self.__balance += amount
        else:
            print("Incorrect pin!")

    def withdraw(self):
        temp = input("Enter your pin: ").strip()
        if temp == self.__pin:
            amount = float(input("Enter the amount you want to withdraw: ").strip())
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient amount.")
        else:
            print("Incorrect pin!")

    def check_balance(self):
        temp = input("Enter your pin: ").strip()
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("Incorrect pin!")
