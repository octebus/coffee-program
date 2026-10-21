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
'''def input_check():
    while True:
        try:
            num = float(input("please enter a number: "))
            break 
        except ValueError:
            print("That is not a valid float number. \n")

    print(f"The number you entered is {num}")

# Main routine
input_check() # This calls the function to be used'''

# V1.3 Valid input checker
# Use parameters in the function
# More Pythonic
'''def input_check(question): # 'question' is a placeholder
    while True:
        error = "That is not a valid number."
        print(question)
        try:
            num = float(input())
            break
        except ValueError:
            print(error)

    return(num) # Gives back the value of num
                # so that I can use it outside of 
                # the function

# Main routine
num1 = input_check("Please enter your first number: ")
print(f"The number you stored is {num1}")

num2 = input_check("Please enter the second number: ")
print(f"The second number you stored is {num2}")

sum = num1 + num2
print(f"Your numbers added together result in {sum}. ")'''

# V1.4. Checking for a valid input using try/except method
# Using parameters (placeholders) to help make the code more pythonic
# Function
def valid_num(question, low, high):
    error = f"Whoops, that is not an integer between {low} and {high}."
    while True:
        try:
            response = int(input(question))
            # if the response >= to the low nr or <= high nr, then continue
            if low <= response <= high:
                break

            else:
                print(f"{error}")

        except ValueError:
            print(error)
    return response # This makes the response available
                    # to be used outside the function

# Main routine
if __name__ =="__main__":

    num1 = valid_num("Enter a number between 1 and 10: ",1,10)
    print(f"The number you entered is {num1}.\n")

    num2 = valid_num("Enter a number between 15 and 20: ", 15, 20)
    print(f"The number you entered is {num2}.\n")

    num3 = valid_num ("Enter a number between 70 and 90: ",70,90)
    print(f"The number you entered is {num3}.\n")

    # Multiply the result of num1, num2, and num3
    multiply = num1 * num2 * num3
    print(f"Your three numbers multiplied together result in {multiply}.")

    # Adding the numbers
    sum = num1 + num2 + num3
    print(f"Your three numbers added together result in {sum}.")
