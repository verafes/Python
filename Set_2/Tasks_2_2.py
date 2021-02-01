# Real code challenges. Set #2
# Completed_solutions 2.11-20

# Task 2.11. How far will I go?
https://www.codewars.com/kata/56d46b8fda159582e100001b
# You have recently discovered that horses travel in a unique pattern - they're either running (at top speed) or resting (standing still).
# Here's an example of how one particular horse might travel:
# The horse Blaze can run at 14 metres/second for 60 seconds, but must then rest for 45 seconds.
# After 500 seconds Blaze will have traveled 4200 metres.
# Your job is to write a function that returns how long a horse will have traveled after a given time.

####Input:
# totalTime - How long the horse will be traveling (in seconds)
# runTime - How long the horse can run for before having to rest (in seconds)
# restTime - How long the horse have to rest for after running (in seconds)
# speed - The max speed of the horse (in metres/second)

def travel(total_time, run_time, rest_time, speed):
    one_round = run_time +  rest_time
    number_round = total_time//one_round
    dist_one_round = run_time * speed
    total_dist = number_round * dist_one_round
    reminder = total_time % one_round
    if reminder >= run_time:
        total_dist += dist_one_round
    else:
        total_dist += reminder * speed
    return total_dist

# Task 2.12. Cat Years, Dog Years (2)
https://www.codewars.com/kata/5a6d3bd238f80014a2000187
## I have a cat and a dog which I got as kitten / puppy.
# I forget when that was, but I do know their current ages as catYears and dogYears.
# Find how long I have owned each of my pets and return as a list [ownedCat, ownedDog]
# NOTES:
# Results are truncated whole numbers of "human" years
# Cat Years
# 15 cat years for first year
# +9 cat years for second year
# +4 cat years for each year after that
# Dog Years
# 15 dog years for first year
# +9 dog years for second year
# +5 dog years for each year after that

