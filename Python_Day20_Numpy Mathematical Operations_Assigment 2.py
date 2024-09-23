# Calculate the profit made by a company
# Input: revenue = np.array([10000, 12000, 11000, 10500]) 
# expenses = np.array([4000, 5000, 4500, 4800])
# Output: Profit: [6000 7000 6500 5700]

# Importing the NumPy library
import numpy as np

# Revenue of the company for each period
revenue = np.array([10000, 12000, 11000, 10500])

# Expenses of the company for each period
expenses = np.array([4000, 5000, 4500, 4800])

# Calculating the profit by subtracting expenses from revenue
profit = revenue - expenses

# Display the calculated profit
print("Profit:", profit)


# Output:

# Profit: [6000 7000 6500 5700]

