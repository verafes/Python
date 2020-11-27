# Real code challenges. Set #2
# Completed_solutions 21-30

# Task 21. Arithmetic sequence - sum of n elements
https://www.codewars.com/kata/55cb0597e12e896ab6000099
# In your class, you have started lessons about "arithmetic progression". 
# Because you are also a programmer, you have decided to write a function.
# This function, arithmetic_sequence_sum(a, r, n), should return the sum of the first (n) elements of a sequence 
# in which each element is the sum of the given integer (a), and a number of occurences of the given integer (r), 
# based on the element's position within the sequence.
# For example:
# arithmetic_sequence_sum(2, 3, 5) should return 40:
# 1     2        3          4            5
# a + (a+r) + (a+r+r) + (a+r+r+r) + (a+r+r+r+r) 
# 2 + (2+3) + (2+3+3) + (2+3+3+3) + (2+3+3+3+3) = 40

def arithmetic_sequence_sum(a, r, n):
    total = 0
    for x in range(n):
        total += a
        a += r
    return total

# Task 22. Growth of a Population
https://www.codewars.com/kata/563b662a59afc2b5120000c6
# In a small town the population is p0 = 1000 at the beginning of a year. 
# The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. 
# How many years does the town need to see its population greater or equal to p = 1200 inhabitants?

# At the end of the first year there will be: 
# 1000 + 1000 * 0.02 + 50 => 1070 inhabitants
# At the end of the 2nd year there will be: 
# 1070 + 1070 * 0.02 + 50 => 1141 inhabitants (number of inhabitants is an integer)
# At the end of the 3rd year there will be:
# 1141 + 1141 * 0.02 + 50 => 1213
# It will need 3 entire years.
# More generally given parameters:
# p0, percent, aug (inhabitants coming or leaving each year), p (population to surpass)
# the function nb_year should return n number of entire years needed to get a population greater or equal to p.
# aug is an integer, percent a positive or null number, p0 and p are positive integers (> 0)
# Examples:
# nb_year(1500, 5, 100, 5000) -> 15
# nb_year(1500000, 2.5, 10000, 2000000) -> 10
# Note: Don't forget to convert the percent parameter as a percentage in the body of your function: 
# if the parameter percent is 2 you have to convert it to 0.02.

def nb_year(p0, percent, aug, p):
    years = 0
    while p0 < p:
        p0 += p0*percent/100 + aug
        years += 1
    return years

# Task 3. Round up to the next multiple of 5
https://www.codewars.com/kata/55d1d6d5955ec6365400006d
# Given an integer as input, can you round it to the next (meaning, "higher") multiple of 5?
# Examples:
# input:    output:
# 0    ->   0
# 2    ->   5
# 3    ->   5
# 12   ->   15
# 21   ->   25
# 30   ->   30
# -2   ->   0
# -5   ->   -5
# etc.
# Input may be any positive or negative integer (including 0).
# You can assume that all inputs are valid integers.

def round_to_next5(n):
    while n%5 != 0:
        n += 1    
    return n

# Task 24. The wheat/rice and chessboard problem
https://www.codewars.com/kata/5b0d67c1cb35dfa10b0022c7
# I assume most of you are familiar with the ancient legend of the rice (but I see wikipedia suggests wheat, for some reason) problem, 
# but a quick recap for you: a young man asks as a compensation only 1 grain of rice for the first square, 2 grains for the second, 
# 4 for the third, 8 for the fourth and so on, always doubling the previous.
# Your task is pretty straightforward (but not necessarily easy): given an amount of grains, 
# you need to return up to which square of the chessboard one should count in order to get at least as many.
# As usual, a few examples might be way better than thousands of words from me:
# squares_needed(0) == 0
# squares_needed(1) == 1
# squares_needed(2) == 2
# squares_needed(3) == 2
# squares_needed(4) == 3
# Input is always going to be valid/reasonable: ie: a non negative number; extra cookie for not using a loop 
# to compute square-by-square (at least not directly) and instead trying a smarter approach [hint: some peculiar operator]; 
# a trick converting the number might also work: impress me!

