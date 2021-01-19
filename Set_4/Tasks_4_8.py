# Real code challenges. Set #4
# Completed_solutions 471-480

#  Task 471. Find The Duplicated Number in a Consecutive Unsorted List - Tougher Version
https://www.codewars.com/kata/558f0553803bc3c4720000af
# Here you will have to figure out an efficient strategy to solve the problem of finding the sole duplicate number among an unsorted array/list of numbers starting from 1 up to n.
# Hints: a solution in linear time can be found; using the most intuitive ones to search for duplicates that can run in O(n²) time won't work.

def find_dup(arr):
    new = []
    for el in arr:
        if el not in new:
            new.append(el)
    return sum(arr) - sum(new)
	
# Short solution 

def find_dup(arr):
    return sum(arr) - sum(range(1,max(arr)+1))
	
# Task 472. Pirate Code
https://www.codewars.com/kata/54599705cbae2aa60b0011a4
# Task. Create a function called one that accepts two params:
# a sequence
# a function
# and returns true only if the function in the params returns true for exactly one (1) item in the sequence.
# Example
# one([1, 3, 5, 6, 99, 1, 3], bigger_than_ten) -> true
# one([1, 3, 5, 6, 99, 88, 3], bigger_than_ten) -> false
# one([1, 3, 5, 6, 5, 1, 3], bigger_than_ten) -> false

def one(sq, fun): 
    return len([el for el in sq if fun(el)])== 1

# Task 473. Multiply array values and filter non-numeric
https://www.codewars.com/kata/55ed875819ae85ca8b00005c
# Your task is to write a function, which takes two arguments and returns a sequence. 
# First argument is a sequence of values, second is multiplier. 
# The function should filter all non-numeric values and multiply the rest by given multiplier.

def multiply_and_filter(seq, multiplier): 
    return [el * multiplier for el in seq if type(el) in [int, float]]

# Task 474. The Lazy Startup Office
https://www.codewars.com/kata/578fdcfc75ffd1112c0001a1 
# A startup office has an ongoing problem with its bin. Due to low budgets, they don't hire cleaners. As a result, the staff are left to voluntarily empty the bin. It has emerged that a voluntary system is not working and the bin is often overflowing. One staff member has suggested creating a rota system based upon the staff seating plan.
# Create a function binRota that accepts a 2D array of names. The function will return a single array containing staff names in the order that they should empty the bin.
# Adding to the problem, the office has some temporary staff. This means that the seating plan changes every month. Both staff members' names and the number of rows of seats may change. Ensure that the function binRota works when tested with these changes.
# Notes:
# All the rows will always be the same length as each other.
# There will be no empty spaces in the seating plan.
# There will be no empty arrays.
# Each row will be at least one seat long.
# An example seating plan is as follows: 
[ ["Stefan", "Raj",    "Marie"],
  ["Alexa",  "Amy",    "Edward"],
  ["Liz",    "Claire", "Juan"],
  ["Dee",    "Luke",   "Katie"] ]
# The rota should start with Stefan and end with Dee, taking the left-right zigzag path. 
# As an output you would expect in this case: 
# ["Stefan", "Raj", "Marie", "Edward", "Amy", "Alexa", "Liz", "Claire", "Juan", "Katie", "Luke", "Dee"# ])

def bin_rota(arr):
    arr = [el if i % 2 == 0 else el[::-1] for i, el in enumerate(arr)]
    res = []
    for el in arr:
        res.extend(el)
    return res
	

# Task 475. Sum - Square Even, Root Odd
https://www.codewars.com/kata/5a4b16435f08299c7000274f
# Complete the function that takes a list of numbers (nums), as the only argument to the function. 
# Take each number in the list and square it if it is even, or square root the number if it is odd. 
# Take this new list and return the sum of it, rounded to two decimal places.
# The list will never be empty and will only contain values that are greater than or equal to zero.

def sum_square_even_root_odd(nums):
    arr = ([el**2 if el%2 == 0 else el**0.5 for el in nums])
    return round(sum(arr), 2)

