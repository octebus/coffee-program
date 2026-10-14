# Error checking
# Caleb Cristobal
# 25 September 2026

# Code that tests whether a valid input was give (v1)
'''done = True # Boolean variable set to True  
while True:
    num = int(input("Please enter your value as an integer: "))
    done = False

print(f"The number you entered is {num}")'''

# Using a try and except method to check for valid input (v1.1)
# Use try and except method to catch errors
done = True
while done:
    try: # This method tries for a valid input
        num = float(input("Please enter a number: "))
        done = True

    except ValueError:
        print("That is not a valid float number. \n")

    print(f"The number you entered is {num}")