def owned_cat_and_dog(cat_years, dog_years):
    if cat_years < 15:
        cat = 0
    elif cat_years < 24:
        cat = 1
    else: 
        cat = 2 + ((cat_years - 24)//4)
    if dog_years < 15:
        dog = 0
    elif dog_years < 24:
        dog = 1
    else: 
        dog = 2 + ((dog_years - 24)//5)
    return [cat, dog]

# Task 2.13. Fuel Calculator
https://www.codewars.com/kata/57b58827d2a31c57720012e8
# In this kata you will have to write a function that takes litres and price_per_litre as arguments. 
# Purchases of 2 or more litres get a discount of 5 cents per litre, purchases of 4 or more litres 
# get a discount of 10 cents per litre, and so on every two litres, up to a maximum discount of 25 cents per litre. 
# But total discount per litre cannot be more than 25 cents. Return the toal cost rounded to 2 decimal places. 
#Also you can guess that there will not be negative or non-numeric inputs.

def fuel_price(litres, price_per_litre):
    if litres < 2:
        price = litres * price_per_litre
    elif litres < 4:
        price = litres * (price_per_litre - 0.05)
    elif litres < 6:
        price = litres * (price_per_litre - 0.1)
    elif litres < 8:
        price = litres * (price_per_litre - 0.15)
    elif litres < 10:
        price = litres * (price_per_litre - 0.2)
    else:
        price = litres * (price_per_litre - 0.25)
    return round(price, 2)

# Task 2.14. Check the exam
https://www.codewars.com/kata/5a3dd29055519e23ec000074
# The first input array is the key to the correct answers to an exam, like ["a", "a", "b", "d"]. 
# The second one contains a student's submitted answers.
# The two arrays are not empty and are the same length. 
# Return the score for this array of answers, giving +4 for each correct answer, -1 for each incorrect answer, 
# and +0 for each blank answer, represented as an empty string (in C the space character is used).
# If the score < 0, return 0. For example:
# checkExam(["a", "a", "b", "b"], ["a", "c", "b", "d"]) → 6
# checkExam(["a", "a", "c", "b"], ["a", "a", "b",  ""]) → 7
# checkExam(["a", "a", "b", "c"], ["a", "a", "b", "c"]) → 16
# checkExam(["b", "c", "b", "a"], ["",  "a", "a", "c"]) → 0

def check_exam(arr1,arr2):
    score = 0
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            score += 4
        elif arr1[i] != arr2[i]:
            if arr2[i] != "":
                score -= 1
    return 0 if score < 0 else score 

# Task 2.15. Factorial
https://www.codewars.com/kata/57a049e253ba33ac5e000212
# Your task is to write function factorial
# https://en.wikipedia.org/wiki/Factorial

def factorial(n):
    res = 1
    for i in range(1,n+1):
        res = res * i  
    return res

# Task 16. Factorial (2). 
https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc
# In mathematics, the factorial of a non-negative integer n, denoted by n!, 
# is the product of all positive integers less than or equal to n. 
# For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. 
# By convention the value of 0! is 1.
# Write a function to calculate factorial for a given input. 
# If input is below 0 or above 12 throw an exception of type ArgumentOutOfRangeException (C#) 
# or IllegalArgumentException (Java) or RangeException (PHP) or throw a RangeError (JavaScript) 
# or ValueError (Python) or return -1 (C).

def factorial(n):
    res = 1
    for i in range(1,n+1):
        res = res * i
    if 12 >= n >= 0:
        return res
    else:
        raise ValueError
	
# Task 2.17. Find the unique number
https://www.codewars.com/kata/585d7d5adb20cf33cb000235
# There is an array with some numbers. All numbers are equal except for one. Try to find it!
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.
# The tests contain some very huge arrays, so think about performance.

def find_uniq(arr):
    arr = sorted(arr)
    if arr[0] == arr[1]:
        return arr[-1]
    else: 
        return arr[0]   # n: unique integer in the array

# Task 2.18. Palindrome chain length
https://www.codewars.com/kata/525f039017c7cd0e1a000a26
# Number is a palindrome if it is equal to the number with digits in reversed order. 
# For example, 5, 44, 171, 4884 are palindromes and 43, 194, 4773 are not palindromes.
# Write a method palindrome_chain_length which takes a positive number and returns the number of special steps needed to obtain a palindrome. 
# The special step is: "reverse the digits, and add to the original number". If the resulting number is not a palindrome, 
# repeat the procedure with the sum until the resulting number is a palindrome.
# If the input number is already a palindrome, the number of steps is 0.
# Input will always be a positive integer.
# For example, start with 87:
# 87 + 78 = 165; 165 + 561 = 726; 726 + 627 = 1353; 1353 + 3531 = 4884
# 4884 is a palindrome and we needed 4 steps to obtain it, so palindrome_chain_length(87) == 4

def palindrome_chain_length(n):
    count = 0
    while str(n) != str(n)[::-1]:
        n += int(str(n)[::-1])
        count += 1
    return count

# Task 2.19. Halving Sum
https://www.codewars.com/kata/5a58d46cfd56cb4e8600009d
# Given a positive integer n, calculate the following sum:
# n + n/2 + n/4 + n/8 + ...
# All elements of the sum are the results of integer division.
# Example
# 25  =>  25 + 12 + 6 + 3 + 1 = 47

def halving_sum(n): 
    sum = n
    while n > 1:
        n = n//2
        sum += n
    return sum

# Task 2.20. Deodorant Evaporator
https://www.codewars.com/kata/5506b230a11c0aeab3000c1f
# This program tests the life of an evaporator containing a gas.
# We know the content of the evaporator (content in ml), the percentage of foam or gas lost every day (evap_per_day) 
#and the threshold (threshold) in percentage beyond which the evaporator is no longer useful. 
# All numbers are strictly positive.
# The program reports the nth day (as an integer) on which the evaporator will be out of use.
# Note : Content is in fact not necessary in the body of the function "evaporator", you can use it or not use it, as you wish. 
# Some people might prefer to reason with content, some other with percentages only. 
# It's up to you but you must keep it as a parameter because the tests have it as an argument.

def evaporator(content, evap_per_day, threshold):
    limit = content * threshold / 100
    days = 0
    while content > limit:
        content = content - content * evap_per_day / 100
        days += 1
    return days

#
