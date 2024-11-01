# Validate Input

# Keep asking the user for input until they enter a number between 1 and 10.



while True :
    userInput = int(input("Enter a number between 1 and 10 : \n"))
    if (userInput >= 1) and (userInput < 10):
        print("Thanks !")
        break
    else:
        print("Oops! Incorrect number")
        