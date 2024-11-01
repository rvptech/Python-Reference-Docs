# Sum of Even Numbers

# Calculate the sum of even numbers up to a given number n.

number = int(input("Enter your number : \n"))
sumData = 0
for numData in range(0,number+1):
    if (numData % 2 == 0):
        sumData += numData
print("the sum of even numbers up to ",number," is", sumData)
 