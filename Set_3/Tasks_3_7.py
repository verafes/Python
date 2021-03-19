# Real code challenges. Set #3-7
# Completed_solutions 3.61-3.70

# Task 3.61. What's up next?
https://www.codewars.com/kata/542ebbdb494db239f8000046
# Given a sequence of items and a specific item in that sequence, return the item immediately following the item specified. 
# If the item occurs more than once in a sequence, return the item after the first occurence. This should work for a sequence of any type.
# When the item isn't present or nothing follows it, the function should return nil in Clojure and Elixir, 
# Nothing in Haskell, undefined in JavaScript, None in Python.
# next_item([1, 2, 3, 4, 5, 6, 7], 3) # => 4
# next_item(['Joe', 'Bob', 'Sally'], 'Bob') # => "Sally"

def next_item(xs, item):
    found = None
    for el in xs:
        if found:
            return el
        else:
            if el == item:
                found = True

# Task 3.62. Filter out the geese
https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7
# Write a function that takes an array of strings as an argument and returns a filtered array containing the same elements but with the 'geese' removed.
# The geese are any strings in the following array, which is pre-populated in your solution:
# geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
# For example, if this array were passed as an argument:
# ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]
# Your function would return the following array: ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
# The elements in the returned array should be in the same order as in the initial array passed to your function, albeit with the 'geese' removed. 
# Note that all of the strings will be in the same case as those provided, and some elements may be repeated.

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    return [el for el in birds if el not in geese]
	
# Task 3.63. Find Duplicates
https://www.codewars.com/kata/5558cc216a7a231ac9000022
# Given an array, find the duplicates in that array, and return a new array of those duplicates. 
# The elements of the returned array should appear in the order when they first appeared as duplicates.
# Note: numbers and their corresponding string representations should not be treated as duplicates (i.e., "1" != 1).
# Examples
# [1, 2, 4, 4, 3, 3, 1, 5, 3, "5"]  ==>  [4, 3, 1]
# [0, 1, 2, 3, 4, 5]                ==>  []

def duplicates(array):
    arr = [el for i, el in enumerate(array) if array.count(el) > 1 and array.index(el) != i] 
    return [el for i, el in enumerate(arr) if arr.index(el) == i]

# Task 3.64. Find numbers which are divisible by given number
https://www.codewars.com/kata/55edaba99da3a9c84000003b
# Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor. 
First argument is an array of numbers and the second is the divisor.
# Example: divisible_by([1, 2, 3, 4, 5, 6], 2) == [2, 4, 6]

def divisible_by(numbers, divisor):
    return [el for el in numbers if el%divisor == 0] 

# Task 3.65. Find the divisors!
https://www.codewars.com/kata/544aed4c4a30184e960010f4
# Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors0
# (except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime'.
# Example:
# divisors(12); #should return [2,3,4,6]
# divisors(25); #should return [5]
# divisors(13); #should return "13 is prime"

def divisors(integer):
    newlist = []
    for x in range(2, (integer//2)+1):
        if integer%x==0:
            newlist.append(x)
    if not newlist:
        return str(integer) + " is prime"
    return newlist

# Solution 2:

def divisors(integer):
    newlist = [x for x in range(2, (integer//2)+1) if integer%x==0] 
    return newlist if newlist else f"{integer} is prime"
	
# Task 3.66. Friend or Foe?
https://www.codewars.com/kata/55b42574ff091733d900002f
# Make a program that filters a list of strings and returns a list with only your friends name in it.
# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

def friend(x):
    return [i for i in x if len(i) == 4]
	
# Task 3.67. How many consecutive numbers are needed?
https://www.codewars.com/kata/559cc2d2b802a5c94700000c
# Create the function consecutive(arr) that takes an array of integers and return the minimum number of integers needed 
# to make the contents of arr consecutive from the lowest number to the highest number.
# For example: If arr contains [4, 8, 6] then the output should be 2 because two numbers need to be added to the array (5 and 7) 
# to make it a consecutive array of numbers from 4 to 8. Numbers in arr will be unique.

def consecutive(arr):
    return max(arr) - min(arr) + 1 - len(arr) if arr else 0

# Task 3.68. Holy cats
https://www.codewars.com/kata/58ebfa6ef7cda1a3d4000048
# My granny has several cats. Most of them are wicked, some are normal and some of them are the likes of ^(~_~)^ aka holy cats. 
# So my granny asked me to separate the holy cats from the rest of the crew. But I don't know how to do it. 
# Can you help me separate the holy cats from the rest? In case there are no holy cats in the group, return an empty array.

def holycats(cats):
    return [i for i in cats if not i.isalnum()]

# Task 3.69. Convert Color image to greyscale
https://www.codewars.com/kata/590ee3c979ae8923bf00095b
# An array of size N x M represents pixels of an image. Each cell of this array contains an array of size 3 with the pixel's color information: [R,G,B]
# Convert the color image, into an average greyscale image.
# The [R,G,B] array contains integers between 0 and 255 for each color.
# To transform a color pixel into a greyscale pixel, average the values of that pixel:
# p = [R,G,B] => [(R+G+B)/3, (R+G+B)/3, (R+G+B)/3]
# Note: the values for the pixel must be integers, therefore you should round floats to the nearest integer.

def color_2_grey(colors):
    res = []
    for el1 in colors:
        res.append([[round(sum(el2)/3)]*3 for el2 in el1])
    return res
 
# Task 3.70. The old switcheroo
https://www.codewars.com/kata/55d410c492e6ed767000004f
# Write a function
# vowel_2_index('this is my string') == 'th3s 6s my str15ng'
# vowel_2_index('Codewars is the best site in the world') == 'C2d4w6rs 10s th15 b18st s23t25 27n th32 w35rld'
# vowel_2_index('') == ''
# Your function should be case insensitive to the vowels.

def vowel_2_index(string):
    return ''.join([str(i+1) if el.lower() in "aeuio" else el for i, el in enumerate(string)])

#
