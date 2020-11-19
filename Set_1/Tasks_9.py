# Real code challenges. Set #1
# Completed_solutions 81-90

# Task 81. Is this a triangle?
https://www.codewars.com/kata/56606694ec01347ce800001b
# Implement a method that accepts 3 integer values a, b, c. 
# The method should return true if a triangle can be built with the sides of given length and false in any other case.
# (In this case, all triangles must have surface greater than 0 to be accepted).

def is_triangle(a, b, c):
    return a+b > c and b+c > a and a+c > b 

# Task 82. Keep up the hoop
https://www.codewars.com/kata/55cb632c1a5d7b3ad0000145
# Alex just got a new hula hoop, he loves it but feels discouraged because his little brother is better than him
# Write a program where Alex can input (n) how many times the hoop goes round and it will return him an encouraging message :)
# -If Alex gets 10 or more hoops, return the string "Great, now move on to tricks".
# -If he doesn't get 10 hoops, return the string "Keep at it until you get it".

def hoop_count(n):
    return "Keep at it until you get it" if n < 10 else "Great, now move on to tricks"

# Task 83. Leap Years
https://www.codewars.com/kata/526c7363236867513f0005ca
# In this kata you should simply determine, whether a given year is a leap year or not. In case you don't know the rules, here they are:
# years divisible by 4 are leap years
# but years divisible by 100 are not leap years
# but years divisible by 400 are leap years

def isLeapYear(year):
    return (year%4 == 0 and not year%100 ==0) or year%400 == 0

# Task 84. Return Negative
https://www.codewars.com/kata/55685cd7ad70877c23000102
# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?
# Example: make_negative(1);  # return -1
# make_negative(-5); # return -5
# make_negative(0);  # return 0
# Notes: The number can be negative already, in which case no change is required.
# Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.

def make_negative( number ):
        return number*-1 if number > 0 else number

# Task 85. 
https://www.codewars.com/kata/52ceafd1f235ce81aa00073a
# We need a simple function that determines if a plural is needed or not. It should take a number, and return true if a plural should be used with that number or false if not. 
#  This would be useful when printing out a string such as 5 minutes, 14 apples, or 1 sun.
# You only need to worry about english grammar rules for this kata, where anything that isn't singular (one of something), 
#  it is plural (not one of something).
# All values will be positive integers or floats, or zero.

def plural(n):
    return n != 1

# Task 86. 
simple calculator
https://www.codewars.com/kata/5810085c533d69f4980001cf/
# You are required to create a simple calculator that returns the result of addition, subtraction, multiplication or division of two numbers.
# Your function will accept three arguments:
# The first and second argument should be numbers.
# The third argument should represent a sign indicating the operation to perform on these two numbers.
# if the variables are not numbers or the sign does not belong to the list above a message "unknown value" must be returned.
# Example:
# calculator(1, 2, '+') => 3
# calculator(1, 2, '$') # result will be "unknown value"

def calculator(x,y,op):
    if type(x) is int and type(y) is int:
        if op == '-':
            return x-y
        if op == '+':
            return x+y
        if op == '*':
            return x*y
        if op == '/':
            return x/y
        else: 
            return "unknown value"
    return "unknown value"

# Solution 2

def calculator(x,y,op):
    if str(op) not in '+-/*' or not str(x).isnumeric() or not str(y).isnumeric():
        return 'unknown value'
    return x + y if op == '+' else x - y if op == '-' else x * y if op == '*' else x / y
	
# Task 87. Student's Final Grade
https://www.codewars.com/kata/5ad0d8356165e63c140014d4
# Create a function finalGrade, which calculates the final grade of a student depending on two parameters: a grade for the exam and a number of completed projects.
# This function should take two arguments: exam - grade for exam (from 0 to 100); projects - number of completed projects (from 0 and above);
# This function should return a number (final grade). There are four types of final grades:
# 100, if a grade for the exam is more than 90 or if a number of completed projects more than 10.
# 90, if a grade for the exam is more than 75 and if a number of completed projects is minimum 5.
# 75, if a grade for the exam is more than 50 and if a number of completed projects is minimum 2.
# 0, in other cases

def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    if exam > 75 and projects >= 5:
        return 90
    if exam > 50 and projects >= 2:
        return 75
    return 0

# Task 88. The Office IV - Find a Meeting Room
https://www.codewars.com/kata/57f604a21bd4fe771b00009c
# Your job at E-Corp is both boring and difficult. It isn't made any easier by the fact that everyone constantly wants to have a meeting with you, and that the meeting rooms are always taken!
# In this kata, you will be given an array. Each value represents a meeting room. Your job? Find the first empty one and return its index (N.B. There may be more than one empty room in some test cases).
# 'X' --> busy 'O' --> empty
# If all rooms are busy, return 'None available!'.

def meeting(rooms):
    return rooms.index("O") if rooms.count("O") >= 1 else 'None available!'

# Task 89. Thinkful - Logic Drills: Traffic light
 https://www.codewars.com/kata/58649884a1659ed6cb000072
# You're writing code to control your town's traffic lights. 
# You need a function to handle each change from green, to yellow, to red, and then to green again.
# Complete the function that takes a string as an argument representing the current state of the light 
# and returns a string representing the state the light should change to.

def update_light(current):
    if current == "green":
        return "yellow"
    if current == "yellow":
        return "red"
    if current == "red":
        return "green"
    

# Task 90. Training JS #7: if..else and ternary operator
https://www.codewars.com/kata/57202aefe8d6c514300001fd
# Complete function saleHotdogs/SaleHotDogs/sale_hotdogs, function accept 1 parameters:n, n is the number of customers to buy hotdogs, different numbers have different prices (refer to the following table), return a number that the customer need to pay how much money.
# +---------------+-------------+
# |  numbers n    | price(cents)|
# +---------------+-------------+
# |n<5            |    100      |
# +---------------+-------------+
# |n>=5 and n<10  |     95      |
# +---------------+-------------+
# |n>=10          |     90      |
# +---------------+-------------+

def sale_hotdogs(n):
    if n <= 0:
        return 0 
    elif n < 5:
        return n*100
    elif 5 <= n < 10:
        return n*95
    else: 
        return n*90 
#
