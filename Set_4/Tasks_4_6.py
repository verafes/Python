# Real code challenges. Set #4
# Completed_solutions 451-460

#  Task 451. Automorphic Number (Special Numbers Series #6)
https://www.codewars.com/kata/5a58d889880385c2f40000aa
# Definition
# A number is called Automorphic number if and only if its square ends in the same digits as the number itself.
# Task: Given a number determine if it Automorphic or not.

def automorphic(n):
    return "Automorphic" if str(n**2).endswith(str(n)) else "Not!!"

# Task 452. Birthday II - Presents
https://www.codewars.com/kata/5805f0663f1f9c49be00011f
# Your colleagues have been good enough(?) to buy you a birthday gift. Even though it is your birthday and not theirs, 
# they have decided to play pass the parcel with it so that everyone has an even chance of winning. 
# There are multiple presents, and you will receive one, but not all are nice... 
# One even explodes and covers you in soil... strange office. To make up for this one present is a dog! 
# Happy days! (do not buy dogs as presents, and if you do, never wrap them).
# Depending on the number of passes in the game (y), and the present you unwrap (x), return as follows:
# x == goodpresent --> return x with num of passes added to each charCode (turn to charCode, add y to each, turn back)
# x == crap || x == empty --> return string sorted alphabetically
# x == bang --> return string turned to char codes, each code reduced by number of passes and summed to a single figure
# x == badpresent --> return 'Take this back!'
# x == dog, return 'pass out from excitement y times' (where y is the value given for y).

def present(x,y):
    if x == "goodpresent":
        return "".join([chr(ord(c)+y )for c in x])
    if x == "badpresent": 
        return 'Take this back!'
    if x == "crap" or x == "empty": 
        return ''.join(sorted(x))
    if x == "bang": 
        return str(sum([(ord(ch)-y) for ch in x]))
    if x == "dog": 
        return f"pass out from excitement {y} times"

# Task 453. Borrower Speak
https://www.codewars.com/kata/57d2ba8095497e484e00002e
# The borrowers are tiny tiny fictional people. As tiny tiny people they have to be sure they aren't spotted, or more importantly, stepped on.
# As a result, the borrowers talk very very quietly. They find that capitals and punctuation of any sort lead them to raise their voices and put them in danger.
# The young borrowers have begged their parents to stop using caps and punctuation.
# Change the input text 's' to new borrower speak. Help save the next generation!

def borrow(s):
    return "".join([el.lower() for el in s if el.isalpha()])

# Task 454. Bumps in the Road
https://www.codewars.com/kata/57ed30dde7728215300005fa
# Your car is old, it breaks easily. The shock absorbers are gone and you think it can handle about 15 more bumps before it dies totally.
# Unfortunately for you, your drive is very bumpy! Given a string showing either flat road ("_") or bumps ("n"), work out if you make it home safely. 
# 15 bumps or under, return "Woohoo!", over 15 bumps return "Car Dead".

def bumps(road):
     return "Woohoo!" if road.count("n") <= 15 else "Car Dead"

# Task 455. Consecutive letters
https://www.codewars.com/kata/5ce6728c939bf80029988b57
# In this Kata, we will check if a string contains consecutive letters as they appear in the English alphabet and if each letter occurs only once.
# Rules are: (1) the letters are adjacent in the English alphabet, and (2) each letter occurs only once.
# For example: 
# solve("abc") = True, because it contains a,b,c
# solve("abd") = False, because a, b, d are not consecutive/adjacent in the alphabet, and c is missing.
# solve("dabc") = True, because it contains a, b, c, d
# solve("abbc") = False, because b does not occur once.
# solve("v") = True
# All inputs will be lowercase letters.

def solve(st):
    s = "abcdefghijklmnopqrstuvwxyz"
    return "".join(sorted(st)) in s

# Task 456. Convert a string to an array
https://www.codewars.com/kata/57e76bc428d6fbc2d500036d
# Write a function to split a string and convert it into an array of words. For example:
# "Robin Singh" ==> ["Robin", "Singh"]

def string_to_array(s):
    return [''] if s == "" else s.split()

# Task 457. Convert string to camel case
https://www.codewars.com/kata/517abf86da9663f1d2000003
# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
# Examples
# to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"
# to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"


# Task 458. Boiled Eggs
https://www.codewars.com/kata/52b5247074ea613a09000164
# You are the greatest chef on earth. No one boils eggs like you! Your restaurant is always full of guests, who love your boiled eggs. But when there is a greater order of boiled eggs, you need some time, because you have only one pot for your job. How much time do you need?
# Your Task
# Implement a function, which takes a non-negative integer, representing the number of eggs to boil. It must return the time in minutes (integer), which it takes to have all the eggs boiled.
# Rules
# you can put at most 8 eggs into the pot at once
# it takes 5 minutes to boil an egg
# we assume, that the water is boiling all the time (no time to heat up)
# for simplicity we also don't consider the time it takes to put eggs into the pot or get them out of it

import math
def cooking_time(eggs):
    return math.ceil(eggs / 8) * 5

# Task 459. Return Even Whatever You've Been Given
https://www.codewars.com/kata/5f8828d56dbd530014c1e241 
# Given integer n return even numbers as they are, but subtract 1 from odd numbers.
# Your solution should be 32 or less characters long.
# Examples
# Input = 3, Output = 2
# Input = 16, Output = 16
# Input = 45, Output = 44

def always_even(n): return n-n%2

# Task 460. [Code Golf] Return Odd No Matter What
https://www.codewars.com/kata/5f882dcc272e7a00287743f5
# Given the integer n return odd numbers as they are, but subtract 1 from even numbers.
# Note: Your solution should be 36 or less characters long.
# Examples
# Input  = 2, Output = 1
# Input  = 13, Output = 13
# Input  = 46, Output = 45

def always_odd(n): return n-(n+1)%2

#
