def add_num():
    a = input("Enter first number:" )
    b = input("Enter second number:" )
    sum = int(a)+int(b)
    print(f"The sum is:",sum)
    return sum

def subtract_num():
    a = input("Enter first number:" )
    b = input("Enter second number:" )
    diff = int(a)-int(b)
    if a < b:
        print("Error: second number cant be greater than the first!")
    else:
        print(f"The difference is:",diff)
        return diff

def multiply_num():
    a = input("Enter first number:" )
    b = input("Enter second number:" )
    multiply = int(a)*int(b)
    if multiply == 0:
        print("Note when a zero is multiplied to a non-zero number, the answer will always be zero")
    else:
        print(f"The multiplication ot two num is:",multiply)
        return multiply

def divide_num():
    a = input("Enter first number:" )
    b = input("Enter second number:" )
    divide = float(a)/float(b)

    if divide == 0:
        print("Invalid division. Answer cant be zero")
    else:
        print(f"The division ot two num is: {divide:.1f}")
        return divide
    
while True:
    print("======================")
    print(f"1. Add")
    print(f"2. Subtract")
    print(f"3. Multiply")
    print(f"4. Divide")
    print(f"5. Exit")
    choice = input("Enter your choice:")
    if choice == "1":
        add_num()
    elif choice == "2":
        subtract_num()
    
    elif choice == "3":
        multiply_num()
    elif choice == "4":
        divide_num()
    elif choice == "5":
        print(f"Thank you for using my program!")
        break
    else:
        print(f"Invalid number")


    


