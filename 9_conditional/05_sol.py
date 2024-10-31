# Weather Activity Suggestion

# Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

weaData = input("Enter your weather name : ")

if (weaData == "sunny"):
    print("Go for a walk")
elif (weaData == "rainy"):
    print("Read a book")
elif (weaData == "snowy"):
    print("Build a snowman")
else:
    print("Oops, invalid weather")
   