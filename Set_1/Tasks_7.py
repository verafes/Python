# Real code challenges. 
# Set #1. Completed_solutions 61-70

# Task 61. Right in the Centre
https://www.codewars.com/kata/5f5da7a415fbdc0001ae3c69
# This is inspired by one of Nick Parlante's exercises on the CodingBat online code practice tool.
# Given a sequence of characters, does "abc" appear in the CENTER of the sequence?
# The sequence of characters could contain more than one "abc".
# To define CENTER, the number of characters in the sequence to the left and right of the "abc" (which is in the middle) must differ by at most one.
# If it is in the CENTER, return True. Otherwise, return False.
# Write a function as the solution for this problem. This kata looks simple, but it might not be easy.
# Example
# is_in_middle("AAabcBB")  ->  True
# is_in_middle("AabcBB")   ->  True
# is_in_middle("AabcBBB")  ->  False

def is_in_middle(sequence):
    return 'abc' in sequence[(len(sequence)-1)//2-1 : (len(sequence)+2)//2+1]

# Task 62. Fix the Bugs (Syntax) - My First Kata
https://www.codewars.com/kata/56aed32a154d33a1f3000018
# Hello, this is my first Kata so forgive me if it is of poor quality.
# In this Kata you should fix/create a program that returns the following values:
# false/False if either a or b (or both) are not numbers
# a % b plus b % a if both arguments are numbers
# You may assume the following: If a and b are both numbers, neither of a or b will be 0.

def my_first_kata(a,b):
    if type(a) is not int:
        return False
    elif type(b) is not int: 
        return False
    else: 
        return a % b + b % a

# Task 63. Can we divide it?
https://www.codewars.com/kata/5a2b703dc5e2845c0900005a/train/python
# Your task is to create functionisDivideBy (or is_divide_by) to check if an integer number is divisible by each out of two arguments.
# A few cases: (-12, 2, -6)  ->  true
# (-12, 2, -5)  ->  false
# (45, 1, 6)    ->  false
# (45, 5, 15)   ->  true
# (4, 1, 4)     ->  true
# (15, -5, 3)   ->  true

def is_divide_by(number, a, b):
    return number%a == 0 and number%b == 0

# Task 64. Drink about
https://www.codewars.com/kata/56170e844da7c6f647000063
# Kids drink toddy. Teens drink coke. Young adults drink beer. Adults drink whisky.
# Make a function that receive age, and return what they drink.
# Rules:
# Children under 14 old. Teens under 18 old. Young under 21 old. Adults have 21 or more.

def people_with_age_drink(age):
    if age >= 21: 
        return "drink whisky"
    elif age >= 18:
        return "drink beer"
    elif age >= 14:
        return "drink coke"
    else: 
        return "drink toddy"

# Task 65. Fix your code before the garden dies!
https://www.codewars.com/kata/57158fb92ad763bb180004e7
# You have an award-winning garden and everyday the plants need exactly 40mm of water. 
# You created a great piece of JavaScript to calculate the amount of water your plants will need when you have taken into consideration the amount of rain water that is forecast for the day. 
# Your jealous neighbour hacked your computer and filled your code with bugs.
# Your task is to debug the code before your plants die!

def rain_amount(mm):
    if mm < 40:
         return f"You need to give your plant {40 - mm}mm of water"
    else:
         return "Your plant has had more than enough water for today!"
#
# Task 66. Get Planet Name By ID
https://www.codewars.com/kata/515e188a311df01cba000003/
# The function is not returning the correct values. Can you figure out why?
# get_planet_name(3) # should return 'Earth'

def get_planet_name(id):
    name=""
    if id == 1: name = "Mercury"
    if id == 2: name = "Venus"
    if id == 3: name = "Earth"
    if id == 4: name = "Mars"
    if id == 5: name = "Jupiter"
    if id == 6: name = "Saturn"
    if id == 7: name = "Uranus"  
    if id == 8: name = "Neptune"
    return name

# Task 67. Grasshopper - Check for factor
https://www.codewars.com/kata/55cbc3586671f6aa070000fb
# This function should test if the factor is a factor of base.
# Return true if it is a factor or false if it is not.
# About factors. Factors are numbers you can multiply together to get another number.
# 2 and 3 are factors of 6 because: 2 * 3 = 6
# You can find a factor by dividing numbers. If the remainder is 0 then the number is a factor.
# You can use the mod operator (%) in most languages to check for a remainder
# For example 2 is not a factor of 7 because: 7 % 2 = 1
# Note: base is a non-negative number, factor is a positive number.

def check_for_factor(base, factor):
    return base % factor == 0

# Task 68. Grasshopper - Debug
https://www.codewars.com/kata/55cb854deb36f11f130000e1
# Your friend is traveling abroad to the United States so he wrote a program to convert fahrenheit to celsius. Unfortunately his code has some bugs.
# Find the errors in the code to get the celsius converter working properly.
# To convert fahrenheit to celsius: # celsius = (fahrenheit - 32) * (5/9)
# Remember that typically temperatures in the current weather conditions are given in whole numbers. 
# It is possible for temperature sensors to report temperatures with a higher accuracy such as to the nearest tenth. 
# Instrument error though makes this sort of accuracy unreliable for many types of temperature measuring sensors.

def weather_info (temp):
    c = (temp - 32) * (5/9)
    if (c < 0):
        return f"{c} is freezing temperature"
    else:
        return f"{c} is above freezing temperature"

# Task 69. Grasshopper - If/else syntax debug
https://www.codewars.com/kata/57089707fe2d01529f00024a
# While making a game, your partner, Greg, decided to create a function to check if the user is still alive called checkAlive/CheckAlive/check_alive. Unfortunately, Greg made some errors while creating the function.
# checkAlive/CheckAlive/check_alive should return true if the player's health is greater than 0 or false if it is 0 or below.
# The function receives one parameter health which will always be a whole number between -10 and 10.

def check_alive(health):
    return health > 0

# Task 70. How do I compare numbers?
https://www.codewars.com/kata/55d8618adfda93c89600012e
# What could be easier than comparing integer numbers? 
# However, the given piece of code doesn't recognize some of the special numbers for a reason to be found. 
# Your task is to find the bug and eliminate it.

def what_is(x):
    if x == 42:
        return 'everything'
    elif x == 42 * 42:
        return 'everything squared'
    else:
        return 'nothing'

#