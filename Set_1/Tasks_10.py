# Real code challenges. Set #1
# Completed_solutions 91-100

# Task 91. Transportation on vacation
https://www.codewars.com/kata/568d0dd208ee69389d000016
# After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and your girlfriend and try to leave all the mess behind you.
# You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.
# Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.
# Write a code that gives out the total amount for different days(d).

def rental_car_cost(d):
    total_cost = d * 40
    if d >= 7:
        total_cost -= 50
    elif d >= 3:
        total_cost -= 20
    return total_cost
	
# Task 92. Watermelon
https://www.codewars.com/kata/55192f4ecd82ff826900089e
# One hot summer day Pete and his friend Billy decided to buy watermelons. They chose the biggest crate. They rushed home, dying of thirst, and decided to divide their loot, however they faced a hard problem.
# Pete and Billy are great fans of even numbers, that's why they want to divide the number of watermelons in such a way that each of the two parts consists of an even number of watermelons. However, it is not obligatory that the parts are equal.
# Example: the boys can divide a stack of 8 watermelons into 2+6 melons, or 4+4 melons.
# The boys are extremely tired and want to start their meal as soon as possible, that's why you should help them and find out, whether they can divide the fruits in the way they want. For sure, each of them should get a part of positive weight.
# Task
# Given an integral number of watermelons w (1 ≤ w ≤ 100; 1 ≤ w in Haskell), check whether Pete and Billy can divide the melons so that each of them gets an even amount.

def divide(weight):
    if weight % 2 != 0 or  weight <= 2:
        return False
    return weight % 2 == 0 

# Task 93. Will you make it?
https://www.codewars.com/kata/5861d28f124b35723e00005e
# You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! 
# You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left. 
# Considering these factors, write a function that tells you if it is possible to get to the pump or not. 
# Function should return true (1 in Prolog) if it is possible and false (0 in Prolog) if not. The input values are always positive.

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return fuel_left*mpg >= distance_to_pump
	
# Task 94. GCD sum
https://www.codewars.com/kata/5dd259444228280032b1ed2a
# Given the sum and gcd of two numbers, return those two numbers in ascending order. If the numbers do not exist, return -1
# For example: Given sum = 12 and gcd = 4...
# solve(12,4) = [4,8]. The two numbers 4 and 8 sum to 12 and have a gcd of 4.
# solve(12,5) = -1. No two numbers exist that sum to 12 and have gcd of 5.
# solve(10,2) = [2,8]. Note that [4,6] is also a possibility but we pick the one with the lower first element: 2 < < 4, so we take [2,8].

def solve(s,g):
    b = s - g
    return (g, b) if s % g == 0 else -1 

# Task 95. What century is it?
https://www.codewars.com/kata/52fb87703c1351ebd200081f
# Return the century of the input year. The input will always be a 4 digit string, so there is no need for validation.
# Examples: "1999" --> "20th", "2011" --> "21st", "2154" --> "22nd", "2259" --> "23rd", "1124" --> "12th", "2000" --> "20th"

import math
def what_century(year):
    century = math.ceil(int(year)/100)
    last = century%10
    if last == 1 and century != 11:
        return f"{century}st"
    elif last == 2 and century != 12:
        return f"{century}nd"
    elif last == 3 and century != 13:
        return f"{century}rd"
    else:
        return f"{century}th"

# Task 96. Build a pile of Cubes
https://www.codewars.com/kata/5592e3bd57b64d00f3000047
# Your task is to construct a building which will be a pile of n cubes. The cube at the bottom will have a volume of n^3, the cube above will have volume of (n-1)^3 and so on until the top which will have a volume of 1^3.
# You are given the total volume m of the building. Being given m can you find the number n of cubes you will have to build?
# The parameter of the function findNb (find_nb, find-nb, findNb) will be an integer m and you have to return the integer n such as n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n.
# Examples: findNb(1071225) --> 45
# findNb(91716553919377) --> -1

def find_nb(m):
    count = 0
    i = 1
    while m > 0:
        m = m - (i ** 3)
        count += 1
        i += 1
    return count if m == 0 else -1
	
