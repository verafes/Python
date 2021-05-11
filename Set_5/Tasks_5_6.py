# Real code challenges. Set #5-6
# Completed_solutions 5.51-5.60

#  Task 5.51. Sorted? yes? no? how?
https://www.codewars.com/kata/580a4734d6df748060000045
# Complete the method which accepts an array of integers, and returns one of the following:
# "yes, ascending" - if the numbers in the array are sorted in an ascending order
# "yes, descending" - if the numbers in the array are sorted in a descending order
# "no" - otherwise
# You can assume the array will always be valid, and there will always be one correct answer.

def is_sorted_and_how(arr):
    sort_a = sorted(arr)
    sort_d = sorted(arr, reverse=True)
    return 'yes, ascending' if arr == sort_a else 'yes, descending' if arr == sort_d else 'no'

# Task 5.52. Simple frequency sort
https://www.codewars.com/kata/5a8d2bf60025e9163c0000bc
# In this Kata, you will sort elements in an array by decreasing frequency of elements. 
# If two elements have the same frequency, sort them by increasing value.
# solve([2,3,5,3,7,9,5,3,7]) = [3,3,3,5,5,7,7,2,9]
# --we sort by highest frequency to lowest frequency. If two elements have same frequency, we sort by increasing value
# More examples in test cases.

def solve(arr):
    return sorted(sorted(arr), key=lambda el: arr.count(el), reverse=True)

# Task 5.53. Most common first
https://www.codewars.com/kata/59824f384df1741e05000913
# Given a string, s, return a new string that orders the characters in order of frequency.
# The returned string should have the same number of characters as the original string.
# Make your transformation stable, meaning characters that compare equal should stay in their original order in the string s.
# most_common("Hello world") => "lllooHe wrd"
# most_common("Hello He worldwrd") => "lllHeo He wordwrd"
# Explanation:
# In the hello world example, there are 3 'l'characters, 2 'o'characters, and one each of 'H', 'e', ' ', 'w', 'r', and 'd'characters. 
# Since 'He wrd'are all tied, they occur in the same relative order that they do in the original string, 'Hello world'.
# Note that ties don't just happen in the case of characters occuring once in a string. 
# See the second example, most_common("Hello He worldwrd")should return 'lllHeo He wordwrd', not 'lllHHeeoo wwrrdd'. 
# This is a key behavior if this method were to be used to transform a string on multiple passes.

def most_common(s):
    return ''.join(sorted(s, key=lambda el: s.count(el), reverse=True))

# Task 5.54. Anagram or not
https://www.codewars.com/kata/546274b0eaa31f79c9000d5d
# "Any word or phrase that exactly reproduces the letters in another order is an anagram." (Wikipedia). 
# Add numbers to this definition to be more interest.
# Examples of anagrams:
# William Shakespeare = I am a weakish speller
# silent = listen
# 12345 = 54321
# The challenge is to write the function isAnagram to return True if the word test is an anagram of the word original and False if not.
# Note: Anagrams are case insensitive, ignore all non-alphanumeric characters, input will always be two strings. 
# Also: two identical words may be considered to be an edge case of an anagram, but for this kata they are still correct anagrams.

def isAnagram(test, original):
    test = [el.lower() for el in test if el.isalnum()]
    original = [el.lower() for el in original if el.isalnum()]
    return sorted(test) == sorted(original)

# Task 5.55. Least Larger
https://www.codewars.com/kata/5f8341f6d030dc002a69d7e4
# Task
Given an array of numbers and an index, return the index of the least number larger than the element at the given index, 
# or -1 if there is no such index ( or, where applicable, Nothing or a similarly empty value ).
# Notes
# Multiple correct answers may be possible. In this case, return any one of them.
# The given index will be inside the given array.
# The given array will, therefore, never be empty.
# Example
# least_larger( [4, 1, 3, 5, 6], 0 )  ->  3
# least_larger( [4, 1, 3, 5, 6], 4 )  -> -1

def least_larger(a, i):
    if a[i] == max(a): return -1
    return a.index(min([x for x in a if x > a[i]]))

