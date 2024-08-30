# Python program to check if a given number is an Armstrong number.

def is_armstrong_number(number):
    # Store the original number to compare later
    original_number = number
    
    # Convert the number to a string to easily iterate through digits
    num_str = str(number)
    
    # Calculate the number of digits in the number
    num_digits = len(num_str)
    
    # Initialize a variable to store the sum of powers
    sum_of_powers = 0
    
    # Iterate over each digit in the number
    for digit in num_str:
        # Convert the digit to an integer
        digit = int(digit)
        # Add the digit raised to the power of num_digits to the sum
        sum_of_powers += digit ** num_digits
    
    # Check if the sum of powers is equal to the original number
    return sum_of_powers == original_number

# Main part of the program
if __name__ == "__main__":
    # Input number from the user
    input_number = int(input("Enter a number to check if it's an Armstrong number: "))
    
    # Check if the input number is an Armstrong number
    if is_armstrong_number(input_number):
        print(f"{input_number} is an Armstrong number.")
    else:
        print(f"{input_number} is not an Armstrong number.")



# Output:

# (Number is Armstrong Output):
# Enter a number to check if it's an Armstrong number: 153
# 153 is an Armstrong number.

# (Number is Not Armstrong Output):
# Enter a number to check if it's an Armstrong number: 213
# 213 is not an Armstrong number.
