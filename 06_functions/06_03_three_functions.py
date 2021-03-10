'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''
print("Welcome of My Friendly ATM")
print("What would you like to do today?")
choice = int(input("1=Deposit, 2=Withdraw, 3=Check Balance, 4= Exit: "))
balance = 250.00

def get_balance():
    return balance

def add_funds(num):
    get_balance()
    funds = float(input("Deposit amount: "))
    new_balance = balance + funds
    print(f"You deposited: {funds}")
    print(f"Your balance is now: {new_balance}")
    return new_balance

def withdraw(num):
    get_balance()
    funds = float(input("Withdrawal amount: "))
    if funds < balance:
        new_balance = balance - funds
        print(f"You withdrew: {funds}")
        print(f"Your balance is now: {new_balance}")
        return new_balance
    else:
        print("Insufficient funds.")



if choice == 1:
    add_funds(choice)
elif choice == 2:
    withdraw(choice)
elif choice == 3:
    get_balance()
    print(f"Your current balance is: {balance}")
else:
    print("Good Bye!")


