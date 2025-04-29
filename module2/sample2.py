'''
ATM Pin System

Problem Details

User must input the correct pin to access the services
allowed 3 times

Services includes

1. Check Balance
2. Withdraw
3. Exit

Logical Flow

1. Set correct PIN
2. Ask user to input PIN
3. Allowed max 3 times
4. If successful show the menu
'''

import os
os.system('cls' if os.name =='nt' else 'clear')

correct_pin = "1234"
balance = 1000
tries = 3

while tries>0:
    pin = input("Enter your 4 digit PIN: ")
    if pin == correct_pin:
        print ("access Granted! \n")
        while True:
            print ("\nATM MENU")
            print ("1. Check Balance")
            print ("2. Withdraw")
            print ("3. Exit ")
            choice = input("Enter choice: ")

            if choice == "1":
                print (f"Your balance is {balance:.2f}")
            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                if amount <= balance:
                    balance -= amount
                    print (f"Withdrew {amount:.2f}, Balance {balance:.2f}")
                else:
                    print ("Insufficient balance!")
            elif choice == "3":
                print ("Thank you ...")
                break
            else:
                print ("Invalid Input ")
        break
    else:
        tries -= 1
        print (f"Wrong PIN! {tries} tries left.")
        
if tries == 0:
    print ("Card Blocked. contact bank")
