# Real code challenges. Set #2
# Completed_solutions 81-90

# Task 81. Say Me Please Operations
https://www.codewars.com/kata/5b5e0c0d83d64866bc00001d
# You have a string of numbers; starting with the third number each number is the result 
# of an operation performed using the previous two numbers.
# Complete the function which returns a string of the operations in order and separated by a comma and a space, 
# e.g. "subtraction, subtraction, addition"
# The available operations are (in this order of preference):
# 1) addition
# 2) subtraction
# 3) multiplication
# 4) division

def say_me_operations(nums):
    nums = [int(el) for el in nums.split()]
    operations = []
    for i in range(len(nums)-2):
        if nums[i] + nums[i+1] == nums[i+2]:
            operations.append("addition")
        elif nums[i] - nums[i+1] == nums[i+2]:
            operations.append("subtraction")
        elif nums[i] * nums[i+1] == nums[i+2]:
            operations.append("multiplication")
        else: 
            operations.append("division")
    return ", ".join(operations)

# Task 82. Indexed capitalization
https://www.codewars.com/kata/59cfc09a86a6fdf6df0000f1
# Given a string and an array of integers representing indices, capitalize all letters at the given indices.
# For example:
# capitalize("abcdef",[1,2,5]) = "aBCdeF"
# capitalize("abcdef",[1,2,5,100]) = "aBCdeF". There is no index 100.
# The input will be a lowercase string with no spaces and an array of digits.

def capitalize(s,ind):
    new_str = ""
    for i, el in enumerate(s):
        if i in ind:
            new_str += el.upper()
        else:
            new_str += el
    return new_str
	
# Solution 2:

def capitalize(s,ind):
    return "".join([el.upper() if i in ind else el for i, el in enumerate(s)])

# Task 83. Maximum Length Difference
https://www.codewars.com/kata/5663f5305102699bad000056
# You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. 
# Let x be any string in the first array and y be any string in the second array.
# Find max(abs(length(x) − length(y)))
# If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).

def mxdiflg(a1, a2):
    if a1 == [] or a2 == []:
        return -1
    len1 = [len(el) for el in a1]
    len2 = [len(el) for el in a2]
    max1 = max(len1)
    max2 = max(len2)
    min1 = min(len1)
    min2 = min(len2)
    dif1 = max2 - min1
    dif2 = max1 - min2
    return max(dif1,dif2)

# Solution 2
def mxdiflg(a1, a2):
    maximum = -1
    for x in a1:
        for y in a2:
            diff = abs(len(x) - len(y))
            if (diff > maximum):
                maximum = diff
    return maximum

# Task 84. Is every value in the array an array?

# Is every value in the array an array?
# This should only test the second array dimension of the array. The values of the nested arrays don't have to be arrays.
# Examples:
# [[1],[2]] => true
# ['1','2'] => false
# [{1:1},{2:2}] => false

def arr_check(arr):
    return all(type(el) == list for el in arr)


# Task 85. CSV representation of array
https://www.codewars.com/kata/5a34af40e1ce0eb1f5000036
# Create a function that returns the CSV representation of a two-dimensional numeric array. Array's length > 2.
# Example:
# input:
#    [[ 0, 1, 2, 3, 4 ],
#     [ 10,11,12,13,14 ],
#     [ 20,21,22,23,24 ],
#     [ 30,31,32,33,34 ]] 
# output:
#      '0,1,2,3,4\n'
#     +'10,11,12,13,14\n'
#     +'20,21,22,23,24\n'
#     +'30,31,32,33,34'

def toCsvText(array):
    new_arr = []
    for lst in array:
        new_arr.append(",".join([str(el) for el in lst]))
    return "\n".join(new_arr)

#Solution #2:
def toCsvText(array) :
    return "\n".join(",".join([str(el) for el in array]))


# Task 86. IPv4 Validator
https://www.codewars.com/kata/57193694938fcdfe3a001dd7
# In this kata you have to write a method to verify the validity of IPv4 addresses.
# Example of valid inputs:
# "1.1.1.1", "127.0.0.1", "255.255.255.255"
# Example of invalid input:
# "1444.23.9", "153.500.234.444", "-12.344.43.11"

def ipValidator(ip):
    ip = ip.split(".")
    ip = [el for el in ip if el.isdigit() and 0 <= int(el) <= 255 and len(str(int(el))) == len(el)] 
    return len(ip) == 4

def ipValidator(ip):    
    ip = ip.split(".")
    if len(ip) != 4: return False
    return len([int(el) for el in ip if el.isdigit() and 0<=int(el)<=255]) == 4
	
# Task 87. Largest 5 digit number in a series
https://www.codewars.com/kata/51675d17e0c1bed195000001
# In the following 6 digit number: 283910
# 91 is the greatest sequence of 2 consecutive digits.
# In the following 10 digit number: 1234567890
# 67890 is the greatest sequence of 5 consecutive digits.
# Complete the solution so that it returns the greatest sequence of five consecutive digits found within the number given. 
# The number will be passed in as a string of only digits. It should return a five digit integer. 
# The number passed may be as large as 1000 digits.

def solution(digits):
    return int(max([digits[i:i+5] for i in (range(len(digits)-4))]))

# Task 88. Multiplication table
https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08
# Your task, is to create NxN multiplication table, of size provided in parameter.
# for example, when given size is 3:
# 1 2 3
# 2 4 6
# 3 6 9
# for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]

def multiplication_table(row,col):
    new_arr = []
    for i in range(1,row+1):
        lst = list(range(i,i*col+1,i))
        new_arr.append(lst)
    return new_arr

# Solution 2 for Task 88: 

def multiplication_table(row,col):
    return [list(range(i,i*col+1,i)) for i in range(1,row+1)]

# Task 89. Multiplication Tables
https://www.codewars.com/kata/5432fd1c913a65b28f000342
# Create a function that accepts dimensions, of Rows x Columns, as parameters in order to create a multiplication table sized according to the given dimensions. 
# **The return value of the function must be an array, and the numbers must be Fixnums, NOT strings.
# Example: multiplication_table(3,3)
# 1 2 3
# 2 4 6
# 3 6 9
# -->[[1,2,3],[2,4,6],[3,6,9]]
# Each value on the table should be equal to the value of multiplying the number in its first row times the number in its first column.

def multiplication_table(size):
    return [list(range(i, i*size +1, i)) for i in range(1,size+1)]

# Task 90. Maximum Product
https://www.codewars.com/kata/5a4138acf28b82aa43000117
# Task. Given an array of integers , Find the maximum product obtained from multiplying 2 adjacent numbers in the array.
# adjacentElementsProduct([1, 2, 3]); ==> return 6

def adjacent_element_product(array):
    return max([array[i]*array[i-1] for i in range(1, len(array))] )

