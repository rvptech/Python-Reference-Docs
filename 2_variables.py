
# Variables are containers for storing data values.

data = 10
print(data) # here data is the variable name [always give meaningful variable names]


a = b = c = 10
print(a+b+c)


a,b,c = 1,2,3
print(a,b,c)


del a   # here the variable a is deleted
print(c)



# User Input :

myData = input("Enter your name")
print(myData)
print(type(myData))


# Format Function

# Direct Formating :

f_name = input("Enter your First Name")
l_name = input ("Enter your Last Name")

print("Welcome {} {} to our World !".format(f_name, l_name))


# Casting:

# If you want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# NOTE : Variable names are case-sensitive.