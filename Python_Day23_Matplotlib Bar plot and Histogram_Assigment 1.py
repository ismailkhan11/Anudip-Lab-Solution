# Create a bar chart to represent monthly expenses in different spending categories and give your conclusion. 
# Input: categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation'] 
# Monthly expenses in dollars (replace with your own data) 
# expenses = [1200, 400, 200, 150, 250]

# Import necessary libraries
import matplotlib.pyplot as plt

# Categories for expenses
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']

# Monthly expenses in dollars
expenses = [1200, 400, 200, 150, 250]

# Create a bar chart
plt.figure(figsize=(8,6))  # Set the figure size for better visibility
plt.bar(categories, expenses, color='skyblue')  # Plot the bar chart with specified color

# Add labels and title
plt.xlabel('Spending Categories')  # X-axis label
plt.ylabel('Monthly Expenses (in $)')  # Y-axis label
plt.title('Monthly Expenses by Category')  # Title of the chart

# Show the plot
plt.show()

# Conclusion: Rent is the largest expense, accounting for a significant portion of the monthly expenses.
# Groceries and Transportation follow, while Utilities and Entertainment have smaller portions of the monthly budget.
