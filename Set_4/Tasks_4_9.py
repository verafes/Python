# Real code challenges. Set #4
# Completed_solutions 4.81-4.90

#  Task 4.81. Count the Digit
https://www.codewars.com/kata/566fc12495810954b1000030
# Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer. Square all numbers k (0 <= k <= n) between 0 and n. 
# Count the numbers of digits d used in the writing of all the k**2. Call nb_dig (or nbDig or ...) the function taking n and d as parameters and returning this count.
# Examples:
# n = 10, d = 1, the k*k are 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
# We are using the digit 1 in 1, 16, 81, 100. The total count is then 4.
# nb_dig(25, 1): the numbers of interest are
# 1, 4, 9, 10, 11, 12, 13, 14, 19, 21 which squared are 1, 16, 81, 100, 121, 144, 169, 196, 361, 441
# so there are 11 digits `1` for the squares of numbers between 0 and 25.
# Note that 121 has twice the digit 1.

def nb_dig(n, d):
    lst = list(range(n+1))
    sqr = "".join(str([k**2 for k in lst]))
    return sqr.count(str(d)) 

# Shoer solution:
def nb_dig(n, d):
	sum(str(i*i).count(str(d)) for i in range(n+1))

# Task 4.82. Counting Duplicates
https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. 
# The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice

def duplicate_count(text):
    dup = []
    for i in set(text.lower()):
        if text.lower().count(i) > 1:
            dup.append(i) 
    return len(dup)

# Task 4.83. Credit Card Mask
https://www.codewars.com/kata/5412509bd436bd33920011bc
# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. 
# However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.
# Your task is to write a function maskify, which changes all but the last four characters into '#'.
# Examples
# maskify("4556364607935616") == "############5616"
# maskify(               "1") ==                "1"
# maskify(                "") ==                 ""
# "What was the name of your first pet?"
# maskify("Skippy")                                   == "##ippy"

# return masked string
def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]

# Task 4.84. Disemvowel Trolls
https://www.codewars.com/kata/52fba66badcd10859f00097e
# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.

def disemvowel(string):
    return "".join([el for el in string if el.lower() not in "aoieu"])
	
# Task 485. First non-repeating character
https://www.codewars.com/kata/52bc74d4ac05d0945d00054e
# Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.
# For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.
# As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. 
# For example, the input 'sTreSS' should return 'T'.
# If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

def first_non_repeating_letter(string):
    res = [c for c in string if string.lower().count(c.lower()) == 1]
    return res[0] if len(res) > 0 else ""

# Task 4.86. Duplicate Encoder
https://www.codewars.com/kata/54b42f9314d9229fd6000d9c
# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, 
# or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 
# Notes. Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!

def duplicate_encode(word):
    return "".join(["(" if word.lower().count(el) == 1 else ")"  for el in word.lower()])

# Task 4.87. Find the non-unique number
https://www.codewars.com/kata/5b62031b97568072da0003db
# Given a list of numbers, a number that appears only once is considered unique. The number that appears more than once is considered non-unique.
# In this kata find the non-unique number and return a list consisting of two elements: [number, # of occurrences of the non-unique number]
# If all the numbers in the list are unique, return the string 'unique'. If the list is empty, return the empty list [].
# Examples
# ['1', '2', '3.0', '3'] -> [3, 2]
# ['0', '0.0', '0'] -> 'unique'
# [] -> []

def non_unique(lst):
    lst = [float(el.rstrip('0')) if str(el).count(".") > 0 else int(el) for el in lst]
    num = 0
    arr = []
    for el in lst:
        if el is float: 
            num = lst.count(float(el))
        else: num = lst.count(el)
        if num > 1:
            arr = [el, num]
    return arr if (len(arr) > 0) else lst if (lst == []) else 'unique'

# Task 4.88. Sum of numbers from 0 to N
https://www.codewars.com/kata/56e9e4f516bcaa8d4f001763/
# Description: We want to generate a function that computes the series starting from 0 and ending until the given number.
# Example:
# Input: > 6
# Output: 0+1+2+3+4+5+6 = 21
# nput: > -15
# Output: -15<0
# Input: > 0
# Output: 0=0


def show_sequence(n):
    serie = "+".join([str(el) for el in range(n+1)])
    return f'{n}=0' if n == 0 else f'{n}<0' if n < 0 else f'{serie} = {sum(range(n+1))}'

# Task 4.89. Find all occurrences of an element in an array
https://www.codewars.com/kata/59a9919107157a45220000e1
# Given an array (a list in Python) of integers and an integer n, find all occurrences of n in the given array and return another array containing all the index positions of n in the given array.
# If n is not in the given array, return an empty array [].
# Assume that n and all values in the given array will always be integers.
# Example: find_all([6, 9, 3, 4, 3, 82, 11], 3)  => [2, 4]

def find_all(array, n):
    return [i for i, el in enumerate(array) if el == n]

# Task 4.90. Split By Value
https://www.codewars.com/kata/5a433c7a8f27f23bb00000dc
# For an integer k rearrange all the elements of the given array in such way, that:
# all elements that are less than k are placed before elements that are not less than k;
# all elements that are less than k remain in the same order with respect to each other;
# all elements that are not less than k remain in the same order with respect to each other.
# For k = 6 and elements = [6, 4, 10, 10, 6], the output should be splitByValue(k, elements) = [4, 6, 10, 10, 6].
# For k = 5 and elements = [1, 3, 5, 7, 6, 4, 2], the output should be splitByValue(k, elements) = [1, 3, 4, 2, 5, 7, 6].

def split_by_value(k, elements):
    arr = []
    for el in elements:
        if el < k:
            arr.append(el)
    for el in elements:
        if el >= k:
            arr.append(el)
    return arr

#
