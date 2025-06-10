
#data types 
#Banking Application
#Dictionary 
#{Create Account, Deposit, Withdraw, View, Exit}

def banking_app():
    accounts = {}   #dictionary store values
    #name balance 

    def create_account():
        account_number = input ("Enter account number: ")
        if account_number in accounts:
            print ("Account already exist!")
        else:
            name = input ("Enter account holders name: ")
            balance = float (input ("Enter initial balance: "))
            accounts[account_number] = {"name": name, "balance":balance}
            print (f"Account created successfully for {name}")
    
    def deposit():
        account_number = input ("Enter accout number: ")
        if account_number in accounts:
            amount = float (input ("Enter amount to deposit: "))
            accounts[account_number]["balance"] += amount 
            print (f"Dosited {amount}. New balance is {accounts[account_number]['balance']}")
        else:
            print ("Account not found!")
        
    def withdraw():
        account_number = input ("Enter accout number: ")
        if account_number in accounts:
            amount = float (input ("Enter amount to withdraw: "))
            if amount > accounts[account_number]["balance"]:
                print ("Insufficient balance!")
            else:
                accounts[account_number]["balance"] -= amount 
            print (f"Withdrew {amount}. New balance is {accounts[account_number]['balance']}")
        else:
            print ("Account not found!")
    
    def view_balance():
        account_number = input ("Enter accout number: ")
        if account_number in accounts:
            print (f"Account name {accounts[account_number]['name']}")
            print (f"Balance is {accounts[account_number]['balance']}")
        else:
            print ("Account not found!")
        
    
    
    while True:
        print ("\nBanking Application")
        print ("1. Create Account")
        print ("2. Deposit Money")
        print ("3. Withdraw Money")
        print ("4. View Balance")
        print ("5. Exit")
        
        choice = input ("Enter your choice: ")
        
        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            view_balance()
        elif choice == "5":
            print ("Exit Banking system")
            break
        else:
            print ("Invalid Choice ")

banking_app()
        
