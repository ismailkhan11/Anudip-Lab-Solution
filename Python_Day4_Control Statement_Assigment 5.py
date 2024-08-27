# Write a Python program that determines the largest of three numbers entered by the user.

# Prompt the user to enter three numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

# Check if the first number is the largest
if number1 >= number2 and number1 >= number3:
    print(f"The largest number is {number1}.")
# Check if the second number is the largest
elif number2 >= number1 and number2 >= number3:
    print(f"The largest number is {number2}.")
# If the above two conditions are not true, the third number is the largest
else:
    print(f"The largest number is {number3}.")


# Output:
# Enter the first number: 3
# Enter the second number: 6
# Enter the third number: 8
# The largest number is 8.0.
