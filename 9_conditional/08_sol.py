# Password Strength Checker

# Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

passData = input("Enter Your desired password : \n")

if (len(passData)<6):
    print("Your Password Strength is Weak")
elif (len(passData)>=6) and (len(passData)<=10):
    print("Your Password Strength is Medium")
elif (len(passData)>10):
    print("Your Password Strength is Strong")