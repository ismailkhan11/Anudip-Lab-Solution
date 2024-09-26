# Install matplotlib  & you can use plt.plot() to create a line plot of given data
# x = [0, 5, 9, 10, 15, 20, 25] 
# y = [0, 1, 2, 3, 4, 5, 6]



# Importing the necessary library
import matplotlib.pyplot as plt

# Defining data points for the x-axis and y-axis
x = [0, 5, 9, 10, 15, 20, 25]
y = [0, 1, 2, 3, 4, 5, 6]

# Creating the plot with markers
# 'o' is the marker, linestyle '-' makes it a line plot
plt.plot(x, y, marker='o', linestyle='-', color='b')

# Adding labels for the x-axis and y-axis
plt.xlabel('X values')
plt.ylabel('Y values')

# Adding a title to the plot
plt.title('Line Plot with Markers')

# Display the plot
plt.show()
