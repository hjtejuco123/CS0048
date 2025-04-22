#if statement (indentation)
# if 5 > 2:
#     print ("Five is greater than two")
#     print ("this is still part of the if block")
# print ("this is outside of the if block")

def greet(name):
    print (f"hello, {name}!")
    if len(name)>5:
        print ("This is a long name")


greet ("Joanss")