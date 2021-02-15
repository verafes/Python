# Real code challenges. Set #2
# Completed_solutions 2.61-2.70

# Task 2.61. Simple Fun #37: House Numbers Sum
https://www.codewars.com/kata/58880c6e79a0a3e459000004
# A boy is walking a long way from school to his home. To make the walk more fun he decides to add up 
# all the numbers of the houses that he passes by during his walk. Unfortunately, not all of the houses have numbers written on them, 
# and on top of that the boy is regularly taking turns to change streets, so the numbers don't appear to him in any particular order.
# At some point during the walk the boy encounters a house with number 0 written on it, 
# which surprises him so much that he stops adding numbers to his total right after seeing that house.
# For the given sequence of houses determine the sum that the boy will get. 
# It is guaranteed that there will always be at least one 0 house on the path.
# Example
# For inputArray = [5, 1, 2, 3, 0, 1, 5, 0, 2], the output should be 11.
# The answer was obtained as 5 + 1 + 2 + 3 = 11.
# Input/Output
# [input] integer array inputArray
# Constraints: 5 ≤ inputArray.length ≤ 50, 0 ≤ inputArray[i] ≤ 10.
# [output] an integer

def house_numbers_sum(inp):
    zero = inp.index(0)
    return sum(inp[:zero])

# Task 2.62. Sum of Odd Cubed Numbers
https://www.codewars.com/kata/580dda86c40fa6c45f00028a/
# Find the sum of the odd numbers within an array, after cubing the initial integers. 
# The function should return undefined/None/nil/NULL if any of the values aren't numbers.
# Note: Booleans should not be considered as numbers.

def cube_odd(arr):
    ar = sum([el**3 for el in arr if type(el) == int and el%2 != 0])
    return ar if [el for el in arr if type(el) != int] == [] else None

# Task 2.63. Create Phone Number
https://www.codewars.com/kata/525f50e3b73515a6db000b83
# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
# Example:
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parentheses!

def create_phone_number(n):
    s = "".join([str(el) for el in n])
    return f'({s[:3]}) {s[3:6]}-{s[6:]}'

# Task 2.64. Removing Elements
https://www.codewars.com/kata/5769b3802ae6f8e4890009d2/
# Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.
# Example:
# my_list = ['Keep', 'Remove', 'Keep', 'Remove', 'Keep', ...]
# None of the arrays will be empty, so you don't have to worry about that!

def remove_every_other(my_list):
    return [el for i, el in enumerate(my_list) if i %2 == 0 ]
    

# Task 2.65. Count the Monkeys!
https://www.codewars.com/kata/56f69d9f9400f508fb000ba7
# You take your son to the forest to see the monkeys. You know that there are a certain number there (n), 
# but your son is too young to just appreciate the full number, he has to start counting them from 1.
# As a good parent, you will sit and count with him. Given the number (n), 
# populate an array with all numbers up to and including that number, but excluding zero.
# For example:
# monkeyCount(10) # --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# monkeyCount(1) # --> [1]

def monkey_count(n):
    return list(range(1, n+1))

# Task 2.66. Find the lucky numbers
https://www.codewars.com/kata/580435ab150cca22650001fb
# Write a function filterLucky/filter_lucky() that accepts a list of integers 
# and filters the list to only include the elements that contain the digit 7.
# For example,
# ghci> filterLucky [1,2,3,4,5,6,7,68,69,70,15,17]
# [7,70,17]
# Don't worry about bad input, you will always receive a finite list of integers.

def filter_lucky(lst):
    return [el for el in lst if '7' in str(el)]

# Task 67. Get number from string
https://www.codewars.com/kata/57a37f3cbb99449513000cd8
# Write a function which removes from string all non-digit characters and parse the remaining to number. 
# E.g: "hell5o wor6ld" -> 56

def get_number_from_string(string):
    return int("".join([el for el in string if el.isdigit()]))

# Task 2.68. Help the Fruit Guy
https://www.codewars.com/kata/557af4c6169ac832300000ba
# Our fruit guy has a bag of fruit (represented as an array of strings) where some fruits are rotten. 
# He wants to replace all the rotten pieces of fruit with fresh ones. 
# For example, given ["apple","rottenBanana","apple"] the replaced array should be ["apple","banana","apple"]. 
# Your task is to implement a method that accepts an array of strings containing fruits should returns an array of strings 
# where all the rotten fruits are replaced by good ones.
# Notes: If the array is null/nil/None or empty you should return empty array ([]).
# The rotten fruit name will be in this camelcase (rottenFruit).
# The returned array should be in lowercase.

def remove_rotten(bag_of_fruits=[]):
    return [el.replace("rotten","").lower() for el in bag_of_fruits] if bag_of_fruits else []

# Task 2.69. Word values
https://www.codewars.com/kata/598d91785d4ce3ec4f000018
# Given a string "abc" and assuming that each letter in the string has a value equal to its position in the alphabet, 
# our string will have a value of 1 + 2 + 3 = 6. This means that: a = 1, b = 2, c = 3 ....z = 26.
# You will be given a list of strings and your task will be to return the values of the strings as explained above 
# multiplied by the position of that string in the list. For our purpose, position begins with 1.
# nameValue ["abc","abc abc"] should return [6,24] because of [ 6 * 1, 12 * 2 ]. Note how spaces are ignored.
# "abc" has a value of 6, while "abc abc" has a value of 12. Now, the value at position 1 is multiplied by 1 
# while the value at position 2 is multiplied by 2.
# Input will only contain lowercase characters and spaces.

def name_value(my_list):
    abc = " abcdefghijklmnopqrstuvwxyz"
    sub = 0
    final = []
    for index, el in enumerate(my_list):
        for i in el:
            sub = sub + abc.index(i)
        final.append(sub*(index+1))
        sub = 0
    return final 

# Solution 2
def name_value(my_list):
    abc = " abcdefghijklmnopqrstuvwxyz"
    return [sum([abc.index(letter) for letter in word])*(index+1) for index, word in enumerate(my_list)]
	
# Task 2.70. Sum two arrays
https://www.codewars.com/kata/59c3e8c9f5d5e40cab000ca6
# Your task is to create a function called sum_arrays() in Python or addArrays in Javascript, 
# which takes two arrays consisting of integers, and returns the sum of those two arrays.
# The twist is that (for example) [3,2,9] does not equal 3 + 2 + 9, it would equal '3' + '2' + '9' 
# converted to an integer for this kata, meaning it would equal 329. 
# The output should be an array of the the sum in a similar fashion to the input (for example, if the sum is 341, you would return [3,4,1]). 
# Examples are given below of what two arrays should return.
# [3,2,9],[1,2] --> [3,4,1]
# [4,7,3],[1,2,3] --> [5,9,6]
# [1],[5,7,6] --> [5,7,7]
# If both arrays are empty, return an empty array.
# In some cases, there will be an array containing a negative number as the first index in the array. 
# In this case treat the whole number as a negative number. See below:
# [3,2,6,6],[-7,2,2,8] --> [-3,9,6,2] # 3266 + (-7228) = -3962

def sum_arrays(array1,array2):
    if array1 == [] and array2 == []:
        return []
    elif array2 == []:
        return array1
    elif array1 == []:
        return array2
    if array1 == [0] and array2 == [0]:
        return []
    arr1 = [str(el) for el in array1]
    arr2 = [str(el) for el in array2]
    num = int("".join(arr1)) + int("".join(arr2))
    if num < 0:
        rate = -1
        num = -num
    else: 
        rate = 1
    all = [int(el) for el in list(str(num))]
    if rate == -1:
        all[0] = -all[0]
    return all  
 
#
