
#SETS 
#unique 
#registration system 


def registration_system():
    #set 
    registered_users = set() #set 
    
    
    def register_user():
        username = input ("Enter username: ")
        if username in registered_users:
            print ("Username already exist ")
        else:
            password = input ("Enter your password: ")
            registered_users.add(username)
            print(f"User {username} registered successfully ")
    
    
    def view_user(): 
        if registered_users:
            print ("Registered users")
            for user in registered_users:
                print(user)
        else:
            print ("No Users Registered yet!") 
    
    def check_username():
        username = input ("Enter username to check: ")
        if username in registered_users:
            print ("Username is already taken ")
        else:
            print ("Username is available")

        
    while True:
        print ("\nRegistration System")
        print ("1. Register User")
        print ("2. View Registered User")
        print ("3. Check Username availabilty")
        print ("4. Exit")
        choice = input ("Enter your choice: ")
        
        if choice == "1":
            register_user()
        elif choice == "2":
            view_user()
        elif choice == "3":
            check_username()
        elif choice == "4":
            print ("Exit System")
            break
        else:
            print ("Invalid Choice ")

registration_system()
