# Find the First Non-Repeated Character

# Given a string, find the first non-repeated character.

data = "teeteradads"

for strData in data:
    if (data.count(strData) == 1):
        print(strData, " is the First Non-Repeated Character")
        break   # exits from the loop ignoring the next iterations