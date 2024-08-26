# Using input() function take one number from the user and using ternary operators check whether the number is even or odd 

# Take input from the user and convert it to an integer
number = int(input("Enter a number: "))

# Check if the number is even or odd using a ternary operator
result = "Even" if number % 2 == 0 else "Odd"

# Print the result
print(f"The number {number} is {result}.")


# Output:

# (Even Number Output):
# Enter a number: 2
# The number 2 is Even.

# (Odd Number Output):
# Enter a number: 3
# The number 3 is Odd.
