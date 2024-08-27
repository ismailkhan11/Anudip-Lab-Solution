# Write a Python program that determines if a given year is a leap year or not.

# Prompt the user to enter a year
year = int(input("Enter a year: "))

# Check if the year is a leap year
if year % 400 == 0:
    # If the year is divisible by 400, it is a leap year
    print(f"{year} is a leap year.")
elif year % 100 == 0:
    # If the year is divisible by 100 but not by 400, it is not a leap year
    print(f"{year} is not a leap year.")
elif year % 4 == 0:
    # If the year is divisible by 4 but not by 100, it is a leap year
    print(f"{year} is a leap year.")
else:
    # If the year is not divisible by 4, it is not a leap year
    print(f"{year} is not a leap year.")


# Output:

# (Leap Year Output):
# Enter a year: 2024
# 2024 is a leap year.

# (Not a Leap Year Output):
# Enter a year: 2022
# 2022 is not a leap year.

