# Write a Python program to Count all letters, digits, and special symbols from the given string

# Input = “P@#yn26at^&i5ve” Output: Chars = 8 Digits = 3 Symbol = 4 

# Define the input string
input_string = "P@#yn26at^&i5ve"

# Initialize counters for letters, digits, and symbols
letters_count = 0
digits_count = 0
symbols_count = 0

# Iterate through each character in the input string
for char in input_string:
    if char.isalpha():  # Check if the character is a letter
        letters_count += 1
    elif char.isdigit():  # Check if the character is a digit
        digits_count += 1
    else:  # If it's neither a letter nor a digit, it's a symbol
        symbols_count += 1

# Print the results
print("Chars =", letters_count)
print("Digits =", digits_count)
print("Symbols =", symbols_count)


# Output:

# Chars = 8
# Digits = 3
# Symbols = 4
