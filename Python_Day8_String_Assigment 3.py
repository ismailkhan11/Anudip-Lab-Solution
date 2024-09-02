# 3. Write a Python program to reverse words in a string 

# String = “Deeptech Python Training”

# Given string
string = "Deeptech Python Training"

# Step 1: Split the string into a list of words
words = string.split()

# Step 2: Reverse the list of words
reversed_words = words[::-1]  # Using slicing to reverse the list

# Step 3: Join the reversed list into a single string
reversed_string = " ".join(reversed_words)

# Print the original and reversed strings
print("Original String: ")
print(string)

print("\nReversed String:")
print(reversed_string)

# Output:

# Original String:
# Deeptech Python Training

# Reversed String:
# Training Python Deeptech
