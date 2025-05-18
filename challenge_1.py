# Start by importing additional math functions
import math 

# Ask the uder to enter the lengths of all three sides of a traingle
print("You will be asked to enter the lengths of all three sides of a triangle denoated as a, b and c below")
a = int(input("Length of a: "))
b = int(input("Length of b: "))
c = int(input("Length of c: "))

# Calculate the area of this triangle
# Using the formula provided
s = (a+b+c)/2
print(s)
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(f"The area of the triangle is {area}")