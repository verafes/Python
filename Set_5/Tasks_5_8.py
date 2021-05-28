# Real code challenges. Set #5-8
# Completed_solutions 5.81-5.90

#  Task 5.81. Thinkful - Number Drills: Congo warehouses
https://www.codewars.com/kata/5862e7c63f8628a126000e18
# Your company, Congo Pizza, is the second-largest online frozen pizza retailer. You own a number of international warehouses that you use to store your frozen pizzas, 
# and you need to figure out how many crates of pizzas you can store at each location.
# Congo recently standardized its storage containers: all pizzas fit inside a cubic crate, 16-inches on a side. 
# The crates are super tough so you can stack them as high as you want.
# Write a function box_capacity() that figures out how many crates you can store in a given warehouse. 
# The function should take three arguments: the length, width, and height of your warehouse (in feet) and should return 
# an integer representing the number of boxes you can store in that space.
# For example: a warehouse 32 feet long, 64 feet wide, and 16 feet high can hold 13,824 boxes because you can fit 24 boxes across, 
# 48 boxes deep, and 12 boxes high, so box_capacity(32, 64, 16) should return 13824.

def box_capacity(length, width, height):
   return int(length * 12//16) * int(width * 12//16) * int(height * 12//16)

# Task 5.82. Is it a palindrome?
https://www.codewars.com/kata/57a1fd2ce298a731b20006a4
# Write function that checks if a given string (case insensitive) is a palindrome.

def is_palindrome(s):
    return s.lower() == s.lower()[::-1]

# Task 5.83. Multiply characters
https://www.codewars.com/kata/52e9aa89b5acdd26d3000127
# Here we have a function that help us spam our hearty laughter. But is not working! I need you to find out why...

#fix this code!
def spam(number):
    return ['hue' for i in range(number+1)]

# fixed code:
def spam(number):
    return "".join(['hue' for i in range(number)])

# Task 5.84. Regex validate PIN code
https://www.codewars.com/kata/55f8a9c06c018a0d6e000132
# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
# If the function is passed a valid PIN string, return true, else return false.
# Examples
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false

def validate_pin(pin):
    return pin.isdigit() and len(pin) in [4,6]

# Task 5.85. validate code with simple regex
https://www.codewars.com/kata/56a25ba95df27b7743000016
# Basic regex tasks. Write a function that takes in a numeric code of any length. 
# The function should check if the code begins with 1, 2, or 3 and return true if so. Return false otherwise.
# You can assume the input will always be a number.

def validate_code(code):
    return str(code).startswith(('1', '2', '3'))

# Task 5.86. Switcheroo
https://www.codewars.com/kata/57f759bb664021a30300007d
# Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice versa). Leave any incidence of c untouched.
# Example:
# 'acb' --> 'bca'
# 'aabacbaa' --> 'bbabcabb'

def switcheroo(s):
    return s.replace("a", "A").replace("b", "a").replace("A", "b")
	
# Task 5.87. FIXME: Replace all dots
https://www.codewars.com/kata/596c6eb85b0f515834000049
# The code provided is supposed replace all the dots . in the specified String str with dashes -
# But it's not working properly.

# Given

import re
def replace_dots(str):
    return re.sub(r".", "-", str)
	
# Solution

def replace_dots(str):
    return str.replace(".", "-")

# Task 5.88. Switcheroo
https://www.codewars.com/kata/57f759bb664021a30300007d
# Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice versa). 
# Leave any incidence of c untouched.
# Example:
# 'acb' --> 'bca'
# 'aabacbaa' --> 'bbabcabb'

def switcheroo(s):
    return s.replace("a", "A").replace("b", "a").replace("A", "b")

# 2nd solution:

def switcheroo(s):
    return "".join([ "a" if el == "b" else "b" if el =="a" else "c" for el in s])
	
# Task 5.89. Initialize my name
 https://www.codewars.com/kata/5768a693a3205e1cc100071f
# Some people just have a first name; some people have first and last names and some people have first, middle and last names.
# You task is to initialize the middle names (if there is any).
# Examples
# 'Jack Ryan'                   => 'Jack Ryan'
# 'Lois Mary Lane'              => 'Lois M. Lane'
# 'Dimitri'                     => 'Dimitri'
# 'Alice Betty Catherine Davis' => 'Alice B. C. Davis'

def initialize_names(name):
    l = name.split()
    for i in range(1, len(l)-1):
        l[i] = l[i][0] + '.'
    return ' '.join(l)

# Task 5.80.Sum The Strings
https://www.codewars.com/kata/5966e33c4e686b508700002d
# Create a function that takes 2 positive integers in form of a string as an input, and outputs the sum (also as a string):
# Example: (Input1, Input2 -->Output)
# "4",  "5" --> "9"
# "34", "5" --> "39"

def sum_str(a, b):
    return str(int('0' + a) + int('0' + b))
	
#
