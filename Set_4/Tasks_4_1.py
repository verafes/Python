# Real code challenges. Set #4-1
# Completed_solutions 4.01-4.10

#  Task 4.01. Square Every Digit
https://www.codewars.com/kata/546e2562b03326a88e000020
# Task: to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer

def square_digits(num):
    return int("".join([str(int(x)**2) for x in str(num)]))

# Task 4.02. Series of integers from m to n
https://www.codewars.com/kata/5841f680c5c9b092950001ae
# Write a function that accepts two arguments and generates a sequence containing the integers from the first argument to the second inclusive.
# Input: Pair of integers greater than or equal to 0. The second argument will always be greater than or equal to the first.
# Example: generate_integers(2, 5) # --> [2, 3, 4, 5]

def generate_integers(m, n): 
    return [el for el in range(m, n+1)]

# Solution #2:

def generate_integers(m, n): 
    return list(range(m,n+1))
	
# Task 4.03. Show multiples of 2 numbers within a range
https://www.codewars.com/kata/583989556754d6f4c700018e
# Print all numbers up to 3rd parameter which are multiple of both 1st and 2nd parameter.
# Python, Javascript, Java versions: return results in a list/array
# NOTICE: Do NOT worry about checking zeros or negative values.
# To find out if 3rd parameter (the upper limit) is inclusive or not, check the tests, it differs in each translation

def multiples(s1,s2,s3):
    return [el for el in range (s1,s3) if el % s1 == 0 and el % s2 == 0]

# Task 4.04. Find longest sequence of an element in array
https://www.codewars.com/kata/5f8dd79aa962b600335f7577
# Write a function longest_sequence that takes in an array and value as arguments. 
# Return the length of the longest sequence of the value in the array as an integer.
# For example, if the array was [1, 0, 1, 1, 0, 0, 1, 1, 1] and the value to check was 1, then you would return 3.
# There does not need to be a strict longest sequence, if two sequences are tied, return one of their lengths. 
# If the value doesn't occur in the array, return 0.

def longest_sequence(arr, elem):
    if arr == [] or elem not in arr: return 0 
    lst = []
    for el in arr:
        if el == elem:
            lst.append(str(el))
        else:
            lst.append(" ")
    return max([len(i)/len(str(elem)) for i in ("".join(lst)).split()])  

# Task 4.05. Prime Primes  
https://www.codewars.com/kata/57ba58d68dcd97e98c00012b
# Define a "prime prime" number to be a rational number written as one prime number over another prime number: primeA / primeB (e.g. 7/31)
# Given a whole number N, generate the number of "prime prime" rational numbers less than 1, using only prime numbers between 0 and N (non inclusive).
# Return the count of these "prime primes", and the integer part of their sum.
# Example: N = 6
# The "prime primes" less than 1 are:
# 2/3, 2/5, 3/5               # count: 3
# 2/3 + 2/5 + 3/5 = 1.6667    # integer part: 1
# Thus, the function should return 3 and 1.

def is_prime(n):
    if n <= 1 :
        return False
    for i in range(2,int(n**0.5+1)):
        if n % i == 0:
            return False
    return True    

def prime_primes(N):
    count = 0 
    s = 0
    arr = [i for i in range(2, N) if is_prime(i)]
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            s += arr[i]/arr[j]
            count += 1
    return  count, int(s)

# Task 4.06. Transform To Prime  
https://www.codewars.com/kata/5a946d9fba1bb5135100007c
# Task : Given a List [] of n integers , find minimum number to be inserted in a list, so that sum of all elements of list should equal the closest prime number .
# Notes: List size is at least 2 .
# List's numbers will only positives (n > 0) .
# Repetition of numbers in the list could occur .
# The newer list's sum should equal the closest prime number .
# Input >> Output Examples: 
# 1- minimumNumber ({3,1,2}) ==> return (1)
# Explanation: Since , the sum of the list's elements equal to (6), the minimum number to be inserted to transform the sum to prime number is (1), 
# which will make *the sum of the List** equal the closest prime number (7)* .
# 2-  minimumNumber ({2,12,8,4,6}) ==> return (5)
# Explanation: Since , the sum of the list's elements equal to (32), the minimum number to be inserted to transform the sum to prime number is (5), 
# which will make *the sum of the List** equal the closest prime number (37)* .
# 3- minimumNumber ({50,39,49,6,17,28}) ==> return (2)
# Explanation: Since , the sum of the list's elements equal to (189), the minimum number to be inserted to transform the sum to prime number is (2), 
# which will make *the sum of the List** equal the closest prime number (191)* .

