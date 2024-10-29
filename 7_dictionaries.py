
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