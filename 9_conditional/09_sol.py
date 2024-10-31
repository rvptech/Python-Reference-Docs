# Leap Year Checker

# Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

yearData = int(input("Enter the year : \n"))

if (yearData % 400 == 0) or (yearData % 4 == 0) and (yearData % 100 != 0):
    print(yearData, " is a leap year")
else:
    print(yearData, " is not a leap year")