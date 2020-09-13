# Real code challenges. Completed_solutions

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

# Task 9. Count Odd Numbers below n
https://www.codewars.com/kata/59342039eb450e39970000a6/python

# Given a number n, return the number of positive odd numbers below n, EASY!

# oddCount(7) //=> 3, i.e [1, 3, 5] 
# oddCount(15) //=> 7, i.e [1, 3, 5, 7, 9, 11, 13]

def odd_count(n):
    if n < 1:
        return 0
    else:
        return n // 2

n = int(input("Enter n: "))
print(oddCount(n))

def century(year):
    if year %  100 == 0:
        return year / 100
    else:
        return year // 100 + 1
		
# Task 10. Expressions Matter
https://www.codewars.com/kata/5ae62fcf252e66d44d00008e

# Given three integers a ,b ,c, return the largest number obtained after inserting 
# the following operators and brackets: +, *, () 
# In other words , try every combination of a,b,c with [*+()], 
# and return the Maximum Obtained

# !!! Notes
# The numbers are always positive. 
# The numbers are in the range (1 ≤ a, b, c ≤ 10).
# You can use the same operation more than once.
# It's not necessary to place all the signs and brackets.
# Repetition in numbers may occur.
# You cannot swap the operands. For instance, 
# in the given example you cannot get expression (1 + 3) * 2 = 8.

def expressionsMatter(a,b,c):
  # for i in range(1,10):
    if a <= 0 or b<= 0 or c <= 0:
      return ("Error. Value of a, b, c should be greater than zero")
    else:
      n1 = a * (b + c) 
      n2 = a * b * c
      n3 = a + b * c
      n4 = (a + b) * c
      n5 = a + b + c
      n6 = a * b + c
    return(max(n1, n2, n3, n4, n5, n6))
	
a = int(input("Enter integer for a: "))
b = int(input("Enter integer for c: "))
c = int(input("Enter integer for c: "))

print(expressionsMatter(a,b,c))


	