def is_prime(n):
    if n <= 1: return False
    for i in range(2, round(n**0.5)+1):
        if n % i == 0: return False
    return True

def minimum_number(num):
    s = sum(num)
    i = 1
    count = 0
    while not is_prime(s):
        s += 1 
        count += 1
    return count

# Task 4.07. Next Prime
https://www.codewars.com/kata/58e230e5e24dde0996000070
# You will get a numbern (>= 0) and your task is to find the next prime number.
# Make sure to optimize your code: there will numbers tested up to about 10^12.
# Examples: 5   =>  7, 12  =>  13

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5+1)):
        if n % i == 0:
            return False
    return True
    
def next_prime(n):
    prime = n
    found = False
    while not found: 
        prime = prime + 1
        if is_prime(prime) == True: 
            found = True
    return prime 
	
# Task 4.08. Pack Some Chocolates
https://www.codewars.com/kata/5f5daf1a209a64001183af9b
# Make Chocolates. Haloween is around the corner and we have to distribute chocolates. We need to assemble a parcel of goal grams of chocolates. 
# The goal can be assumed to be always a positive integer value.
# There are small chocolates (2 grams each) and big chocolates (5 grams each)
# To reach the goal, the chocolates (big and small) must be used as-is, meaning, the chocolates cannot be broken into smaller pieces
# Maximize the use of big chocolates that are available to achieve the desired goal. And only then should you proceed to use the small chocolates.
# NOTE: "Maximize" does not imply you have to use all the available big chocolates before using the small chocolates
# For example, consider the goal of 6, and big=1, small=3. Using the existing one big chocolate, it is not possible to achieve the remainder of the weight of 1. 
# Therefore, avoid using the big chocolate. Use the existing 3 small chocolates and achieve the goal.
# Determine the number of small chocolates that are required to achieve the desired parcel weight.
# Write a function make_chocolates that will accept three integer values as arguments, in the following order:
# small -> number of small chocolates available
# big -> number of big chocolates available
# goal -> the desired weight of the final parcel
# The function should return the number of small chocolates required to achieve the goal. 
# The function should return -1 only if the goal cannot be achieved by any possible combination of big chocolates and small chocolates.
# Example: make_chocolates (4, 1, 13) => 4  
# make_chocolates (4, 1, 14) => -1  
# make_chocolates (2, 1, 7) => 1  
# using the big chocolate prevents goal accomplishment, therefore don't use it!
# make_chocolates (3, 1, 6) => 3  

def make_chocolates(small, big, goal):
    for  s in range(0, small+1):
        for b in range(0, big+1):
            if goal == s * 2 + b * 5:
                return s
    return -1

# Task 4.09. Multiply the number
https://www.codewars.com/kata/5708f682c69b48047b000e07
# Jack really likes his number five: 
# the trick here is that you have to multiply each number by 5 raised to the number of digits of each numbers, so, for example:
# multiply(3)==15
# multiply(10)==250
# multiply(200)==25000
# multiply(0)==0
# multiply(-3)==-15

def multiply(n):
    l = len(str(n)) if n > 0 else len(str(-n))
    return 5**l*n

# Task 4.10. Calculator: Coin Combination
https://www.codewars.com/kata/564d0490e96393fc5c000029
# The function takes cents value (int) and needs to return the minimum number of coins combination of the same value.
# The function should return an array where
# coins[0] = pennies ==> $00.01
# coins[1] = nickels ==> $00.05
# coins[2] = dimes ==> $00.10
# coins[3] = quarters ==> $00.25
# So for example: coinCombo(6) --> [1, 1, 0, 0]

def coin_combo(cents):
    lst = []
    for x in [25, 10, 5, 1]:
        lst.append(cents // x)
        cents %= x
    return [el for el in reversed(lst)] 
