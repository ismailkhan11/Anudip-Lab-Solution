# Python program to find the area of a triangle whose sides are given 

# Lengths of the sides of the triangle
a = 5
b = 6
c = 7

# Calculate the semi-perimeter
s = (a + b + c) / 2

# Calculate the area using Heron's formula
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

# Print the area of the triangle, formatted to 2 decimal places
print('The area of the triangle is %0.2f' % area)

# Output:

# The area of the triangle is 14.70