# Task 5.56. Max-min arrays
https://www.codewars.com/kata/5a090c4e697598d0b9000004
# In this Kata, you will be given an array of unique elements, and your task is to rearrange the values so that the first max value is followed by the first minimum, followed by second max value then second min value, etc.
# For example:
# solve([15,11,10,7,12]) = [15,7,12,10,11]
# The first max is 15 and the first min is 7. The second max is 12 and the second min is 10 and so on.
# More examples in the test cases.

def solve(arr):
    new_arr = []
    arr = sorted (arr)
    while arr:
        new_arr.append(arr[-1])
        arr.pop()
        if arr:
            new_arr.append(arr[0])
            del arr[0]
        else: break
    return new_arr
	
# Task 5.57. Anagram Detection
https://www.codewars.com/kata/529eef7a9194e0cbc1000255
# An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).
# Note: anagrams are case insensitive
# Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.
# Examples
# "foefet" is an anagram of "toffee"
# "Buckethead" is an anagram of "DeathCubeK"

def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())

# Task 5.58. Descending Order
https://www.codewars.com/kata/5467e4d82edf8bbf40000155
# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
# Examples:
# Input: 42145 Output: 54421
# Input: 145263 Output: 654321
# Input: 123456789 Output: 987654321

def descending_order(num):
    return int("".join(sorted(str(num), reverse = True)))

# Task 5.59. Gravity Flip
https://www.codewars.com/kata/5f70c883e10f9e0001c89673
# If you've completed this kata already and want a bigger challenge, here's the 3D version
# Bob is bored during his physics lessons so he's built himself a toy box to help pass the time. The box is special because it has the ability to change gravity.
# There are some columns of toy cubes in the box arranged in a line. The i-th column contains a_i cubes. At first, the gravity in the box is pulling the cubes downwards. When Bob switches the gravity, it begins to pull all the cubes to a certain side of the box, d, which can be either 'L' or 'R' (left or right). Below is an example of what a box of cubes might look like before and after switching gravity.
# +---+                                       +---+
# |   |                                       |   |
# +---+                                       +---+
# +---++---+     +---+              +---++---++---+
# |   ||   |     |   |   -->        |   ||   ||   |
# +---++---+     +---+              +---++---++---+
# +---++---++---++---+         +---++---++---++---+
# |   ||   ||   ||   |         |   ||   ||   ||   |
# +---++---++---++---+         +---++---++---++---+
# Given the initial configuration of the cubes in the box, find out how many cubes are in each of the n columns after Bob switches the gravity.
# Examples:
# flip('R', [3, 2, 1, 2])     =>  [1, 2, 2, 3]
# flip('L', [1, 4, 5, 3, 5])  =>  [5, 5, 4, 3, 1]

def flip(d, a):
    return sorted(a, reverse=True) if d == "L" else sorted(a) 
	

# Task 5.60. Sort the Gift Code
https://www.codewars.com/kata/52aeb2f3ad0e952f560005d3
# Happy Holidays fellow Code Warriors!
# Santa's senior gift organizer Elf developed a way to represent up to 26 gifts by assigning a unique alphabetical character to each gift. 
# After each gift was assigned a character, the gift organizer Elf then joined the characters to form the gift ordering code.
# Santa asked his organizer to order the characters in alphabetical order, 
# but the Elf fell asleep from consuming too much hot chocolate and candy canes! Can you help him out?
# Sort the Gift Code
# Write a function called sortGiftCode/sort_gift_code/SortGiftCode that accepts a string containing up to 26 unique alphabetical characters, 
# and returns a string containing the same characters in alphabetical order.
# Examples:
# sort_gift_code( 'abcdef' ) # 'abcdef'
# sort_gift_code( 'pqksuvy' ) # 'kpqsuvy'
# sort_gift_code( 'zyxwvutsrqponmlkjihgfedcba' ) # 'abcdefghijklmnopqrstuvwxyz'

def sort_gift_code(code):
    return "".join(sorted(code))
	
#
