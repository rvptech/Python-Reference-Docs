# Multiplication Table Printer

# Print the multiplication table for a given number up to 10, but skip the fifth iteration.

number = int(input("Enter your number : \n"))

for multinum in range(1,11):
    if (multinum == 5):    
        continue   # here continue ignores the next lines for current iteration and moves to the next iteration
    result = number * multinum
    print(result)