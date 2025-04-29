'''
Banking System

Menu
    Deposit
    Withdraw
    Check Balance
    Exit

Logical Flow
1. Start with balance = 0
2. Show menu
3. Ask user for choice
4. Perform the operation (menu 1-4)
5. Loop is terminated if the user selects 4
'''
import os
os.system('cls' if os.name =='nt' else 'clear')

balance = 0

while True:
    print ("\n---Banking System---")
    print ("1. Deposit")
    print ("2. Withdraw")
    print ("3. Check Balance")
    print ("4. Exit")

    choice = input("Enter choice: ") #type string
    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print (f"Deposited {amount:.2f}, New Balance is {balance:.2f}")
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print (f"Withdrew {amount:.2f}, New Balance is {balance:.2f}")
        else:
            print ("Insufficient balance!")
    elif choice == "3":
        print (f"Current Balance is {balance:.2f}")
    elif choice == "4":
        print ("Thank you for using banking System")
        break 
    else:
        print ("invalid choice, try again")


