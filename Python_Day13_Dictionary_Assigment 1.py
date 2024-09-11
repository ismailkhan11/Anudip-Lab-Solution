# Write a Python program and calculate the mean of the below dictionary.
# test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4} 
# Output: 6.2

# Define the dictionary with values
test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}

# Extract all the values from the dictionary
values = test_dict.values()

# Calculate the total sum of all values
total_sum = sum(values)

# Calculate the number of elements (values) in the dictionary
num_elements = len(values)

# Calculate the mean by dividing the total sum by the number of elements
mean = total_sum / num_elements

# Print the mean
print("The mean of the dictionary values is:", mean)


# Output:

# The mean of the dictionary values is: 6.2
