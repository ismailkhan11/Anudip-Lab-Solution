# Write a Python program to sum all the items in a list.

# Define a function to sum all items in a list
def sum_of_list(items):
    total = 0  # Initialize total to 0
    for item in items:
        total += item  # Add each item to the total
    return total  # Return the final sum

# Example list
my_list = [2, 4, 6, 8, 10]

# Call the function and print the result
print("The sum of the list is:", sum_of_list(my_list))


# Output:

# The sum of the list is: 30
