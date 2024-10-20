
myName = "Rohith"
print(myName)


# Concatination

myData1 = "Hello "
myData2 = "World"

print(myData1 + myData2)


# Indexing in Strings

myData = "This is my Own World"

print(myData[0])  # left to right goes from to 0 till the end

print(myData[-1])  # right to left goes from to -1 till the beginning

print(len(myData))  # returns the length of the string

newData = myName[0:3]  #slicing
print(newData)

newData = myName[0:4:2]  # here its [start:end:hop]
print(newData)

print(len(myName)) # returns length of the string

# string methods :

myData = "Lemon Chai"

print(myData.upper())  # all characters UpperCase
print(myData.lower())  # all characters LowerCase

print(myData.replace("Lemon","Ginger"))  # replace a word "Lemon" with "Ginger"

# Conversion of string into list

items = "Lemon, Mint, Ginger, Masala"

cartData = items.split(", ")
print(cartData)

print(type(cartData))