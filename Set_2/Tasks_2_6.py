# Real code challenges. Set #2
# Completed_solutions 2.51-2.60

# Task 2.51. Rock Off!
https://www.codewars.com/kata/5b097da6c3323ac067000036   
# Alice and Bob have participated to a Rock Off with their bands. A jury of true metalheads rates the two challenges, 
# awarding points to the bands on a scale from 1 to 50 for three categories: Song Heaviness, Originality, and Members' outfits.
# For each one of these 3 categories they are going to be awarded one point, should they get a better judgement from the jury. 
# No point is awarded in case of an equal vote.
# You are going to receive two arrays, containing first the score of Alice's band and then those of Bob's. 
# Your task is to find their total score by comparing them in a single line.
# Example:
# Alice's band plays a Nirvana inspired grunge and has been rated 20 for Heaviness, 32 for Originality and only 18 for Outfits. 
# Bob listens to Slayer and has gotten a good 48 for Heaviness, 25 for Originality and a rather honest 40 for Outfits.
# The total score should be followed by a colon : and by one of the following quotes: if Alice's band wins: 
# Alice made "Kurt" proud! if Bob's band wins: Bob made "Jeff" proud! if they end up with a draw: that looks like a "draw"! Rock on!
# The solution to the example above should therefore appear like '1, 2: Bob made "Jeff" proud!'.

def solve(a, b):
    countA = 0 
    countB = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            countA += 1
        elif a[i] < b[i]:
            countB += 1
    return f'{countA}, {countB}: that looks like a "draw"! Rock on!' if countA == countB else f'{countA}, {countB}: Alice made "Kurt" proud!' if countA > countB else f'{countA}, {countB}: Bob made "Jeff" proud!'

# Task 2.52. Simple consecutive pairs
https://www.codewars.com/kata/5a3e1319b6486ac96f000049
# In this Kata your task will be to return the count of pairs that have consecutive numbers as follows:
# pairs([1,2,5,8,-4,-3,7,6,5]) = 3
# The pairs are selected as follows [(1,2),(5,8),(-4,-3),(7,6),5]
# --the first pair is (1,2) and the numbers in the pair are consecutive; Count = 1
# --the second pair is (5,8) and are not consecutive
# --the third pair is (-4,-3), consecutive. Count = 2
# --the fourth pair is (7,6), also consecutive. Count = 3. 
# --the last digit has no pair, so we ignore.
# More examples in the test cases.

def pairs(ar):
    count = 0
    for i in range(0,len(ar)-1,2):
        if ar[i]+1 == ar[i+1] or ar[i]-1 == ar[i+1]:
            count += 1
    return count

# Task 2.53. IQ Test
https://www.codewars.com/kata/552c028c030765286c00007d
# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers 
# differs from the others. Bob observed that one number usually differs from the others in evenness. 
# Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, 
# and return a position of this number.
# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)
##Examples :
# iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even
# iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd

ef iq_test(numbers):
    arr = numbers.split()
    even = 0
    odd = 0
    for el in arr: 
        if int(el)%2 == 0:
            even += 1
        else:
            odd += 1
    if even == 1:
        for i, el in enumerate(arr):
            if int(el) % 2 == 0:
                return i+1
    else: 
        for i, el in enumerate(arr):
            if int(el) % 2 != 0:
                return i+1
#
# Task 2.54. Beginner - Lost Without a Map
https://www.codewars.com/kata/57f781872e3d8ca2a000007e
# Given an array of integers, return a new array with each value doubled.
# For example: [1, 2, 3] --> [2, 4, 6]
# For the beginner, try to use the map method - it comes in very handy quite a lot so is a good one to know.

def maps(a):
    return [el * 2 for el in a]

