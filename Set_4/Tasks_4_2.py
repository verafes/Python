# Real code challenges. Set #4
# Completed_solutions 411-420

#  Task 411. Fake Binary
https://www.codewars.com/kata/57eae65a4321032ce000002d
# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

def fake_bin(x):
      return "".join(["0" if int(el) < 5 else "1" for el in x])

# Solution #2:

def fake_bin(x):
    r = ""
    for el in x:
        if int(el) < 5 :
            el = "0" 
            r += el
        elif int(el) >= 5:
            el = "1"
            r += el 
    return r
	
# Task 412. Heads and Legs
https://www.codewars.com/kata/574c5075d27783851800169e
# Description. Everybody has probably heard of the animal heads and legs problem from the earlier years at school. It goes:
# “A farm contains chickens and cows. There are x heads and y legs. How many chickens and cows are there?” Where x <= 1000 and y <=1000
# Task: Assuming there are no other types of animals, work out how many of each animal are there.
# Return a tuple in Python - (chickens, cows) and an array list - [chickens, cows]/{chickens, cows} in all other languages.  
# If either the heads & legs is negative, the result of your calculation is negative or the calculation is a float return "No solutions" (no valid cases).

def animals(heads, legs):
    for chickens in range(0, heads+1):
        for cows in range(0, heads+1):
            if chickens*2 + cows*4 == legs and chickens+cows == heads:
                return chickens, cows
    return "No solutions"

# Solution #2:

def animals(heads, legs):
    chiken = (legs - 2*heads)/2 
    cow = heads - chiken
    if cow%1 !=0 or chiken%1 !=0:
        return 'No solutions'
    return (cow, chiken) if (cow >= 0 and chiken >= 0) else 'No solutions'

# Task 413. How many balls you need?
https://www.codewars.com/kata/57f945b77a28db0d750001f2
# How many balls would it take to assemble a regular tetrahedron, if the edge of the tetrahedron consists of N balls?
# Write a function that takes the value N (where 1 <= N <= 20000) and return the count of balls needed.
# Example: count_balls(5) == 35 -> 15 balls  +  10 balls  +  6 balls  +  3 balls  +  1 ball  =  35 balls

def count_balls(n):
    s = 0
    x = 1
    for i in range(1,n+1):
        s += x
        x += i+1
    return s

# Task 414. Sum of Triangular Numbers
https://www.codewars.com/kata/580878d5d27b84b64c000b51
# Your task is to return the sum of Triangular Numbers up-to-and-including the nth Triangular Number.
# Triangular Number: "any of the series of numbers (1, 3, 6, 10, 15, etc.) obtained by continued summation of the natural numbers 1, 2, 3, 4, 5, etc."
# [01]
# 02 [03]
# 04 05 [06]
# 07 08 09 [10]
# 11 12 13 14 [15]
# 16 17 18 19 20 [21]
# e.g. If 4 is given: 1 + 3 + 6 + 10 = 20.
# Triangular Numbers cannot be negative so return 0 if a negative number is given.

def sum_triangular_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += (i * (i + 1)) / 2
    return 0 if n < 0 else int(sum)

# Short solution:

def sum_triangular_numbers(n):
    return 0 if n < 0 else sum((i * (i + 1)) / 2 for i in range(1, n+1))
	
	
# Task 415. Beginner Series #5 Triangular Numbers
https://www.codewars.com/kata/56d0a591c6c8b466ca00118b
# Triangular number is the amount of points that can fill equilateral triangle.
# Example: the number 6 is a triangular number because all sides of a triangle has the same amount of points.
# Hint! T(n) = n * (n + 1) / 2, where n - is the size of one side, T(n) - is the triangular number.

def is_triangular(t):
    tnum = (int( (i * (i + 1)) / 2 ) for i in range(1, int(t)+1)) 
    return t in tnum

# Task 416. Consecutive items
https://www.codewars.com/kata/5f6d533e1475f30001e47514
# You are given a list of unique integers arr, and two integers a and b. Your task is to find out whether or not a and b appear consecutively in arr, 
# and return a boolean value (True if a and b are consecutive, False otherwise).
# It is guaranteed that a and b are both present in arr.

def consecutive(arr, a, b):
    return abs(arr.index(a) - arr.index(b)) == 1

# Task 417. String matchup
https://www.codewars.com/kata/59ca8e8e1a68b7de740001f4
# Given two arrays of strings, return the number of times each string of the second array appears in the first array.
# Example:
# array1 = ['abc', 'abc', 'xyz', 'cde', 'uvw']
# array2 = ['abc', 'cde', 'uap']
# How many times do the elements in array2 appear in array1?
# 'abc' appears twice in the first array (2)
# 'cde' appears only once (1)
# 'uap' does not appear in the first array (0)
# Therefore, solve(array1, array2) = [2, 1, 0]

def solve(a,b):
    arr = []
    count = 0
    for i in b:
        if i in a:
            count = a.count(i)
        arr.append(count)
        count = 0
    return arr

# Short solution:

def solve(a,b):
    return [a.count(e) for e in b]
	
# Task 418. String to integer conversion
https://www.codewars.com/kata/54fdadc8762e2e51e400032c
# You are asked to write a myParseInt method with the following rules:
# It should make the conversion if the given string only contains a single integer value (and possibly spaces - including tabs, line feeds... - at both ends)
# For all other strings (including the ones representing float values), it should return NaN
# It should assume that all numbers are not signed and written in base 10

def my_parse_int(string):
    return int(string) if string.strip().isdigit() else "NaN"

# Solution  2:

import string

def my_parse_int(s):
    s = s.strip()
    s1 = [el for el in s if el.isdigit()]
    s2 = [el for el in s if el in "!@#$%^&*?" ]
    s3 = [el for el in s if el.isalpha()]
    s4 = [el for el in s if el in string.punctuation]
    s5 = [el for el in s if el == " "]
    return int("".join(s1)) if s1 and not (s2 or s3 or s4 or s5) else 'NaN'

# Task 419. Sum of all the multiples of 3 or 5
https://www.codewars.com/kata/57f36495c0bb25ecf50000e7
# Your task is to write function findSum.
# Upto and including n, this function will return the sum of all multiples of 3 and 5.
# For example: 
# findSum(5) should return 8 (3 + 5)
# findSum(10) should return 33 (3 + 5 + 6 + 9 + 10)

def find(n):
    return sum([el for el in range(n+1) if el%3 == 0 or el%5 == 0])

# Task 420. 16+18=214
https://www.codewars.com/kata/5effa412233ac3002a9e471d/
# For this Kata you will have to forget how to add two numbers together.
# The best explanation on what to do for this kata is this meme: https://i.ibb.co/Y01rMJR/caf.png
# In simple terms, our method does not like the principle of carrying over numbers and just writes down every number it calculates :-)
# You may assume both integers are positive integers

def add(num1, num2):
    x = str(num1)
    y = str(num2)
    res = 0
    s = ''
    m = max(len(x), len(y))
    x = x.rjust(m, "0")
    y = y.rjust(m, "0")
    for i in range(m):
        res = int(x[i]) + int(y[i])
        s += str(res)
    return int(s)
	
#
