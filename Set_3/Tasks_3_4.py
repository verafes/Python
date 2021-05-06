# Real code challenges. Set #3-4
# Completed_solutions 3.31-3.40.

# Task 3.31. Reversed Words
https://www.codewars.com/kata/51c8991dee245d7ddf00000e
# Complete the solution so that it reverses all of the words within the string passed in.
# Example:
# reverseWords("The greatest victory is that which requires no battle")
# // should return "battle no requires which that is victory greatest The"

def reverseWords(s):
    return ' '.join(reversed(s.split(' ')))

# Task 3.32. Odd or Even?
https://www.codewars.com/kata/5949481f86420f59480000e7
# Task:  Given a list of numbers, determine whether the sum of its elements is odd or even.
# Give your answer as a string matching "odd" or "even".
# If the input array is empty consider it as: [0] (array with a zero).
# Example: odd_or_even([0]) ==  "even"
# odd_or_even([0, 1, 4])    ==  "odd"
# odd_or_even([0, -1, -5])  ==  "even"

def odd_or_even(arr):
    return 'even' if sum(arr)%2 == 0 else "odd"

# Task 3.33. Powers of 2
https://www.codewars.com/kata/57a083a57cb1f31db7000028
# Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to n (inclusive).
# Examples
# n = 0  ==> [1]        # [2^0]
# n = 1  ==> [1, 2]     # [2^0, 2^1]
# n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]

def powers_of_two(n):
    a = []
    for i in range(n+1):
        a.append(2**i)
    return a

# Solution 2:

def powers_of_two(n):
    return [2**i for i in range(n+1)]

# Task 3.34. No Loops 2 - You only need one
https://www.codewars.com/kata/57cc40b2f8392dbf2a0003ce
# You will be given an array (a) and a value (x). All you need to do is check 
# whether the provided array contains the value, without using a loop.
# Array can contain numbers or strings. X can be either. Return true if the array contains the value, false if not. 
# With strings you will need to account for case.

def check(a, x): 
    return x in a

# Task 3.35. Match My Husband
https://www.codewars.com/kata/5750699bcac40b3ed80001ca
# It is 2050 and romance has long gone, relationships exist solely for practicality.
# MatchMyHusband is a website that matches busy working women with perfect house husbands. 
# You have been employed by MatchMyHusband to write a function that determines who matches!!
# The rules are... a match occurs providing the husband's "usefulness" rating is greater than or equal to the woman's "needs".
# The husband's "usefulness" is the SUM of his cooking, cleaning and childcare abilities and takes the form of an array .
# usefulness example --> [15, 26, 19]   (15 + 26 + 19) = 60
# Every woman that signs up, begins with a "needs" rating of 100. However, it's realised 
# that the longer women wait for their husbands, the more dissatisfied they become with our service. 
# They also become less picky, therefore their needs are subject to exponential decay of 15% per month.
# Given the number of months since sign up, write a function that returns "Match!" if the husband is useful enough, or "No match!" if he's not.

def match(usefulness, months):
    s = 100
    sum_use = sum(usefulness) 
    for i in range(0,months+1):
        if sum_use >= s:
            return "Match!"
        else:
            s *= 0.85
    return "No match!"
	
# Task 3.36. Simple Fun #152: Invite More Women?
https://www.codewars.com/kata/58acfe4ae0201e1708000075
# Task. King Arthur and his knights are having a New Years party. 
# Last year Lancelot was jealous of Arthur, because Arthur had a date and Lancelot did not, and they started a duel.
# To prevent this from happening again, Arthur wants to make sure that there are at least as many women as men at this year's party. 
# He gave you a list of integers of all the party goers.
# Arthur needs you to return true if he needs to invite more women or false if he is all set.

def invite_more_women(arr):
    women = arr.count(-1)
    men = arr.count(1)
    return women < men

# Task 3.37. Row Weights
https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9
# Scenario. Several people are standing in a row divided into two teams. 
# The first person goes into team 1, the second goes into team 2, the third goes into team 1, and so on.
# Task. Given an array of positive integers (the weights of the people), return a new array/tuple of two integers, 
# where the first one is the total weight of team 1, and the second one is the total weight of team 2.
# Notes. Array size is at least 1. All numbers will be positive.

def row_weights(array):
    team1 = []
    team2 = []
    for i, el in enumerate(array):
        if i%2 == 0:
            team1.append(el)
        else:
            team2.append(el)
    return sum(team1), sum(team2)
	
# Task 3.38. Manhattan Distance
https://www.codewars.com/kata/52998bf8caa22d98b800003a
# The distance formula can be used to find the distance between two points. 
# What if we were trying to walk from point A to point B, but there were buildings in the way? 
# We would need some other formula..but which?
# Manhattan Distance
# Manhattan distance is the distance between two points in a grid 
# (like the grid-like street geography of the New York borough of Manhattan) 
# calculated by only taking a vertical and/or horizontal path.
# Complete the function that accepts two points and returns the Manhattan Distance between the two points.# 
# The points are arrays or tuples containing the x and y coordinate in the grid. 
# You can think of x as the row in the grid, and y as the column.

def manhattan_distance(pointA, pointB):
    return abs(pointA[0] - pointB[0])+abs(pointA[1] - pointB[1])

# Task 3.39. Tribonacci Sequence
https://www.codewars.com/kata/556deca17c58da83c00002db
# Well met with Fibonacci bigger brother, AKA Tribonacci.
# As the name may already reveal, it works basically like a Fibonacci, 
# but summing the last 3 (instead of 2) numbers of the sequence to generate the next. 
# And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(
# So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:
# [1, 1 ,1, 3, 5, 9, 17, 31, ...]
# But what if we started with [0, 0, 1] as a signature? 
# As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence by once place, 
# you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:
# [0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
# Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function 
# that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.
# Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, 
# then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;)

def tribonacci(signature, n):
    if n < 3:
        return signature[:n]
    for i in range(3, n):
        signature.append(sum(signature[i-3:i]))
    return signature

# Task 3.40. Sums of Parts
https://www.codewars.com/kata/5ce399e0047a45001c853c2b
# Let us consider this example (array written in general format):
# ls = [0, 1, 3, 6, 10]
# Its following parts:
# ls = [0, 1, 3, 6, 10]
# ls = [1, 3, 6, 10]
# ls = [3, 6, 10]
# ls = [6, 10]
# ls = [10]
# ls = []
# The corresponding sums are (put together in a list): [20, 20, 19, 16, 10, 0]
# The function parts_sums (or its variants in other languages) will take 
# as parameter a list ls and return a list of the sums of its parts as defined above.

def parts_sums(ls):
    s = sum(ls)
    arr = [s]
    for elem in ls:
        s -= elem 
        arr.append(s)
    return arr

#