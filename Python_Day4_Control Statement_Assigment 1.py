# Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.

# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Check if the number is even
if number % 2 == 0:
    # If the remainder when dividing by 2 is 0, it's even
    print("Even")
else:
    # If the remainder is not 0, it's odd
    print("Odd")


# Output:

# (Even Number Output):
# Enter a number: 4
# Even

# (Odd Number Output):
# Enter a number: 5
# Odd
