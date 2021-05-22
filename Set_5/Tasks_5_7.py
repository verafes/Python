# Real code challenges. Set #5-7
# Completed_solutions 5.61-5.70

#  Task 5.61. Debug the functions EASY
https://www.codewars.com/kata/5844a422cbd2279a0c000281/
# Should be easy, begin by looking at the code. Debug the code and the functions should work.
# There are three functions: Multiplication (x) Addition (+) and Reverse (!esreveR)

def multi(l_st):
    product = 1
    for x in l_st:
        product *= x
    return product
def add(l_st):
    return sum(l_st)
def reverse(string):
    return string[::-1]
	
# Task 5.62. Grasshopper - Function syntax debugging
https://www.codewars.com/kata/56dae9dc54c0acd29d00109a
# A student was working on a function and made some syntax mistakes while coding. Help them find their mistakes and fix them.

# Given:
def main [verb, noun]
return verb + noun

# Solution:
def main (verb, noun):
    return verb + noun

# Task 5.63. Maximum Multiple
https://www.codewars.com/kata/5aba780a6a176b029800041c
# Task. Given a Divisor and a Bound , Find the largest integer N , Such That ,
# Conditions : N is divisible by divisor
# N is less than or equal to bound
# N is greater than 0.
# Notes: The parameters (divisor, bound) passed to the function are only positive values .
# It's guaranteed that a divisor is Found .

