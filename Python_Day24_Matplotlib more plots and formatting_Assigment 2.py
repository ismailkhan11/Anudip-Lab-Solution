# Suppose you're a sales manager for an e-commerce company, and you want to create a figure with subplots to compare the sales performance of different product categories over time. You have sales data for four product categories: Electronics, Clothing, Home & Garden, and Sports & Outdoors. Share your conclusion/analysis.
# Input: months = np.arange(1, 13) 
# electronics_sales = np.array([25000, 28000, 31000, 27000, 30000, 32000, 35000, 36000, 38000, 39000, 41000, 42000]) 
# clothing_sales = np.array([15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000]) 
# home_garden_sales = np.array([18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000])
# sports_outdoors_sales = np.array([12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000])

# Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Data: months (1 to 12, representing each month of the year)
months = np.arange(1, 13)

# Sales data for each product category
electronics_sales = np.array([25000, 28000, 31000, 27000, 30000, 32000, 35000, 36000, 38000, 39000, 41000, 42000])
clothing_sales = np.array([15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000])
home_garden_sales = np.array([18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000])
sports_outdoors_sales = np.array([12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000])

# Create a figure with subplots (2 rows, 2 columns)
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# First subplot: Electronics Sales
axs[0, 0].plot(months, electronics_sales, marker='o', color='blue', label='Electronics')
axs[0, 0].set_title('Electronics Sales')
axs[0, 0].set_xlabel('Months')
axs[0, 0].set_ylabel('Sales')
axs[0, 0].legend()

# Second subplot: Clothing Sales
axs[0, 1].plot(months, clothing_sales, marker='o', color='green', label='Clothing')
axs[0, 1].set_title('Clothing Sales')
axs[0, 1].set_xlabel('Months')
axs[0, 1].set_ylabel('Sales')
axs[0, 1].legend()

# Third subplot: Home & Garden Sales
axs[1, 0].plot(months, home_garden_sales, marker='o', color='red', label='Home & Garden')
axs[1, 0].set_title('Home & Garden Sales')
axs[1, 0].set_xlabel('Months')
axs[1, 0].set_ylabel('Sales')
axs[1, 0].legend()

# Fourth subplot: Sports & Outdoors Sales
axs[1, 1].plot(months, sports_outdoors_sales, marker='o', color='purple', label='Sports & Outdoors')
axs[1, 1].set_title('Sports & Outdoors Sales')
axs[1, 1].set_xlabel('Months')
axs[1, 1].set_ylabel('Sales')
axs[1, 1].legend()

# Adjust layout for better spacing between plots
plt.tight_layout()

# Show the plot
plt.show()


# Conclusion/Analysis:
# Electronics: The sales in the electronics category exhibit consistent growth throughout the year, with significant increases in the last quarter.
# Clothing: The clothing category also shows steady growth, though at a slower rate compared to electronics.
# Home & Garden: Sales in the home & garden category grow consistently, mirroring the trend in clothing but at a higher starting point.
# Sports & Outdoors: Sales in the sports & outdoors category show steady but moderate growth, with the lowest overall sales among the four categories.
