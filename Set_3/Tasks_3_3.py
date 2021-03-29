# Real code challenges. Set #3-3
# Completed_solutions 3.21-3.30.

# Task 3.21. Find Maximum and Minimum Values of a List
https://www.codewars.com/kata/577a98a6ae28071780000989
# Your task is to make two functions, max and min (maximum and minimum in PHP and Python) 
# that take a(n) array/vector of integers list as input 
# and outputs, respectively, the largest and lowest number in that array/vector.

def minimum(arr):
    mi = min(arr)
    return mi

def maximum(arr):
    ma = max(arr)
    return ma

# Task 3.22. Find min and max
https://www.codewars.com/kata/57a1ae8c7cb1f31e4e000130
# Implement a function that returns the minimal and the maximal value of a list (in this order).

def get_min_max(seq): 
    seq = sorted(seq)
    return seq[0], seq[-1] 
	
# Task 3.23. Find something in an Array
https://www.codewars.com/kata/53d56645ed770fb7c500085f
# Create a find function that takes a string and an array as arguments. If the string is in the array, return true.
# For example: find("hello", ["bye bye","hello"]) # return true
# find("anything", ["bye bye","hello"]) # return false

def find(str, lst):
    return str in lst 

# Task 3.24. Find the first non-consecutive number
https://www.codewars.com/kata/58f8a3a27a5c28d92e000144
# Your task is to find the first element of an array that is not consecutive.
# By not consecutive we mean not exactly 1 larger than the previous element of the array.
# E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive 
# but 6 is not, so that's the first non-consecutive number.
# If the whole array is consecutive then return null2.
# The array will always have at least 2 elements1 and all elements will be numbers. The numbers will also all be unique and in ascending order. 
# The numbers could be positive or negative and the first non-consecutive could be either too!

def first_non_consecutive(arr):
    for i in range(0,len(arr)-1):
        if arr[i+1] - arr[i] > 1:
            return arr[i+1]

# Task 3.25. Find the Slope
https://www.codewars.com/kata/55a75e2d0803fea18f00009d
# [a,b,c,d] representing two points (a, b) and (c, d), return a string representation of the slope of the line joining these two points.
# For an undefined slope (division by 0), return undefined . Note that the "undefined" is case-sensitive.

def find_slope(points):
    a,b,c,d = points
    return 'undefined' if a == c else str(int((b - d) / (a - c)))

# Task 3.26. Find the smallest integer in the array
https://www.codewars.com/kata/55a2d7ebe362935a210000b2
# Given an array of integers your solution should find the smallest integer.
# For example:
# Given [34, 15, 88, 2] your solution will return 2
# Given [34, -345, -1, 100] your solution will return -345
# You can assume, for the purpose of this kata, that the supplied array will not be empty.

def find_smallest_int(arr):
    return min(arr)

# Task 3.27. 
https://www.codewars.com/kata/563e320cee5dddcf77000158
# It's the academic year's end, fateful moment of your school report. The averages must be calculated. 
# All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.
# Return the average of the given array rounded down to its nearest integer. The array will never be empty.

def get_average(marks):
    return sum(marks)//len(marks)

# Task 3.28. How good are you really?
https://www.codewars.com/kata/5601409514fc93442500010b
# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the average student in your class.
# You receive an array with your peers' test scores. Now calculate the average and compare your score!
# Return True if you're better, else False!
# Note: Your points are not included in the array of your class's points. 
# For calculating the average point you may add your point to the given array!

def better_than_average(class_points, your_points):
    average = (sum(class_points) + your_points) / (len(class_points) + 1)
    return your_points > average

# Task 3.29. Head, Tail, Init and Last
https://www.codewars.com/kata/54592a5052756d5c5d0009c3
# Haskell has some useful functions for dealing with lists. Your job is to implement these functions in your given language. 
# Make sure it doesn't edit the array; that would cause problems! Here's a cheat sheet:
# | HEAD | <----------- TAIL ------------> |
# [  1,  2,  3,  4,  5,  6,  7,  8,  9,  10]
# | <----------- INIT ------------> | LAST |
# head [x] = x
# tail [x] = []
# init [x] = []
# last [x] = x

def head(arr):
    return arr[0]

def tail(arr):
    return arr[1:]

def init(arr):
    return arr[:-1]

def last(arr):
    return arr[-1]

# Task 3.30. Largest pair sum in array
https://www.codewars.com/kata/556196a6091a7e7f58000018
# Given a sequence of numbers, find the largest pair sum in the sequence.
# For example
# [10, 14, 2, 23, 19] -->  42 (= 23 + 19)
# [99, 2, 2, 23, 19]  --> 122 (= 99 + 23)
# Input sequence contains minimum two elements and every element is an integer.

def largest_pair_sum(numbers): 
    numbers = sorted(numbers)[::-1]
    return numbers[0] + numbers[1]