# Task 2.55. Sum of array's elements
https://www.codewars.com/kata/58f475735e78fde4a2000011
# You will be given an array of integers. You will need to return an integer that is the sum of the elements multiplied by an incrementing constant. 
# The first element in the array is multiplied by 1, the second element multiplied by 2, etc:
# a, b, c, d, ... => 1*a + 2*b + 3*c + 4*d + ...
# Examples
# 8, 5, 4        =>  30    # 1*8 + 2*5 + 3*4 = 30
# 4, 9           =>  22    # 1*4 + 2*9 = 22
# 5, 4, 3, 2, 1  =>  35    # 1*5 + 2*4 + 3*3 + 4*2 + 5*1 = 35

def sum1(array):
    return sum([(i+1)*el for i, el in enumerate(array)])

# Task 2.56. Array element parity
https://www.codewars.com/kata/5a092d9e46d843b9db000064
# In this Kata, you will be given an array of integers whose elements have both a negative and a positive value, 
# except for one integer that is either only negative or only positive. Your task will be to find that integer.
# Examples:
# [1, -1, 2, -2, 3] => 3
# 3 has no matching negative appearance
# [-3, 1, 2, 3, -1, -4, -2] => -4
# -4 has no matching positive appearance
# [1, -1, 2, -2, 3, 3] => 3
# (the only-positive or only-negative integer may appear more than once)

def solve(arr):
    return [el for el in arr if -el not in arr ][0]

# Task 2.57. Bingo ( Or Not )
https://www.codewars.com/kata/5a1ee4dfffe75f0fcb000145
# For this game of BINGO, you will receive a single array of 10 numbers from 1 to 26 as an input. 
# Duplicate numbers within the array are possible.
# Each number corresponds to their alphabetical order letter (e.g. 1 = A. 2 = B, etc). 
# Write a function where you will win the game if your numbers can spell "BINGO". 
# They do not need to be in the right order in the input array). Otherwise you will lose. 
# Your outputs should be "WIN" or "LOSE" respectively.

def bingo(array): 
    bingo = [2,7,9,14,15]
    return "WIN" if len([el for el in bingo if el in array]) == len(bingo) else "LOSE"

# Task 2.58. Even odd disparity
https://www.codewars.com/kata/59c62f1bdcc40560a2000060
# Given an array, return the difference between the count of even numbers and the count of odd numbers. 0 will be considered an even number.
# For example:
# solve([0,1,2,3]) = 0 because there are two even numbers and two odd numbers. Even - Odd = 2 - 2 = 0.  
# Let's now add two letters to the last example:
# solve([0,1,2,3,'a','b']) = 0. Again, Even - Odd = 2 - 2 = 0. Ignore letters. 
# The input will be an array of lowercase letters and numbers only.
# In some languages (Haskell, C++, and others), input will be an array of strings:
# solve ["0","1","2","3","a","b"] = 0 

def solve(a):
    return sum([1 if el%2 == 0 else -1 for el in a if type(el) == int])

# Task 2.59. Small enough? - Beginner
https://www.codewars.com/kata/57cc981a58da9e302a000214
# You will be given an array and a limit value. You must check that all values in the array are below or equal to the limit value. 
# If they are, return true. Else, return false.
# You can assume all values in the array are numbers.

def small_enough(array, limit):
    return max(erray) <= limit

# Solution #2:

def small_enough(array, limit):
    return [el for el in array if el <= limit] == array
 
# Task 2.60. Peak array index
https://www.codewars.com/kata/5a61a846cadebf9738000076/
# Given an array of ints, return the index such that the sum of the elements to the right of that index equals the sum of the elements 
# to the left of that index. If there is no such index, return -1. If there is more than one such index, return the left-most index.
# For example:
# peak([1,2,3,5,3,2,1]) = 3, because the sum of the elements at indexes 0,1,2 == sum of elements at indexes 4,5,6. We don't sum index 3.
# peak([1,12,3,3,6,3,1]) = 2
# peak([10,20,30,40]) = -1

def peak(arr):
    ar = [i for i in range(len(arr)) if sum(arr[:i]) == sum(arr[i+1:]) ]
    return ar[0] if len(ar) > 0 else -1 

