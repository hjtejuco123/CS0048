#User Input

# name = input("Enter your name ")
# print (f"Hello, {name}!")

#convert str into int

# age = int(input ("Enter you age "))
# print (f"Next you will be  {age+1} years old.")

#multiple inputs

# x,y = input("Enter two numbers separated by space ").split()
# print (f"Sum {int(x) + int(y)}")


#menu selection
#\n = new line

# print ("1. Option A \n2. Option B\n3. Option C")
# choice = input("Select option from 1-3: ")
# if choice == '1':
#     print ("You have selected A")
# elif choice == '2':
#     print ("You have selected B")
# elif choice == '3':
#     print ("You have selected C")
# else:
#     print ("invalid choice")



#Identity operators

# a = [1,2,3]
# b =  a
# c = [1,2,3]

# print (a is b) #same object
# print (a is c) #different object
# print (a==c) #values are the same
# print (a is not c)  #different object a and c 
               #8421
a = 5 #Binary  0101
b = 3 #Binary  0011


print ("AND: ", a & b) #0001 = 1
print ("OR: ",a | b) #0111 = 7
print ("XOR: ",a^b) #0110 = 6
print ("NOT: ",~a) #twos complement 1010 -6
print ("a << 1",a<<1) #1010 
print ("a >> 1",a>>1) #0010

