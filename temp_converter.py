def celcius_to_Farenheit():
    celcius = float(input("Enter celcius:" ))
    farenheit = (celcius * 1.8) +32
    print(f"The celcius to farenheit conversion of", celcius ," is:", farenheit)

def Farenheit_to_celcius():
    farenheit = float(input("Enter farenheit:" ))
    celcius = (farenheit-32)*(5/9)
    print(f"The celcius to farenheit conversion of", farenheit ," is:", round(celcius,2))
        
while True:
    print("======================")
    print(f"1. Conver Celsius to Farenheit")
    print(f"2. Convert Farenhei to Celcius")
    print(f"3. Exit")
   
    choice = input("Enter your choice:")
    if choice == "1":
        celcius_to_Farenheit()
    elif choice == "2":
        Farenheit_to_celcius()
    elif choice == "3":
        print(f"Thank you for using my program!")
        break
    else:
        print(f"Invalid choice")


    


