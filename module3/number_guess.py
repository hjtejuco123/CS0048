import random 

def number_guess():
    num = random.randint(0,100)
    attemps = 0

    while True:
        print("==========================")
        guess = int(input("Guess the number: "))
        if num == guess:
            print("You are correct!")
            attemps += 1
            print(f"You've guess the number in: ", attemps, "attempt(s)")

            choice = input("Do you want to continue?: ")
            if choice == "Y" or choice == "y":
                continue
            elif choice == "N" or choice == "n":
                break
            else: 
                print("Wrong choice")
        elif guess < num:
            print("You are less than the given num")
            attemps += 1

        elif guess > num:
            print("You are greater than the given num")
            attemps += 1
        else:
           print("Wrong choice")
           break
while True:
    print("======================")
    print(f"a. Play Number Guessing Game")
    print(f"b. Exit")
   
    choice = input("Enter your choice:")
   
    if choice == "a":
      number_guess()
    elif choice == "b":
        print(f"Thank you for using my program!")
        break
    else:
        print(f"Invalid choice")


    


