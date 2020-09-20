# Real code challenges. 
# Set #1. Completed_solutions 1-10

# Task 1. Multiply
https://www.codewars.com/kata/50654ddff44f800200000004
# This code does not execute properly. Try to figure out why.

def multiply(a, b):
	#Need to add return statement
	return a * b

# Task 2. Even or Odd
https://www.codewars.com/kata/53da3dbb4a5168369a0000fe

# Create a function (or write a script in Shell) that takes an integer as an argument 
# and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Task 3. Function 1 - hello world
https://www.codewars.com/kata/523b4ff7adca849afe000035

# Write a function `greet` that returns "hello world!"

def greet():
    return "hello world!"

# Task 4. Century From Year
https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097

# The first century spans from the year 1 up to and including the year 100, The second - from the year 101 up to and including the year 200, etc.

# Task : Given a year, return the century it is in.

# Input, Output Examples :
# centuryFromYear(1705)  returns (18)
# centuryFromYear(1900)  returns (19)
# centuryFromYear(1601)  returns (17)
# centuryFromYear(2000)  returns (20)

# Task 5. Return the closest number multiple of 10
https://www.codewars.com/kata/58249d08b81f70a2fc0001a4
# Given a number return the closest number to it that is divisible by 10.
# Example input:
# 22
# 25
# 37
# Expected output:
# 20
# 30
# 40

def closest_multiple_10(i):
    return round(i / 10) * 10
	
# Task # 6.Formatting decimal places #0
https://www.codewars.com/kata/5641a03210e973055a00000d

# Each number should be formatted that it is rounded to two decimal places. You don't need to check whether the input is a valid number because only valid numbers are used in the tests.
# Example:    
# 5.5589 is rounded 5.56   
# 3.3424 is rounded 3.34

def two_decimal_places(n):
    return round(n, 2)
	
# Task 7. Area of an arrow 
https://www.codewars.com/kata/589478160c0f8a40870000bc

# Complete the function that calculates the area of the red square, 
# when the length of the circular arc A is given as the input. 
# Return the result rounded to two decimals.
# Note: use the π value provided in your language (Math::PI, M_PI, math.pi, etc)

def square_area(A):
    from math import pi
    r = (A*4)/(2*pi)
    area = r**2
    return (round(area, 2))

# Task 8. Beginner Series #2 Clock
https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a

# Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.
# Your task is to make 'Past' function which returns time converted to milliseconds.

# Example:
# past(0, 1, 1) == 61000
# Input constraints: 0 <= h <= 23, 0 <= m <= 59, 0 <= s <= 59

h = int(input("Enter h: "))
m = int(input("Enter m: "))
s = int(input("Enter s: "))
def past(h,m,s):
  if 0 <= h <= 23 and  0 <= m <= 59 and 0 <= s <= 59:
    return (h * 3600000 + m * 60000 + s * 1000)
  else: 
    return 0
print(f"Given '{h}' hours, '{m}' minutes and 'S' seconds after midnight")  
print("Total milliseconds = ", past(h,m,s))

# Task 9. Opposite number
https://www.codewars.com/kata/56dec885c54a926dcd001095
# Very simple, given a number, find its opposite. 
# Examples: 1: -1, -34: 34
# Examples: 1: -1, -34: 34

def opposite(number): 
	return -number

# Task 10. Returning Strings
https://www.codewars.com/kata/55a70521798b14d4750000a4/train/python 
# Make a function that will return a greeting statement that uses an input; 
# your program should return, "Hello, <name> how are you doing today?".
# [Make sure you type the exact thing I wrote or the program may not execute properly]

def greet(name):
    return f"Hello, {name} how are you doing today?"
	
#
