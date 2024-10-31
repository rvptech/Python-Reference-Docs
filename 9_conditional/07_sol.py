# Coffee Customization

# Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

orderSize = input("Enter the size of your coffee : \n")
extraShot = True

if (extraShot == True):
    print("Enjoy your", orderSize, "coffee with an extra shot of espresso")
else:
    print("Enjoy your", orderSize,"coffee")
