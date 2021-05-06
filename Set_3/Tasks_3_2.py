# Real code challenges. Set #3
# Completed_solutions 3.11-3.20.

# Task 3.11. Finding Remainder Without Using '%' Operator
https://www.codewars.com/kata/564f458b4d75e24fc9000041
# Write a method remainder which takes two integer arguments, dividend and divisor, 
# and returns the remainder when dividend is divided by divisor. 
# Do NOT use the modulus operator (%) to calculate the remainder!
# Assumption: Dividend will always be greater than or equal to divisor.
# Notes: 
# Make sure that the implemented remainder function works exactly the same as the Modulus operator (%).

def remainder(dividend,divisor):
    while dividend >= divisor:
        dividend -= divisor
    return dividend

# Task 3.12. Sum of Primes
https://www.codewars.com/kata/5902ea9b378a92a990000016
# A prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.
# You will be given the lower and upper limits: the program will look for any prime number 
# that exists between the lower limit to the upper limit (included).
# Your objective is to sum all the primes between the given limits.
# If the limits are primes, then they are included
# -100000 <= lower < upper <= 100000
# If lower is greater than upper, it should return 0
# Example: You are given a lower limit of 4 and an upper limit of 20.
# So the prime numbers from 4 to 20 will be: 5, 7, 11, 13, 17, 19
# and if you add them up, the result will be 72.
# sum_primes(4, 20) = 72  # 5 + 7 + 11 + 13 + 17 + 19 = 72
# sum_primes(20, 4) = 0  # since lower is greater than upper

def is_x_prime(x):
    if x <= 1:
        return False
    isPrime = True
    for i in range(2,round(x**0.5)+1):
        if x % i == 0:
            isPrime = False
            break
    return isPrime

def sum_primes(lower, upper):
    summ = 0
    for i in range(lower,upper+1):
        if is_x_prime(i) == True:
            summ  += i
    return summ
	
# Task 3.13. "Very Even" Numbers
https://www.codewars.com/kata/58c9322bedb4235468000019
# Task:
# Write a function that returns true if the number is a "Very Even" number.
# If a number is a single digit, then it is simply "Very Even" if it itself is even.
# If it has 2 or more digits, it is "Very Even" if the sum of it's digits is "Very Even".

def is_very_even_number(n):
    while n > 9:
        s = 0
        while n > 0:
            s += n % 10
            n = (n - n % 10) / 10
        n = s
    return n % 2 == 0

# Task 3.14. Simple nearest prime 
https://www.codewars.com/kata/5a9078e24a6b340b340000b8
# In this Kata, you will be given a number and your task will be to return the nearest prime number.
# solve(4) = 3. The nearest primes are 3 and 5. If difference is equal, pick the lower one. 
# solve(125) = 127

def is_prime(n):
    if n <= 1: 
        return False
    for i in range(2, round(n**0.5)+1):
        if n % i == 0: 
            return False
    return True

# Solution 2

def solve(n):
    if is_prime(n):
        return n
    b = n
    s = n
    while not is_prime(b) and not is_prime(s):
        b += 1
        s -= 1
    return s if is_prime(s) else b
	
# Task 3.15. Array plus array
https://www.codewars.com/kata/5a2be17aee1aaefe2a000151
# I'm new to coding and now I want to get the sum of two arrays...actually the sum of all their elements. I'll appreciate for your help.
# P.S. Each array includes only integer numbers. Output is a number too.

def array_plus_array(arr1,arr2):
    return sum(arr1+arr2)

# Task 3.16. Beginner - Reduce but Grow
https://www.codewars.com/kata/57f780909f7e8e3183000078
# Given a non-empty array of integers, return the result of multiplying the values together in order. 
# Example: [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

def grow(arr):
    s = 1
    for i in range(len(arr)):
        s *= arr[i]
    return s

# Task 3.17. Calculate average
https://www.codewars.com/kata/57a2013acf1fa5bfc4000921
# Write function avg which calculates average of numbers in given list.

def find_average(lst):
    return sum(lst) / len(lst) 

# Solution 2
def find_average(lst):
    return sum(lst) / len(lst) if lst else 0
	
# Task 3.18. Clean up after your dog
https://www.codewars.com/kata/57faa6ff9610ce181b000028
# You have stumbled across the divine pleasure that is owning a dog and a garden. Now time to pick up all the cr@p! :D
# Given a 2D array to represent your garden, you must find and collect all of the dog cr@p - represented by '@'.
# You will also be given the number of bags you have access to (bags), and the capactity of a bag (cap). 
# If there are no bags then you can't pick anything up, so you can ignore cap.
# You need to find out if you have enough capacity to collect all the cr@p and make your garden clean again.
# If you do, return 'Clean', else return 'Cr@p'.
# Watch out though - if your dog is out there ('D'), he gets very touchy about being watched. If he is there you need to return 'Dog!!'.

def crap(garden, bags, cap):
    c=d=j=0
    for i in range(len(garden)):
        g = garden[i]
        i += 1
        for el in g: 
            j += 1
            if el == "@":
                c += 1
            if el == "D":
                d += 1
    if d != 0: 
        return 'Dog!!'
    if bags > 0: 
        if c == 0 or c <= bags*cap:
            return 'Clean'
    return 'Cr@p'

Solution 2:

def crap(garden, bags, cap):
    g = sum(garden,[])
    if 'D' in g:
        return "Dog!!"    
    return "Clean" if g.count('@') <= bags*cap else "Cr@p"
	
# Task 3.19. Divide and Conquer
https://www.codewars.com/kata/57eaec5608fed543d6000021
# Given a mixed array of number and string representations of integers, 
# add up the string integers and subtract this from the total of the non-string integers.
# Return as a number.

def div_con(x):
    s = sum([int(el) for el in x if type(el) is str])
    total = sum([el for el in x if type(el) is int])
    return total - s

# Task 3.20. Enumerable Magic #3 - Does My List Include This?
https://www.codewars.com/kata/545991b4cbae2a5fda000158
# Create a method that accepts a list and an item, and returns true if the item belongs to the list, otherwise false.

def include(arr,item):
    return (item in arr)

