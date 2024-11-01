# Prime Number Checker

# Check if a number is prime.

userInput = int(input("Enter a number : \n"))
primeNum = True

if (userInput > 1):
    for num in range(2, userInput):
        if (userInput % num == 0):
            primeNum = False
            break
print(primeNum)
            