def max_multiple(divisor, bound):
    return (bound//divisor)*divisor

# Task 5.64. Sushi-go-round (Beginner's)
https://www.codewars.com/kata/59619e4609868dd923000041
# Sam has opened a new sushi train restaurant - a restaurant where sushi is served on plates 
# that travel around the bar on a conveyor belt and customers take the plate that they like.
# Sam is using Glamazon's new visual recognition technology that allows a computer to record the number of plates at a customer's table 
# and the colour of those plates. The number of plates is returned as a string. 
# For example, if a customer has eaten 3 plates of sushi on a red plate the computer will return the string 'rrr'.
# Currently, Sam is only serving sushi on red plates as he's trying to attract customers to his restaurant. 
# There are also small plates on the conveyor belt for condiments such as ginger and wasabi - 
# the computer notes these in the string that is returned as a space ('rrr r' //denotes 4 plates of red sushi and a plate of condiment).
# Sam would like your help to write a program for the cashier's machine to read the string 
# and return the total amount a customer has to pay when they ask for the bill. The current price for the dishes are as follows:
# Red plates of sushi ('r') - $2 each, but if a customer eats 5 plates the 5th one is free.
# Condiments (' ') - free.

def total_bill(s):
    r = s.count('r')
    return (r - r//5)*2

# Task 5.65. Perimeter sequence
https://www.codewars.com/kata/589519d1f0902e01af000054
#  The first three stages of a sequence are shown.
# The blocksize is a by a and a ≥ 1.
# What is the perimeter of the nth shape in the sequence (n ≥ 1) ?

def perimeter_sequence(a, n): 
    return 4 * n * a
	
# Task 5.66. Nth Root of a Number
https://www.codewars.com/kata/5520714decb43308ea000083
# Given two numbers x and n, calculate the (positive) nth root of x.
# This means that being r = result, r^n = x.
# Examples
# Input: x=4, n=2, output: 2. The square root of 4 is 2, 2^2 = 4
# Input: x=8, n=3, output: 2. The cube root of 8 is 2 , 2^3 = 8
# Input: x=256, n=4, output: 4. The 4th root of 256 is 4 , 4^4 = 256
# Input: x=9, n=2, output: 3. The square root of 9 is 3 , 3^2 = 9
# Input: x=6.25, n=2, output: 2.5. The square root of 6.25 is 2.5 , 2.5^2 = 6.25
# Notes:
# Expect x greater than 1 × 10^19
# n will always be a positive integer.

def root(x, n):
    return x ** (1/n)

# Task 5.67. Sum of values from 1 to n inclusive { nΣn=1 }
https://www.codewars.com/kata/578a55517c77f535a8000064
# In this Kata , your job is to write a program that finds the sum of the numbers from 1 to n.
# e.g.
# total(10) => 55
# total(20) => 210
# total(34) => 595
# If you are unsure of what output you got, You can use console.log("Your output") to check

    sum = 0
    for i in range(n+1):
        sum += i;
    return sum

# Task 5.68. Easy Time Convert
https://www.codewars.com/kata/5a084a098ba9146690000969
# This kata requires you to convert minutes (int) to hours and minutes in the format hh:mm (string).
# If the input is 0 or negative value, then you should return "00:00"
# Hint: use the modulo operation to solve this challenge. The modulo operation simply returns the remainder after a division. 
# For example the remainder of 5 / 2 is 1, so 5 modulo 2 is 1.

def time_convert(num):
    if num <= 0: return "00:00"
    m = num%60
    h = num//60
    if m < 10:
        m = "0" + str(m)
    if h < 10:
        h = "0" + str(h)
    return f'{h}:{m}'

# Task 5.69. Square Roots: Approximation
 https://www.codewars.com/kata/58475cce273e5560f40000fa
# Your job here is to implement a method, approx_root in Ruby/Python/Crystal and approxRoot in JavaScript/CoffeeScript, 
# that takes one argument, n, and returns the approximate square root of that number, rounded to the nearest hundredth and computed in the following manner.# 
# Start with n = 213 (as an example).
# To approximate the square root of n, we will first find the greatest perfect square that is below or equal to n. (In this example, that would be 196, or 14 squared.) 
# We will call the square root of this number (which means sqrt 196, or 14) base.
# Then, we will take the lowest perfect square that is greater than or equal to n. (In this example, that would be 225, or 15 squared.)
# Next, subtract 196 (greatest perfect square less than or equal to n) from n. (213 - 196 = 17) We will call this value diff_gn.
# Find the difference between the lowest perfect square greater than or equal to n and 
# the greatest perfect square less than or equal to n. (225 – 196 = 29) We will call this value diff_lg.
# Your final answer is base + (diff_gn / diff_lg). In this example: 14 + (17 / 29) which is 14.59, rounded to the nearest hundredth.
# Just to clarify, if the input is a perfect square itself, you should return the exact square of the input.
# In case you are curious, the approximation (computed like above) for 213 rounded to four decimal places is 14.5862. The actual square root of 213 is 14.5945.# 
# Inputs will always be positive whole numbers. If you are having trouble understanding it, let me know with a comment, or take a look at the second group of the example cases.

def approx_root(n):
    base = int(n ** 0.5)
    lowest = base ** 2
    greatest = (base + 1) ** 2
    diff_gn = n - lowest
    diff_lg = greatest - lowest
    return round(base + diff_gn / diff_lg, 2)

# Task 5.70. Thinkful - Number Drills: Blue and red marbles
https://www.codewars.com/kata/5862f663b4e9d6f12b00003b
# You and a friend have decided to play a game to drill your statistical intuitions. The game works like this:
# You have a bunch of red and blue marbles. To start the game you grab a handful of marbles of each color and put them into the bag, 
# keeping track of how many of each color go in. You take turns reaching into the bag, guessing a color, and then pulling one marble out. 
# You get a point if you guessed correctly. The trick is you only have three seconds to make your guess, so you have to think quickly.
# You've decided to write a function, guessBlue() to help automatically calculate whether you should guess "blue" or "red". The function should take four arguments:
# -the number of blue marbles you put in the bag to start
# -the number of red marbles you put in the bag to start
# -the number of blue marbles pulled out so far (always lower than the starting number of blue marbles)
# -the number of red marbles pulled out so far (always lower than the starting number of red marbles)

def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    return (blue_start - blue_pulled)/(blue_start - blue_pulled + red_start - red_pulled)

#
