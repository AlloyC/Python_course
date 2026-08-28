# Check balance
# Withdraw
# Transfer
# Buy airtime
# Buy data

# Class for the data creation

class User:
    def __init__(self, name, pin, amount, bank):
        self.username = name
        self.pin = int(pin)
        self.amount = amount
        self.bank = bank

# database
Users = [
    User("Matthew", 1212, 50000, "Access"),
    User("Peter", 1272, 60000, "GTB"),
    User("Joel", 1234, 70000, "Opay")
]

def verify_pin():
    for x in range(5):
        pin = int(input("Please enter your pin: "))
        for y in Users:
            if pin == y.pin:
                return Users.index(y)
        if x == 4:
            print("Account blocked!")
        else:
           print("incorrect pin")
    return -1

def option_selection():
    options= '''
    select option:
    1. withdraw
    2. check balance
    3. transfer
    4. airtime
    5. data
            '''
    print(options)
    option = int(input("Enter option (1-5): "))
    return option

def welcome():
    print("Welcome, ")
    global id
    id = verify_pin()
    if id != -1:
        print(f"Welcome, {Users[id].username} to {Users[id].bank}")

def withdraw(amount = 0):
    if amount == 0:
        amount = int(input("Enter amount: "))
    index = verify_pin()
    if index == id:
        Users[id].amount -= amount
        print("withdraw successful")
    elif index != -1:
        print("invalid password")
        withdraw(amount)

def check_balance():
    index = verify_pin()
    if index == id:
        print(Users[id].amount)
    elif index != -1:
        print("invalid password")
        check_balance()

def transfer(amount = 0):
    account_number = int(input("Enter account number: "))
    if amount == 0:
        amount = int(input("Enter amount: "))
    index = verify_pin()
    if index == id:
        if Users[id].amount < amount:
            print("Insufficient funds")
        else:
            Users[id].amount -= amount
            print("Transfer successful")
    elif index != -1:
        print("invalid password")
        transfer(amount)        

def processing(initalized = True):
    if initalized:
        welcome()
    if id != -1:
        value = option_selection()
        if value == 1:
            withdraw()
        elif value == 2:
            check_balance()
        elif value == 3:
            transfer()
        elif value == 4:
            pass #airtime()
        elif value == 5:
            pass #data()
        else:
            print("Invalid selection!!")
            processing(False)
        checking_processing = input("Would you like to exit(Y/N): ")
        if checking_processing.lower() == "y":
            print("Thanks for banking with us, good bye.")
        else:
            processing(False)

processing()