# Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

# Function to prompt user for an integer input
def get_integer_input():
    while True:
        try:
            # Prompt the user to input a value
            user_input = input("Please enter an integer: ")
            
            # Try to convert the input to an integer
            user_input = int(user_input)
            
            # If conversion is successful, return the integer
            return user_input
            
        except ValueError:
            # Handle the case where input is not a valid integer
            print("Error: That's not a valid integer. Please try again.")

# Call the function and store the result
user_number = get_integer_input()

# Output the valid integer entered by the user
print(f"You entered the integer: {user_number}")


# Output:

# (If it is a Integer Output):
# Please enter an integer: 2
# You entered the integer: 2

# (If it is not Integer Output):
# Please enter an integer: ab
# Error: That's not a valid integer. Please try again.
