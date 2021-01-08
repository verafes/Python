# Real code challenges. Set #3
# Completed_solutions 1-10.

# Task 301. Sum of prime-indexed elements
https://www.codewars.com/kata/59f38b033640ce9fc700015b
# In this Kata, you will be given an integer array and your task is to return the sum of elements occupying prime-numbered indices.
# The first element of the array is at index 0.

def isprime(num):
    if num <= 1:
        return False
    for i in range(2, num//2+1):
        if num % i == 0:
            return False
    return True
def total(arr):
    return sum([el for i, el in enumerate(arr) if isprime(i)])

# Task 302. Testing 1-2-3

# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
# Write a function which takes a list of strings and returns each line prepended by the correct number.
# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

def number(lines):
    return [f'{i+1}: {el}' for i, el in enumerate (lines)]

# Task 303. Title Case
https://www.codewars.com/kata/5202ef17a402dd033c000009
# A string is considered to be in title case if each word in the string is either (a) capitalised 
# (that is, only the first letter of the word is in upper case) or (b) considered to be an exception 
# and put entirely into lower case unless it is the first word, which is always capitalised.
# Write a function that will convert a string into title case, given an optional list of exceptions (minor words). 
# The list of minor words will be given as a string with each word separated by a space. 
# Your function should ignore the case of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.

###Arguments (Haskell)
# First argument: space-delimited list of minor words that must always be lowercase except for the first word in the string.
# Second argument: the original string to be converted.

def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])

# Task 304. Grasshopper - Summation
https://www.codewars.com/kata/55d24f55d7dd296eb9000030
# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
# For example:  summation(2) -> 3  - > 1 + 2
# summation(8) -> 36 -> 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

def summation(num):
    return sum(i for i in range(1, num+1))
	
# Task 305. Persistent Bugger
https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
# which is the number of times you must multiply the digits in num until you reach a single digit.
# For example:
#  persistence(39) => 3 # Because 3*9 = 27, 2*7 = 14, 1*4=4
#                       # and 4 has only one digit.
# persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
#                       # 1*2*6 = 12, and finally 1*2 = 2.
# persistence(4) => 0   # Because 4 is already a one-digit number.

def persistence(n):
    count=0
    while len(str(n))>1:
        p=1
        count += 1
        for i in str(n):
            p=p*int(i)
        n=p
    return count
	
# Task 306. Reverse Factorials
https://www.codewars.com/kata/58067088c27998b119000451
# I'm sure you're familiar with factorials – that is, the product of an integer and all the integers below it.
# For example, 5! = 120, as 5 * 4 * 3 * 2 * 1 = 120
# Your challenge is to create a function that takes any number and returns the number that it is a factorial of. So, if your function receives 120, it should return "5!" (as a string).
# Of course, not every number is a factorial of another. In this case, your function would return "None" (as a string).
# Examples
# 120 will return "5!"
# 24 will return "4!"
# 150 will return "None"

def reverse_factorial(num):
    n = f = 1
    while f < num:
        n += 1
        f = f * n
    return f"{n}!" if f == num else "None"

# Task 307. Single digit
https://www.codewars.com/kata/5a7778790136a132a00000c1
# The goal of this Kata is to reduce the passed integer to a single digit (if not already) by converting the number to binary, taking the sum of the binary digits, and if that sum is not a single digit then repeat the process.
# n will be an integer such that 0 < n < 10^20
# If the passed integer is already a single digit there is no need to reduce
# For example given 5665 the function should return 5:
# 5665 --> (binary) 1011000100001
# 1011000100001 --> (sum of binary digits) 5

def single_digit(n):
    while (n) > 9:
        n = bin(n).count("1")
    return n
	
# Task 308. Square(n) Sum
https://www.codewars.com/kata/515e271a311df0350d00000f
# Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

def square_sum(numbers):
    return sum(x**2 for x in numbers)

# Task 309. Squares sequence
https://www.codewars.com/kata/5546180ca783b6d2d5000062
# Complete the function that returns an array of length n, starting with the given number x and the squares of the previous number. 
# If n is negative or zero, return an empty array/list.
# Examples
# 2, 5  -->  [2, 4, 16, 256, 65536]
# 3, 3  -->  [3, 9, 81]

def squares(x, n):
    if x <= 0 or n <= 0:
        return []
    arr = [x]
    while len(arr) < n:
        x = x**2
        arr.append(x)
    return arr
	
# Solution 2:
def squares(x,n):
    return [x**(2**i) for i in range(n)]

# Task 310. Subtract the Sum
https://www.codewars.com/kata/56c5847f27be2c3db20009c3
# Complete the function which get an input number n such that n >= 10 and n < 10000, then:
# Sum all the digits of n.
# Subtract the sum from n, and it is your new n.
# If the new n is in the list below return the associated fruit, otherwise return back to task 1.
# Example
# n = 325
# sum = 3+2+5 = 10
# n = 325-10 = 315 (not in the list)
# sum = 3+1+5 = 9
# n = 315-9 = 306 (not in the list)
# sum = 3+0+6 = 9
# n =306-9 = 297 (not in the list)
# . .
# . ...until you find the first n in the list below.
# There is no preloaded code to help you. This is not about coding skills; think before you code

def subtract_sum(n):
    n -= sum(int(digit) for digit in str(n))

    while n > 100:
        n -= sum(int(digit) for digit in str(n))

    if n % 9 == 0: return "apple"
    elif n in [1, 3, 24, 26, 47, 49, 68, 70, 91, 93]: return "kiwi"
    elif n in [2, 21, 23, 42, 44, 46, 65, 67, 69, 88]: return "pear"
    elif n in [4, 6, 25, 29, 48, 50, 71, 73, 92, 94, 96]: return "banana"
    elif n in [5, 7, 28, 30, 32, 51, 53, 74, 76, 95, 97]: return "melon"
    elif n in [8, 10, 12, 31, 33, 52, 56, 75, 77, 79, 98, 100]: return "pineapple"
    elif n in [11, 13, 34, 55, 57, 59, 78, 80]: return "cucumber"
    elif n in [14, 16, 35, 37, 39, 58, 60, 83]: return "orange"
    else: return "cherry"

# 

