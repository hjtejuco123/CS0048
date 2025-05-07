
'''
#syntax

def function_name(parameters):
    """ doc string """
    #function body
    return 
'''
# def greet(name):
#     """Function greets the person and name as the parameter"""
#     print ("Hello "+name+". Good morning ")

# greet("Hadji")

# def display_hello():
#     """
#         documentation
#         this display the hello message
    
#     """
#     print ("This display the hello message")

# #display_hello()
# print (display_hello.__doc__)

#Function Arguments
#positional Arguments

# def greet (name, message):
#     print (message,name)

# greet("Hadji","Hello")

#default Arguments

# def greet(name,message="Hi"):
#     print (message,name)

# greet("Hadji")
# greet("James","Hi there...")

#arbitrary arguments (number of arguments (*args))

# def greet(*names):
#     for name in names:
#         print ("Hello", name)

# greet("Aida","Lorna","Fe")

#return statement

# def add(a,b):
#     return a+b
    
# result = add(3,5)
# print (result)
# print (add(10,5))


#scope of variables
#local variables - var is inside a function- access it within the function 
#global variable - var define outside of a function, accessible anywhere

# x = 10  #global var 
# def abc():
#     y = 15
#     print ("Values of variables ", x,y)

# abc()
# print ("Outide of the function code ")

#modify the global variable 
# counter = 0 

# def increase_counter():
#     global counter 
    
#     counter += 1 
#     print (f"Inside the function, counter = {counter}")

# print (f"Before calling the function, counter = {counter}")
# increase_counter()
# print (f"After callilng the function, counter = {counter}")

    
#global varible access to multiple functions 
#global var 
# balance = 1000

# def deposit(amount):
#     global balance 
#     balance += amount 
#     print (f"After deposit, New balance is {balance}")

# def withdraw(amount):
#     global balance
#     if amount <= balance:
#         balance -= amount 
#         print (f"After withdraw, New balance is {balance}")
#     else:
#         print ("Inssuficient balance ")

# print (f"Initial Balance is {balance}")
# deposit(500)
# withdraw(200)
# withdraw(2000)
# print (f"current Balance is {balance}")



# #lambda functions
# double = lambda x: x*2

# print(double(5))

# def double(x):
#     return x * 2

# print(double(5))

# add = lambda x, y: x+y
# print(add(5,10))


Lambda functions, also known as anonymous functions, are small, one-time-use functions in Python.

lambda keyword followed by the function's inputs, a colon, and the function's expression. The output of a lambda function is returned as the result of the expression, rather than a return statement.

One of the main limitations is that lambda functions are limited to a single expression, meaning that they cannot contain multiple statements or complex control flow.

Syntax for creating lambda functions
	lambda arguments: expression

def greet(name):
    return "Hello " + name
print(greet("John")) 

# Output: "Hello John"

greet = lambda name: "Hello " + name
print(greet("John")) 

# Output: "Hello John"

# Document lambda functions for better code readability

# This lambda function returns the square of its input
square = lambda x: x * x
print(square(5)) 

# Output: 25

Use descriptive variable names in lambda functions
# This lambda function returns the sum of its inputs
sum = lambda x, y: x + y
print(sum(5, 10)) 

# Output: 15

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) 
# Output: [2, 4]

lambda functions to return functions as values

def make_adder(x):
    return lambda y: x + y
add5 = make_adder(5)
print(add5(3)) 

# Output: 8


Avoid complex expressions and statements in lambda functions

calculate = lambda x, y: x + y if x > y else x - y
print(calculate(5, 10)) 

# Output: -5

def calculate(x, y):
    if x > y:
        return x + y
    else:
        return x - y

print(calculate(5, 10)) 

# Output: -5

# shapes.py
import math
def find_area_of_circle(radius):
    return math.pi * radius ** 2
def find_area_of_rectangle(width, height):
    return width * height
def main():
    shape = int(input("Enter 1 for circle, 2 for rectangle: "))
    if shape == 1:
        radius = int(input("Enter radius: "))
        print(f"The area of the circle is {find_area_of_circle(radius)}")
    elif shape == 2:
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
        print(f"The area of the rectangle is {find_area_of_rectangle(width, height)}")
       
if __name__ == "__main__":
    main()

----------------------

# more_shapes.py
import shapes
radius = 4
print(f"The area of the rectangle is defined in 'more_shapes.py' is: "
      f"{shapes.find_area_of_circle(radius)}")

----------------------
# more_shapes3.py
import shapes
width = 5
height = 5
print(f"The area of the circle defined in 'more_shapes3.py' is: "
      f"{shapes.find_area_of_rectangle(width, height)}")



    
    
    
    
    
    
    
    















































