# Real code challenges. Set #3
# Completed_solutions 71-80

# Task 371. Complete The Pattern #1
https://www.codewars.com/kata/5572f7c346eb58ae9c000047
# Task: You have to write a function pattern which returns the following Pattern(See Pattern & Examples) upto n number of rows.
# Note:Returning the pattern is not the same as Printing the pattern.
# Rules/Note: If n < 1 then it should return "" i.e. empty string. There are no whitespaces in the pattern.
# Pattern:
# 1
# 22
# 333
# ....
# nnnnnn

def pattern(n):
    s = ""
    for i in range(1,n+1):
        s += str(i)*i+"\n"
    return s[:-1]

#Solution#2 

def pattern(n):
    return "\n".join([str(i)*i for i in range(1,n+1)])
	
# Task 372. Complete The Pattern #2
https://www.codewars.com/kata/55733d3ef7c43f8b0700007c
# You have to write a function pattern which returns the following Pattern (See Pattern & Examples) upto n number of rows.
# Note: Returning the pattern is not the same as Printing the pattern.
# Rules/Note:
# If n < 1 then it should return "" i.e. empty string.
# There are no whitespaces in the pattern.
# Pattern:
# (n)(n-1)(n-2)...4321
# (n)(n-1)(n-2)...432
# (n)(n-1)(n-2)...43
# (n)(n-1)(n-2)...4
# ...............
# (n)(n-1)(n-2)
# (n)(n-1)
# (n)

def pattern(n):
    arr = []
    for i in range(1,n+1):
        arr.append(list(range(n,i-1,-1)))
    print(arr)
    for i in range(len(arr)):
        arr[i] = "".join([str(el) for el in arr[i]])
    return "\n".join(el for el in arr)
	
# Task 373. The highest profit wins!
https://www.codewars.com/kata/559590633066759614000063
# Story
# Ben has a very simple idea to make some profit: he buys something and sells it again. Of course, this wouldn't give him any profit at all if he was simply to buy and sell it at the same price. Instead, he's going to buy it for the lowest possible price and sell it at the highest.
# Task. Write a function that returns both the minimum and maximum number of the given list/array.
# Examples
# min_max([1,2,3,4,5])   == [1,5]
# min_max([2334454,5])   == [5, 2334454]
# min_max([1])           == [1, 1]

def min_max(lst):
    return [min(sorted(lst)), max(sorted(lst))]

# Task 4. JavaScript Array Filter
https://www.codewars.com/kata/514a6336889283a3d2000001
# In Python, there is a built-in filter function that operates similarly to JS's filter. For more information on how to use this function, visit https://docs.python.org/3/library/functions.html#filter
# The solution would work like the following: get_even_numbers([2,4,5,6]) => [2,4,6]

def get_even_numbers(arr):
    return list(filter(lambda x: x % 2 == 0, arr))

# Solution #2:

def get_even_numbers(arr):
    return [el for el in arr if el%2 == 0]

# Task 375. last digits of a number
https://www.codewars.com/kata/5cd5ba1ce4471a00256930c0
# Your job is to write function last_digits(n,d) which return the last d digits of an integer n as a list. n will be from 0 to 10^10
# Examples:
# last_digits(1,1) --> [1]
# last_digits(1234,2) --> [3,4]
# last_digits(637547,6) --> [6,3,7,5,4,7]
# Special cases:
# If d > the number of digits, just return the number's digits as a list.
# If d <= 0, then return an empty list.

def solution(n,d):
    return [int(el)for el in str(n)[-d:]] if d > 0 else []

# Task 376. Sum of array singles
https://www.codewars.com/kata/59f11118a5e129e591000134
# In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice. 
# Your task will be to return the sum of the numbers that occur only once.
# For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15. Every other number occurs twice.

def repeats(arr):
    return sum(el for el in arr if arr.count(el) == 1)

# Task 7. Minimize Sum Of Array (Array Series #1)
https://www.codewars.com/kata/5a523566b3bfa84c2e00010b
# Given an array of integers , Find the minimum sum which is obtained from summing each Two integers product .
# Notes. Array/list will contain positives only. Array/list will always has even size
# Explanation: The minimum sum obtained from summing each two integers product , 5*2 + 3*4 = 22

def min_sum(arr):
    my_list = [sorted(arr)[i] for i in range(0, int(len(arr) / 2))]
    my_rev = [sorted(arr, reverse=True)[i] for i in range(0, int(len(arr) / 2))]
    return sum(my_rev[j] * my_list[j] for j in range(len(my_rev)))

#Solution #2

def min_sum(arr):
    lst = sorted(arr)
    return sum(lst[i] * lst[-i-1] for i in range(len(lst)//2))
	
# Task 378. Multiples of 3 or 5
https://www.codewars.com/kata/514b92a657cdc65150000006
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# Note: If the number is a multiple of both 3 and 5, onl

def solution(number):
    n = 0
    for i in range(1,number):
         if not i % 5 or not i % 3:
            n = n + i
    return n 

#Solution #2

def solution(number):
    return sum(i for i in range(1,number) if not i % 5 or not i % 3)


# Task 379. Character with longest consecutive repetition 
https://www.codewars.com/kata/586d6cefbcc21eed7a001155
# For a given string s find the character c (or C) with longest consecutive repetition and return: (c, l)
# where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first in order of appearance.
# For empty string return: ('', 0)

def longest_repetition(chars):
    if chars == "":
        return ('', 0)
    s = chars[0]
    for i in range(1,len(chars)):
        if chars[i] == chars[i-1]:
            s += chars[i]
        else:
            s += " " + chars[i]
    arr = s.split(" ")
    lengths = [len(el) for el in arr]
    return arr[lengths.index(max(lengths))][0], max(lengths)

# Task 380. Sum of array singles
https://www.codewars.com/kata/59f11118a5e129e591000134
# In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice. 
# Your task will be to return the sum of the numbers that occur only once.
# For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15. Every other number occurs twice.
# More examples in the test cases.

def repeats(arr):
    return sum(el for el in arr if arr.count(el) == 1)

#
