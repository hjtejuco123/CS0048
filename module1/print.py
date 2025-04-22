'''
Print statements

'''


#print
# print ("Hello World")

#print multiple items
# name = "Hadji"
# age = 25
# print ("Name: ", name, "Age: ",age) 

#Separator parameter (sep)
#default is space
# print("Python","is","the","best","programming","language")
# print("Python","is","the","best","programming","language", sep="-")
# print (1,2,3, sep=", ")

#End Paramater
# end default \n
# print ("hello World")
# print ("Hello Python")

# print ("Hello", end=" ")
# print ("World", end="!")

# % - formatting (OLD)
# %s -> String
# %f -> float (number of decimal places)
# %d -> int

# name = "Hadji"
# print ("Hello, %s!" % name)

# pi=3.14159
# print(pi)
# print ("Pi %.2f" % pi)

#str.format() method
                                    #0     1
#print ("{} is {} years old".format("Hadji",25))
                                       #0     1
#print ("{1} comes before {0}".format("Zebra","Apple"))

#print("Price: {:.2f}".format(19.995))

#f-String 3.6
# name = "Hadji"
# age = 25
# print (f"{name} is {age} years old")

# import math 
# print (f"pi is approximately {math.pi:.3f}")
