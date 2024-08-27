# Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.

# Prompt the user to enter their age
age = int(input("Please enter your age: "))

# Check if the person is eligible to vote
if age >= 18:
    # If age is 18 or more, the person is eligible to vote
    print("You are eligible to vote.")
else:
    # If age is less than 18, the person is not eligible to vote
    print("You are not eligible to vote yet.")


# Output:

# (Eligible Output):
# Please enter your age: 19
# You are eligible to vote.

# (Not Eligible Output):
# Please enter your age: 16
# You are not eligible to vote yet.