# Task 476. STRONGN Strong Number (Special Numbers Series #2)
https://www.codewars.com/kata/5a4d303f880385399b000001
# Definition. Strong number is the number that the sum of the factorial of its digits is equal to number itself.
# For example: 145, since 1! + 4! + 5! = 1 + 24 + 120 = 145
# So, 145 is a Strong number.
# Task. Given a number, Find if it is Strong or not.

import math

def strong_num(number):
    return "STRONG!!!!" if sum([math.factorial(int(el)) for el in str(number)]) == number else "Not Strong !!"

# Task 477. The old switcheroo 2
https://www.codewars.com/kata/55d6a0e4ededb894be000005
# Write a function that takes in a string str and replaces all the letters with their respective positions in the English alphabet.
# encode('abc') == '123'   # a is 1st in English alpabet, b is 2nd and c is 3rd
# encode('codewars') == '315452311819'
# encode('abc-#@5') == '123-#@5'

def encode(string):
    abc = " abcdefghijklmnopqrstuvwxyz"
    return "".join([str(abc.index(char.lower())) if char.isalpha() else char for char in string])


# Task 478. Failed Filter - Bug Fixing #3
https://www.codewars.com/kata/55c606e6babfc5b2c500007c
# Oh no, Timmy's filter doesn't seem to be working? Your task is to fix the FilterNumber function to remove all the numbers from the string.

# Given:

def filter_numbers(string):
    return "".join([x for x in string if int(x)])
	
# Fixed code:

def filter_numbers(string):
    return "".join([x for x in string if not x.isdigit()])

# Task 479. A Rule of Divisibility by 7 
https://www.codewars.com/kata/55e6f5e58f7817808e00002e
# A number m of the form 10x + y is divisible by 7 if and only if x − 2y is divisible by 7. In other words, subtract twice the last digit from the number formed by the remaining digits.
# Continue to do this until a number known to be divisible or not by 7 is obtained; you can stop when this number has at most 2 digits because you are supposed to know if a number of at m# ost 2 digits is divisible by 7 or not.
# The original number is divisible by 7 if and only if the last number obtained using this procedure is divisible by 7.
# Examples:
# 1 - m = 371 -> 37 − (2×1) -> 37 − 2 = 35 ; thus, since 35 is divisible by 7, 371 is divisible by 7. -> The number of steps to get the result is 1.
# 2 - m = 1603 -> 160 - (2 x 3) -> 154 -> 15 - 8 = 7 and 7 is divisible by 7.
# 3 - m = 372 -> 37 − (2×2) -> 37 − 4 = 33 ; thus, since 33 is not divisible by 7, 372 is not divisible by 7. -> The number of steps to get the result is 1.
# 4 - m = 477557101->47755708->4775554->477547->47740->4774->469->28 and 28 is divisible by 7, so is 477557101.->  The number of steps is 7.
# Task:
# Your task is to return to the function seven(m) (m integer >= 0) an array (or a pair, depending on the language) of numbers, 
# the first being the last number m with at most 2 digits obtained by your function (this last m will be divisible or not by 7), 
# the second one being the number of steps to get the result.

def seven(m):
    steps = 0
    while m > 99:
        m = m // 10 - 2*(m % 10)
        steps += 1
    return (m, steps)

# Task 480. How much coffee do you need?
https://www.codewars.com/kata/57de78848a8b8df8f10005b1
# Your task here is to define how much coffee you need to stay awake after your night. You will have to complete a function that take an array of events in arguments, 
# according to this list you will return the number of coffee you need to stay awake during day time. Note: If the count exceed 3 please return 'You need extra sleep'.
# The list of events can contain the following:
# You come here, to solve some kata ('cw').
# You have a dog or a cat that just decide to wake up too early ('dog' | 'cat').
# You just watch a movie ('movie').
# Other events can be present and it will be represent by arbitrary string, just ignore this one.
# Each event can be downcase/lowercase, or uppercase. If it is downcase/lowercase you need 1 coffee by events and if it is uppercase you need 2 coffees.

def how_much_coffee(events):
    if len(events) == 0: return 0
    lst = ['cw', 'dog', 'cat', 'movie']
    coffee = 0
    for el in events:
        if el.isupper() and el.lower() in lst:
            coffee += 2
        if el in lst:
            coffee += 1
    return coffee if coffee <= 3 else 'You need extra sleep'

#
