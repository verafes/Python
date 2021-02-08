# Real code challenges. Set #2
# Completed_solutions 2.31-2.40

# Task 2.31. Sentence Smash
https://www.codewars.com/kata/53dc23c68a0c93699800041d
# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. 
# You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. 
# Be careful, there shouldn't be a space at the beginning or the end of the sentence!
# Example: ['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'

def smash(words):
    return " ".join(words)

# Task 2.32. Are the numbers in order?
https://www.codewars.com/kata/56b7f2f3f18876033f000307
# In this Kata, your function receives an array of integers as input. Your task is to determine whether the numbers are in ascending order. 
# An array is said to be in ascending order if there are no two adjacent integers where the left integer exceeds the right integer in value.
# For the purposes of this Kata, you may assume that all inputs are valid, i.e. non-empty arrays containing only integers.
# Note that an array of 1 integer is automatically considered to be sorted in ascending order since all (zero) adjacent pairs of integers 
# satisfy the condition that the left integer does not exceed the right integer in value. 
# An empty list is considered a degenerate case and therefore will not be tested in this Kata - 
# feel free to raise an Issue if you see such a list being tested.
# For example:
# in_asc_order([1,2,4,7,19]) # returns True
# in_asc_order([1,2,3,4,5]) # returns True
# in_asc_order([1,6,10,18,2,4,20]) # returns False
# in_asc_order([9,8,7,6,5,4,3,2,1]) # returns False because the numbers are in DESCENDING order

def in_asc_order(arr):
    return arr == sorted(arr)
	
# Task 2.33. Array Mash
https://www.codewars.com/kata/582642b1083e12521f0000da
# Mash 2 arrays together so that the returning array has alternating elements of the 2 arrays. 
# Both arrays will always be the same length.
# eg. [1,2,3] + ['a','b','c'] = [1, 'a', 2, 'b', 3, 'c']

def array_mash(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i])
        c.append(b[i])
    return c
	
# Task 2.34. Array plus array
https://www.codewars.com/kata/5a2be17aee1aaefe2a000151
# I'm new to coding and now I want to get the sum of two arrays...actually the sum of all their elements. 
# I'll appreciate for your help.
# P.S. Each array includes only integer numbers. Output is a number too.

def array_plus_array(arr1,arr2):
    return sum(arr1+arr2)
	
# Task 2.35. Bases Everywhere
https://www.codewars.com/kata/5f47e79e18330d001a195b55
# You will have to create a function which takes in a sequence of numbers in random order 
# and you will have to return the correct base of those numbers.
# The base is the number of unique digits. For example, a base 10 number can have 10 unique digits: 
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 and a base 2 number (Binary) can have 2 unique digits: 0 and 1.
# Constraints
# The sequence will always be 10 numbers long and we know that the base is going to be between 2 and 10 inclusive 
# so no need to worry about any letters. When sorted, the sequence is made up of consecutive numbers.
# Examples
# [ "1", "2", "3", "4", "5", "6", "7", "8", "9", "10" ]     -->  10
# [ "1", "2", "3", "4", "5", "6", "10", "11", "12", "13" ]  -->   7

def base_finder(seq):
    return int(max(list("".join(seq))))+1

# Task 2.36. 
https://www.codewars.com/kata/5413759479ba273f8100003d
# Write a function reverse which reverses a list (or in clojure's case, any list-like data structure)
# (the dedicated builtin(s) functionalities are deactivated)

def reverse(lst):
    empty_list = list()
    for i in range(len(lst)-1,-1,-1):
        empty_list.append(lst[i])
    return empty_list  

# Task 2.37. A Needle in the Haystack
https://www.codewars.com/kata/56676e8fabd2d1ff3000000c
# Can you find the needle in the haystack?
# Write a function findNeedle() that takes an array full of junk but containing one "needle"
# After your function finds the needle it should return a message (as a string) that says:
# "found the needle at position " plus the index it found the needle, so:
# find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
# should return "found the needle at position 5"

def find_needle(haystack):
    index = haystack.index('needle')
    return f"found the needle at position {index}"

# Task 2.38. Mean Means
https://www.codewars.com/kata/57c6b44f58da9ea6c20003da
# Introduction. 
# Take a list of n numbers a1, a2, a3, ..., aN to start with.
# Arithmetic mean (or average) is the sum of these numbers divided by n.
# Geometric mean (or average) is the product of these numbers taken to the nth root.
###Example. List of numbers: 1, 3, 9, 27, 81. n = 5
# Arithmetic mean = (1 + 3 + 9 + 27 + 81) / 5 = 121 / 5 = 24.2
# Geometric mean = (1 * 3 * 9 * 27 * 81) ^ (1/5) = 59049 ^ (1/5) = 9
# Task
# You will be given a list of numbers and their arithmetic mean. However, the list is missing one number. 
# Using this information, you must figure out and return the geometric mean of the FULL LIST, including the number that's missing.
# Note: If you're using Javascript, use the root function provided for you 
# because Math.pow() doesn't handle the floating point numbers well.

def geo_mean(nums, arith_mean):
    prod = 1
    missing_num = arith_mean * (len(nums) + 1) - sum(nums)
    for i in nums:
        prod *= i
    return (prod * missing_num) ** (1/(len(nums) + 1))

# Task 2.39. Count of positives / sum of negatives
https://www.codewars.com/kata/576bb71bbbcf0951d5000044
# Given an array of integers.
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.
# If the input array is empty or null, return an empty array.
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

def count_positives_sum_negatives(arr):
    count_pos = 0
    sum_neg = 0
    for el in arr:
        if el > 0:
            count_pos += 1
        else:
            sum_neg += el
    return [count_pos, sum_neg] if len(arr) > 0 else []  

# Task 2.40. Find the middle element
https://www.codewars.com/kata/545a4c5a61aa4c6916000755
# As a part of this Kata, you need to create a function that when provided with a triplet, 
# returns the index of the numerical element that lies between the other two elements.
# The input to the function will be an array of three distinct numbers (Haskell: a tuple).
# For example:
# gimme([2, 3, 1]) => 0
# 2 is the number that fits between 1 and 3 and the index of 2 in the input array is 0.
# Another example (just to make sure it is clear):
# gimme([5, 10, 14]) => 1
# 10 is the number that fits between 5 and 14 and the index of 10 in the input array is 1.

def gimme(input_array):
    arr = sorted(input_array)
    middle = arr[1]
    return input_array.index(middle)