# Task 97. Difference Of Squares
https://www.codewars.com/kata/558f9f51e85b46e9fa000025
# Find the difference between the sum of the squares of the first n natural numbers (1 <= n <= 100) and the square of their sum.
# Example: For example, when n = 10:
# The square of the sum of the numbers is:
# (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)2 = 552 = 3025
# The sum of the squares of the numbers is:
# 12 + 22 + 32 + 42 + 52 + 62 + 72 + 82 + 92 + 102 = 385
# Hence the difference between square of the sum of the first ten natural numbers and the sum of the squares of those numbes is: 3025 - 385 = 2640

def difference_of_squares(n):
    num = [i+1 for i in range(0,n)]
    squares = [x**2 for x in range(1,n+1)]
    return sum(num)**2 - sum(squares)

#Solution 2:

def difference_of_squares(n):
    return sum(i for i in range(1,n+1))**2 - sum(i*i for i in range(1,n+1)) 
	
# Task 98. Find the next perfect square!
https://www.codewars.com/kata/56269eb78ad2e4ced1000013
# You might know some pretty large perfect squares. But what about the NEXT one?
# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
# If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is positive.
# Examples:
# findNextSquare(121) --> returns 144
# findNextSquare(114) --> returns -1 since 114 is not a perfect

def find_next_square(sq):
    if int(sq ** 0.5) < sq ** 0.5:
        return -1
    else:
        return ((sq ** 0.5) + 1)**2

# Task 99. Graceful Tipping
https://www.codewars.com/kata/5eb27d81077a7400171c6820
# Adding tip to a restaurant bill in a graceful way can be tricky, thats why you need make a function for it.
# The function will receive the restaurant bill (always a positive number) as an argument. You need to 1) add at least 15% in tip, 2) round that number up to an elegant value and 3) return it.
# What is an elegant number? It depends on the magnitude of the number to be rounded. Numbers below 10 should simply be rounded to whole numbers. Numbers 10 and above should be rounded like this:
# 10 - 99.99... ---> Round to number divisible by 5
# 100 - 999.99... ---> Round to number divisible by 50
# 1000 - 9999.99... ---> Round to number divisible by 500
# Examples
#  1  -->    2
#  7  -->    9
# 12  -->   15
# 86  -->  100

import math
def graceful_tipping(bill):
    bill = math.ceil(bill * 1.15)
    divisible = 5
    n = 100
    if bill < 10: 
        return bill
    while True:
        if bill < n:
            while bill % divisible != 0:
                bill += 1
            return bill
        n = n * 10
        divisible = divisible * 10
 
# Task 100. Money, Money, Money 
https://www.codewars.com/kata/563f037412e5ada593000114
# Mr. Scrooge has a sum of money 'P' that he wants to invest. Before he does, he wants to know 
# how many years 'Y' this sum 'P' has to be kept in the bank in order for it to amount to a desired sum of money 'D'.
# The sum is kept for 'Y' years in the bank where interest 'I' is paid yearly. After paying taxes 'T' for the year the new sum is re-invested.
# Note to Tax: not the invested principal is taxed, but only the year's accrued interest
# Example:
#   Let P be the Principal = 1000.00      
#   Let I be the Interest Rate = 0.05      
#   Let T be the Tax Rate = 0.18      
#   Let D be the Desired Sum = 1100.00
# After 1st Year -->   P = 1041.00
# After 2nd Year -->   P = 1083.86
# After 3rd Year -->   P = 1128.30
# Thus Mr. Scrooge has to wait for 3 years for the initial principal to amount to the desired sum.
# Your task is to complete the method provided and return the number of years 'Y' as a whole in order for Mr. Scrooge to get the desired sum.
# Assumption: Assume that Desired Principal 'D' is always greater than the initial principal. However it is best to take into consideration that if Desired Principal 'D' is equal to Principal 'P' this should return 0 Years.

def calculate_years(principal, interest, tax, desired):
    y = 0
    while principal < desired:
        principal += principal * interest * (1 - tax)
        y += 1
    return y

#
