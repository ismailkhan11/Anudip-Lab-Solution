# 2. Write a Python program to remove a newline in Python

# String = "\nBest \nDeeptech \nPython \nTraining\n"

# Given string with newline characters
string = "\nBest \nDeeptech \nPython \nTraining\n"

# Remove all newline characters
cleaned_string = string.replace('\n', '')

# Print the original and cleaned strings
print("Original String:")
print(string)  # This will include newlines

print("Cleaned String:")
print(cleaned_string)  # Newlines are removed


# Output:

# Original String:

# Best 
# Deeptech 
# Python 
# Training

# Cleaned String:
# Best Deeptech Python Training