def squares_needed(grains):
    squares = 0
    while 2**squares <= grains:
        squares += 1
    return squares

# 2nd solution:

def squares_needed(grains):
    grain = 1
    cell_count = 0
    while grains > 0:
        grains -= grain
        grain *= 2
        cell_count += 1
    return cell_count

# Task 25. Product of consecutive Fib numbers
https://www.codewars.com/kata/5541f58a944b85ce6d00006a
#The Fibonacci numbers are the numbers in the following integer sequence (Fn):
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
# such as
# F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.
# Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying
# F(n) * F(n+1) = prod.
# Your function productFib takes an integer (prod) and returns an array:
# [F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
# depending on the language if F(n) * F(n+1) = prod.
# If you don't find two consecutive F(m) verifying F(m) * F(m+1) = prodyou will return
# [F(m), F(m+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
# F(m) being the smallest one such as F(m) * F(m+1) > prod.

def productFib(prod):
    f1 = 0
    f2 = 1
    while f1 * f2 < prod:
        f1, f2 = f2, f1 + f2
    return [f1, f2, f1 * f2 == prod] 

# Task 26. Count the divisors of a number
https://www.codewars.com/kata/542c0f198e077084c0000c2e
#Count the number of divisors of a positive integer n.
# Random tests go up to n = 500000.
# Examples
# divisors(4)  == 3  # 1, 2, 4
# divisors(5)  == 2  # 1, 5
# divisors(12) == 6  # 1, 2, 3, 4, 6, 12
# divisors(30) == 8  # 1, 2, 3, 5, 6, 10, 15, 30

def divisors(n):
    count = 0
    for i in range (1, n+1):
        if n % i == 0:
            count += 1
    return count

# Task 27. Beginner Series #3 Sum of Numbers
https://www.codewars.com/kata/55f2b110f61eb01779000053
# Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including them too and return it. 
# If the two numbers are equal return a or b.
# Note: a and b are not ordered!
# Examples
# get_sum(1, 0) == 1   // 1 + 0 = 1
# get_sum(1, 2) == 3   // 1 + 2 = 3
# get_sum(0, 1) == 1   // 0 + 1 = 1
# get_sum(1, 1) == 1   // 1 Since both are same
# get_sum(-1, 0) == -1 // -1 + 0 = -1
# get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2

def reverse(n):
    """Returns n with all digits reversed. Assume positive n."""
    n = str(n)
    return int(n[::-1])

# Task 28. Reverser
https://www.codewars.com/kata/58069e4cf3c13ef3a6000168
Impliment the reverse function, which takes in input n and reverses it. For instance, reverse(123) should return 321. You should do this without converting the inputted number into a string.

def reverse(n):
    """Returns n with all digits reversed. Assume positive n."""
    n = str(n)
    return int(n[::-1])

# Task 29. Does my number look big in this?
https://www.codewars.com/kata/5287e858c6b5a9678200083c
# A Narcissistic Number is a positive number which is the sum of its own digits, 
# each raised to the power of the number of digits in a given base. 
# In this Kata, we will restrict ourselves to decimal (base 10).
# For example, take 153 (3 digits):
#     1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# and 1634 (4 digits):
#     1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
# The Challenge:
# Your code must return true or false depending upon whether the given number is a Narcissistic number in base 10.
# Error checking for text strings or other invalid inputs is not required, 
# only valid positive non-zero integers will be passed into the function.

def narcissistic( value ):
    sum = 0
    value = str(value)
    l = len(str(value))
    for el in value:
        sum = sum + int(el)**l
    return sum == int(value)

# Task 30. Counting sheep...
https://www.codewars.com/kata/54edbc7200b811e956000556
# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
# For example,
# [True,  True,  True,  False,
#  True,  True,  True,  True ,
#  True,  False, True,  False,
#  True,  False, False, True ,
#  True,  True,  True,  True ,
#  False, False, True,  True]
# The correct answer would be 17.
# Hint: Don't forget to check for bad values like null/undefined

def count_sheeps(sheep):
    count = 0
    for el in sheep:
        if el == True:
            count += 1
    return count


