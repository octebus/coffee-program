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
'''done = True
while done:
    try: # This method tries for a valid input
        num = float(input("Please enter a number: "))
        done = True

    except ValueError:
        print("That is not a valid float number. \n")

    print(f"The number you entered is {num}")'''

# Check for valid input and recycling code with a function (V1.2)
# Create a function to call every time I ask the user
# for a number. A function is a chunk of code that does 
# something.
# Functions can be used over and over again.
# To use a function (call it), write out its name with
# parenthesis at the end.
# To create a function, start with the word def
def input_check():
    while True:
        try:
            num = float(input("please enter a number: "))
            break 
        except ValueError:
            print("That is not a valid float number. \n")

    print(f"The number you entered is {num}")

# Main routine
input_check() # This calls the function to be used