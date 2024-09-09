#  Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

# Function to divide two numbers
def divide_numbers(a, b):
    try:
        # Try to perform the division
        result = a / b
    except ZeroDivisionError:
        # Handle the case where the divisor is zero
        print("Error: Division by zero is not allowed.")
        return None
    else:
        # If no exception, return the result
        return result

# Test the function
numerator = 10
denominator = 0

# Calling the function with a divisor of zero
result = divide_numbers(numerator, denominator)

if result is not None:
    print(f"Result: {result}")


# Output:

# Error: Division by zero is not allowed.
