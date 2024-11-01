# Reverse a String

# Reverse a string using a loop.

data = input("Enter your string : \n")
revData = ""

for char in data:
    revData = char + revData
print(revData)