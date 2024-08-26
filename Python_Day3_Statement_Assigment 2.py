# Using input function take two number and then swap the number

# Take two numbers as input from the user
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Print the numbers before swapping
print(f"Before swapping: num1 = {num1}, num2 = {num2}")

# Swapping the values of num1 and num2
num1, num2 = num2, num1

# Print the numbers after swapping
print(f"After swapping: num1 = {num1}, num2 = {num2}")


# Output:

# Enter the first number: 4
# Enter the second number: 5
# Before swapping: num1 = 4, num2 = 5
# After swapping: num1 = 5, num2 = 4
