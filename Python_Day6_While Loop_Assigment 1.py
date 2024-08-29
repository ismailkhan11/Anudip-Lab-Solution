# Write a python program to check whether a number is palindrome or not?

# Get input from the user
number = int(input("Enter a number to check if it is a palindrome: "))

# Store the original number to compare later
original_number = number

# Initialize the reversed number to 0
reversed_number = 0

# Use a while loop to reverse the number
while number > 0:
    # Extract the last digit of the number
    last_digit = number % 10
    
    # Update the reversed number by shifting digits left and adding the last digit
    reversed_number = (reversed_number * 10) + last_digit
    
    # Remove the last digit from the current number
    number = number // 10

# Check if the original number is equal to the reversed number
if original_number == reversed_number:
    print(f"{original_number} is a palindrome.")
else:
    print(f"{original_number} is not a palindrome.")


# Output:

# (Palindrome Output):
# Enter a number to check if it is a palindrome: 121
# 121 is a palindrome.

# (Not Palindrome Output):
# Enter a number to check if it is a palindrome: 231
# 231 is not a palindrome.
