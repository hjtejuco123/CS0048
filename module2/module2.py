# Check for True
# Check for False

#  Non-Zero and Non-Null values are True
#  Zero and Null are False

'''
if condition:
    # block of codes
'''

# num = 5
# if num > 0:
#     print ("Positive Number")
# print ("Continue with program code ...")

'''
if condition:
    #block of codes if the condition is True
else:
    #block of codes if the condition is False
'''
# num = 3
# if num >= 0:
#     print ("Number is positive ")
# else:
#     print ("Number is negative ")

'''
if condition1:
    #block1
elif condition2:
    #block2
elif condition3:
    #block3
else:
    #block4
'''

# num = -1
# if num > 0:
#     print ("positive number ")
# elif num==0:
#     print ("zero")
# else:
#     print ("negative number")

'''
Nested If statements

if condition1:
    if condition2:
        #block of code
    else:
        #block of code
elif conditionX:
    #block of code
else:
    #block of code
'''

num = -1
if num >= 0:
    if num == 0:
        print ("Zero")
    else:
        print ("Positive number")
else:
    print ("Negative number")