# Real code challenges. 
# Set #1. Completed_solutions 31-40

# Task 31. Beginner Series #4 Cockroach
https://www.codewars.com/kata/55fab1ffda3e2e44f00000c6
# The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).
# For example:
# cockroach_speed(1.08) == 30
# Note! The input is a Real number (actual type is language dependent) and is >= 0. The result should be an Integer.

def cockroach_speed(s):
    return int(s * 100000 / 3600)

# Task 32. Discover The Original Price
https://www.codewars.com/kata/552564a82142d701f5001228
# We need to write some code to return the original price of a product, the return type must be of type decimal and the number must be rounded to two decimal places.
# We will be given the sale price (discounted price), and the sale percentage, our job is to figure out the original price.

def discover_original_price(discounted_price, sale_percentage):
    return round(discounted_price / (1 - sale_percentage/100), 2)

# Task 33. Miles per gallon to kilometers per liter
https://www.codewars.com/kata/557b5e0bddf29d861400005d
# Create an application that will display the number of kilometers per liter (output) based on the number of miles per imperial gallon (input).
# Make sure to round off the result to two decimal points. If the answer ends with a 0, it should be rounded off without the 0. So instead of 5.50, we should get 5.5.
# Some useful associations relevant to this kata: 1 Imperial Gallon = 4.54609188 litres 1 Mile = 1.609344 kilometres

def converter(mpg):
    kml = mpg * 1.609344 / 4.54609188
    return round(kml, 2)

# Task 4. 


# Task 5. 


# Task 6. 


# Task 7. 


# Task 8. 


# Task 9. 


# Task 10. 


