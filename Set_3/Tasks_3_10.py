# Real code challenges. Set #3-10
# Completed_solutions 3.91-3.100

#  Task 3.91. List Filtering
https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
# In this kata you will create a function that takes a list of non-negative integers and strings 
#and returns a new list with the strings filtered out.
# Example:
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

def filter_list(l):
    return [x for x in l if type(x) is int]
	
# Task 3.92. Parts of a list
https://www.codewars.com/kata/56f3a1e899b386da78000732
# Write a function partlist that gives all the ways to divide a list (an array) of at least two elements into two non-empty parts.
# Each two non empty parts will be in a pair (or an array for languages without tuples or a structin C - C: see Examples test Cases - )
# Each part will be in a string
# Elements of a pair must be in the same order as in the original array.
# a = [|"az", "toto", "picaro", "zone", "kiwi"|] -->
# [("az", "toto picaro zone kiwi"), ("az toto", "picaro zone kiwi"), ("az toto picaro", "zone kiwi"), ("az toto picaro zone", "kiwi")]

def partlist(arr):
    return [(' '.join(arr[:i]), ' '.join(arr[i:])) for i in range(1, len(arr))]

# Task 3.93. Figurate Numbers #2 - Pronic Number
https://www.codewars.com/kata/55b1e5c4cbe09e46b3000034
# You have to create a function isPronic to check whether the argument passed is a Pronic Number and return true if it is & false otherwise.
# Description: Pronic Number -A pronic number, oblong number, rectangular number or heteromecic number, 
# is a number which is the product of two consecutive integers, that is, n(n + 1).
# The first few Pronic Numbers are - 0, 2, 6, 12, 20, 30, 42...
# Explanation:
#   0 = 0 × 1   // ∴  0 is a Pronic Number
#   2 = 1 × 2   // ∴  2 is a Pronic Number
#   6 = 2 × 3   // ∴  6 is a Pronic Number
#  12 = 3 × 4   // ∴ 12 is a Pronic Number
#  20 = 4 × 5   // ∴ 20 is a Pronic Number
#  30 = 5 × 6   // ∴ 30 is a Pronic Number
#  42 = 6 × 7   // ∴ 42 is a Pronic Number

def is_pronic(n):
    for i in range(0, n+1):
        if i * (i+1) == n:
            return True 
    return False

# Task 3.94. Mythical Heads and Tails
https://www.codewars.com/kata/5751aa92f2dac7695d000fb0
# The formidable "Orthus" is a 2 headed dog with 1 tail. The mighty "Hydra" has 5 heads and 1 tail.
# Before Hercules goes in, he asks you "How many of each beast am I up against!?".
# You know the total number of heads and the total number of tails, that's the dangerous parts, right? 
# But you didn't consider how many of each beast.
# Task: Given the number of heads and the number of tails, work out the number of each mythical beast!
# The data is given as two parameters. Your answer should be returned as an array. 
# If there aren't any cases for the given amount of heads and tails - return "No solutions" 

def beasts(heads, tails):
    if tails == 0 and heads == 0: return [0, 0]

    if tails > heads or tails <= 0 or heads < 0:
        return 'No solutions'
    
    if heads % tails == 0: 
        l = heads+1
        h = heads+1
    else:
        l = round((heads+1)/2)
        h = round((heads+1)/2)

    for orthus in range(0, l):
        for hydra in range(0, h):
            if orthus*2 + hydra*5 == heads and orthus+hydra == tails:
                return [orthus, hydra]

# Solutions #2:

def beasts(heads, tails):
    # o + h = tails
    # o * 2 + h * 5 = heads
    # (tails - h) * 2 + h * 5 = heads
    # tails * 2 + h * 3 = heads
    # h = (heads - tails * 2) / 3
    hydra = (heads - tails * 2) / 3
    orthus = tails - hydra
    return [orthus, hydra] if hydra * orthus >= 0 else "No solutions" 
	
# Task 3.95. Strong password?
https://www.codewars.com/kata/57e35f1bc763b8ccce000038 
# Your users' passwords were all stolen in the Yahoo! hack, and it turns out they have been lax in creating secure passwords. 
# Create a function that checks their new password (passed as a string) to make sure it meets the following requirements:
# -Between 8 - 20 characters
# -Contains only the following characters (and at least one character from each category):
# -uppercase letters,
# -lowercase letters,
# -digits,
# -special characters from !@#$%^&*?
# Return "valid" if passed or "not valid" otherwise.

import string

