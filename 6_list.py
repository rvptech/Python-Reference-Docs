
teaItems = ["Black", "Green", "White"]

print(teaItems[0]) # slicing works in lists in the same way as strings

teaItems[1] = "Herbal"
print(teaItems)   # replace items in a list using direct index value


teaItems[1:2] = ["Lemon"]
print(teaItems)  # alternate way to replace items in a list, using slicing method

for teaData in teaItems:
    print(teaData)      # loops over every items in the list

for teaData in teaItems:
    print(teaData, end="-") # by default, after every loop the the item name prints in a new line. Hence, here we change it using "end" and end our each item name with a "-", rather than "\n".


if "Green" in teaItems:
    print("we have it")  # conditional statements in lists
    

# List Methods:

teaItems = ["Black", "Green", "White"]

teaItems.append("Oolong")  # appends a new item at the end of the list
print(teaItems)


popIteam = teaItems.pop() # pops out the last item from the list
print(teaItems)
print(popIteam)

teaItems.remove("Green") # removes specific item from the list
print(teaItems)

teaItems.insert(2, "Masala") # (index_val, your value) used to insert an item into specific index value
print(teaItems)


newTeaData = teaItems.copy() # copy of the list is created and associated to a new variable. Most commonly used to seperate the memory ref of both the lists.
print(newTeaData)


print(teaItems.count("Black")) # returns the count of items in the list