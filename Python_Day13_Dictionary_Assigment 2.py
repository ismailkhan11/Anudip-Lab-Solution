# Write a Python script to concatenate the following dictionaries to create a new one. 
# Sample Dictionary : dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60} 
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Define the sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Create a new dictionary by concatenating all three dictionaries
# The update() method adds the key-value pairs from each dictionary to the new dictionary
result = {}
result.update(dic1)
result.update(dic2)
result.update(dic3)

# Print the concatenated dictionary
print("Concatenated dictionary:", result)


# Output:

# Concatenated dictionary: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