def check_password(s):
    s0 = 8<= len(s)<=20
    s1 = [el for el in s if el.isupper() ]
    s2 = [el for el in s if el.islower() ]
    s3 = [el for el in s if el.isdigit() ]
    s4 = [el for el in s if el in "!@#$%^&*?" ]
    s5 = [el for el in s if el not in string.ascii_letters + string.digits + "!@#$%^&*?"]
    return "valid" if s0 and s1 and s2 and s3 and s4 and  not s5 else "not valid"

# Task 3.96. Zalgo text reader
https://www.codewars.com/kata/588fe9eaadbbfb44b70001fc	
# Zalgo text is text that leaks into our plane of existence from a corrupted dimension of Unicode. 
# Complete the function that converts a string of Zalgo text into a string interpretable by our mortal eyes. 
# For example, the string above would be converted into:
# Have a great day!
# The converted string should only feature ASCII characters.

def read_zalgo(zalgotext):
    return "".join([c for c in zalgotext if c.isascii()])

# Task 3.97. Scrolling Text
https://www.codewars.com/kata/5a995c2aba1bb57f660001fd
# Let's create some scrolling text!
# Your task is to complete the function which takes a string, 
# and returns an array with all possible rotations of the given string, in uppercase.
# Example: scrollingText("codewars") should return:
# [ "CODEWARS", "ODEWARSC", "DEWARSCO", "EWARSCOD", "WARSCODE", "ARSCODEW", "RSCODEWA", "SCODEWAR" ]

def scrolling_text(text):
    text = text.upper()
    arr = []
    for i in range(len(text)):
        arr.append(text)
        text = text[1:]+text[0]
    return arr
	
# Solution #2 

def scrolling_text(text):
    text = text.upper()
    return [text[i:]+text[:i] for i in range(len(text))]

# Task 3.98. Replace all items
https://www.codewars.com/kata/57ae18c6e298a7a6d5000c7a
# Write function replaceAll (Python: replace_all) that will replace all occurrences of an item with another.
# Python / JavaScript: The function has to work for strings and lists.
# Example: replaceAll [1,2,2] 1 2 -> in list [1,2,2] we replace 1 with 2 to get new list [2,2,2]
# replaceAll(replaceAll(array: [1,2,2], old: 1, new: 2) // [2,2,2]

def replace_all(obj, find, replace):
    res = ""
    if type(obj) is str:
        res = obj.replace(find, replace)
    if type(obj) is list:
        res = [replace if el == find else el for el in obj ] 
    return res

# Solution #2 

def replace_all(obj, find, replace):
    return [replace if el == find else el for el in obj] if type(obj) is list else obj.replace(find, replace)

# Task 3.99. Moving Average
https://www.codewars.com/kata/5c745b30f6216a301dc4dda5
# Background: Moving average of a set of values and a window size is a series of local averages.
# Example:
# Values: [1, 2, 3, 4, 5]
# Window size: 3
# Moving average is calculated as:
#  1, 2, 3, 4, 5
#  |     |
#  ^^^^^^^
#  (1+2+3)/3 = 2

#   1, 2, 3, 4, 5
#      |     |
#      ^^^^^^^
#      (2+3+4)/3 = 3

#   1, 2, 3, 4, 5
#         |     |
#         ^^^^^^^
#         (3+4+5)/3 = 4
# Here, the moving average would be [2, 3, 4]

# Task: Given a list values of integers and an integer n representing size of the window, calculate and return the moving average.
# When integer n is equal to zero or the size of values list is less than window's size, return None 

def moving_average(values,n):
    if n == 0 or n > len (values):
        return None
    a = []
    for i in range (len(values)-n+1):
        a.append(sum(values[i:i+n])/n)
    return a

# Solution #2 

def moving_average(values,n):
    return None if n <= 0 or n > len(values) else [(sum(values[i:i+n])/n) for i in range (len(values)-n+1)]
	
# Task 3.100. Sum of Array Averages
https://www.codewars.com/kata/56d5166ec87df55dbe000063
# Program a function sumAverage(arr) where arr is an array containing arrays full of numbers, for example:
# sum_average([[1, 2, 2, 1], [2, 2, 2, 1]]) -> [6, 7] -> answer being 3
# First, determine the average of each array. Then, return the sum of all the averages.
# All numbers will be less than 100 and greater than -100.
# arr will contain a maximum of 50 arrays.
# After calculating all the averages, add them all together, then round down.

import math

def sum_average(arr):
    a = []
    for i in range(len(arr)):
        el = sum(arr[i])/len(arr[i])
        a.append(el)
    return math.floor(sum(a))

#
