# Write a python program finding the factorial of a given number using a while loop.

# Get input from the user
number = int(input("Enter a number to find its factorial: "))

# Initialize the factorial to 1 (since the factorial of 0 is 1)
factorial = 1

# Initialize a counter variable to the input number
counter = number

# Use a while loop to calculate the factorial
while counter > 0:
    # Multiply the current factorial by the counter
    factorial *= counter
    
    # Decrease the counter by 1
    counter -= 1

# Print the calculated factorial
print(f"The factorial of {number} is: {factorial}")


# Output:

# Enter a number to find its factorial: 5
# The factorial of 5 is: 120
