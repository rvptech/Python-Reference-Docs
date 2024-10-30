
myData = {
    "name":"alex",
    "age":27,
    "gender":"male"
}

print(myData["name"]) # access the value in the dictionary, using the key.

print(myData.get("age")) # alternate method to access data from the dictionary


myData["age"] = 40  # you can also change the value of each data inside the dictionary
print(myData)

print(len(myData)) # returns the no of items in the dictionary


for keyData in myData:   #  here you can obtain all "keys" inside a dictionary
    print(keyData)
    
for valData in myData:   #  here you can obtain all "values" inside a dictionary
    print(myData[valData])
    
# NOTE: "key":"value", paired together is called as Item in dictionary.

for keyData, valData in myData.items(): # alternate method wherein you can access "key" as well as "value" in single line.
    print(keyData, valData, sep=": ")
    
myData["Education"]="MBA" # adds a new item (key:value pair) to the dictionary
print(myData)

myData.pop("age") # pops out the item, based on the key provided
print(myData)

del myData["name"] # deletes a specific item from dictionary
print(myData)

newData = myData.copy() # copy of the dict is created and associated to a new variable. Most commonly used to seperate the memory ref of both the dict.
print(newData)

# Nested Dictionary:

myData2 = {
    "user1" : {
        "name":"Alex",
        "age":25,
        "gender":"male"
    },
    "user2" : {
        "name":"Nitin",
        "age":42, 
        "gender":"male"
    },
    "user3" : {
        "name":"Mohan",
        "age":38,
        "gender":"male"
    }
}

print(myData2["user2"]["name"])

# Example (exceptional)
sqdnum = {x:x**2 for x in range(0,10)}
print(sqdnum)


# Constructing a new dictionary from list

chai = ["lemon", "ginger", "green"]
defaultVal = "delicious"

myDict = dict.fromkeys(chai, defaultVal)
print(myDict)