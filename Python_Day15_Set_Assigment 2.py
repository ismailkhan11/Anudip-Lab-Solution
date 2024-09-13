# Write a Python program to Return a set of elements present in Set A or B, but not both.
# Input: set1 = {10, 20, 30, 40, 50} set2 = {30, 40, 50, 60, 70} 
# Output: {20, 70, 10, 60}

# Define the two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Use symmetric difference to get elements that are in set1 or set2 but not both
unique_items = set1.symmetric_difference(set2)

# Print the unique items
print("Unique items from both sets:", unique_items)


# Output:

# Unique items from both sets: {20, 70, 10, 60}
