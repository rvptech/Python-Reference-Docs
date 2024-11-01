# Counting Positive Numbers

# Given a list of numbers, count how many are positive.

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positiveCount = 0
for povnum in numbers:
    if (povnum > 0):
        positiveCount += 1
print("final count of Positive Numbers is", positiveCount)
