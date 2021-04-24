# Real code challenges. Set #4-7
# Completed_solutions 4.61-4.70

#  Task 4.61. Unscrambled eggs
https://www.codewars.com/kata/55ea5650fe9247a2ea0000a7
# The string given to your function has had an "egg" inserted directly after each consonant. 
# You need to return the string before it became eggcoded.
# Example
# unscrambleEggs("Beggegeggineggneggeregg"); => "Beginner"
# //             "B---eg---in---n---er---"

def unscramble_eggs(word):
    return word.replace("egg", "")

# Task 4.62. Find the nth Digit of a Number
https://www.codewars.com/kata/577b9960df78c19bca00007e  
# Complete the function that takes two numbers as input, num and nth and return the nth digit of num (counting from right to left).
# Note
# If num is negative, ignore its sign and treat it as a positive value
# If nth is not positive, return -1
# Keep in mind that 42 = 00042. This means that findDigit(42, 5) would return 0
# Examples
# findDigit(5673, 4)     returns 5
# findDigit(129, 2)      returns 2
# findDigit(-2825, 3)    returns 8
# findDigit(-456, 4)     returns 0

def find_digit(num, nth):
    if num < 0:
        num = -num
    if nth <= 0 :
        return -1
    if nth > len(str(num)):
        return 0
    res = (str(num)[::-1])
    return int(res[nth-1])
	
# Task 4.63. Largest prime number containing n digit
https://www.codewars.com/kata/5676f07029da352ba2000065
# Just as the title suggestes :D . For example ->
# largest(1); //Should return 7
# largest(2); //Should return 97
# ....
# Do not mind the pattern as it is just an incident ! 
# And make sure to return false if the input is not an integer :D 
# This might seem simple at first, it is, but keep an eye on the performance. Go for it !

def largest(n):
    if type(n) != int or n < 1:
        return False
    x = 10**n - 3
    while pow(2, x-1, x) != 1:
        print(x)
        x -= 2
    return x

# Task 4.64. Enumerable Magic #5- True for Just One?
https://www.codewars.com/kata/54599705cbae2aa60b0011a4
# Task. Create a function called one that accepts two params:
# a sequence
# a function
# and returns true only if the function in the params returns true for exactly one (1) item in the sequence.
# Example
# one([1, 3, 5, 6, 99, 1, 3], bigger_than_ten) -> true
# one([1, 3, 5, 6, 99, 88, 3], bigger_than_ten) -> false
# one([1, 3, 5, 6, 5, 1, 3], bigger_than_ten) -> false

def one(sq, fun): 
    return len([el for el in sq if fun(el)])== 1

# Task 4.65. Put a Letter in a Column
https://www.codewars.com/kata/563d54a7329a7af8f4000059
# Create a function that takes index [0, 8] and a character. It returns a string with columns. Put character in column marked with index.
# Ex.: index = 2, character = 'B'
# | | |B| | | | | | |
#  0 1 2 3 4 5 6 7 8
# Assume that argument index is integer [0, 8]. Assume that argument character is string with one character.

def build_row_text(index, character):
    arr = ['|','|','|','|','|','|','|','|','|','|']
    lst = []
    for i, el in enumerate(arr):
        if i == index:
            el = arr[i] + character
            a = el + character
        else: 
            el = arr[i] + " "
        lst.append(el)
    lst = "".join(lst)
    return lst.rstrip()

# Task 4.66. Flatten
https://www.codewars.com/kata/5250a89b1625e5decd000413
# Write a function that flattens an Array of Array objects into a flat Array. Your function must only do one level of flattening.
# flatten [1,2,3] # => [1,2,3]
# flatten [[1,2,3],["a","b","c"],[1,2,3]]  # => [1,2,3,"a","b","c",1,2,3]
# flatten [[[1,2,3]]] # => [[1,2,3]]

def flatten(lst):
    new = []
    for el in lst:
        new.extend(el) if type(el)==list else new.append(el)
    return new

# Task 4.67. Remove duplicates from list
https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118/
# Define a function that removes duplicates from an array of numbers and returns it as a result.
# The order of the sequence has to stay the same.

def distinct(seq):
    new = []
    for el in seq:
        if el not in new:
            new.append(el)
    return(new)
	
# Task 468. Organise duplicate numbers in list
https://www.codewars.com/kata/5884b6550785f7c58f000047
# Sam is an avid collector of numbers. Every time he finds a new number he throws it on the top of his number-pile. 
# Help Sam organise his collection so he can take it to the International Number Collectors Conference in Cologne.
# Given an array of numbers, your function should return an array of arrays, where each subarray contains all the duplicates of a particular number. 
#Subarrays should be in the same order as the first occurence of the number they contain:
# group([3, 2, 6, 2, 1, 3])  >>> [[3, 3], [2, 2], [6], [1]]
# Assume the input is always going to be an array of numbers. If the input is an empty array, an empty array should be returned.

def group(arr):
    new = [] 
    for el in arr:
        if el not in new:
            new.append(el)
    return [arr.count(el)*[el] for el in new]
	
# Task 4.69. Delete occurrences of an element if it occurs more than n times
https://www.codewars.com/kata/554ca54ffa7d91b236000023 
# Enough is enough! Alice and Bob were on a holiday. Both of them took many pictures of the places they've been, 
# and now they want to show Charlie their entire collection. However, Charlie doesn't like these sessions, 
# since the motive usually repeats. He isn't fond of seeing the Eiffel tower 40 times. 
#  tells them that he will only sit during the session if they show the same motive at most N times. 
# Luckily, Alice and Bob are able to encode the motive as a number. 
# Can you help them to remove numbers such that their list contains each number only up to N times, without changing the order?
# Task
# Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering. 
# For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] 
# since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
# Example
#   delete_nth ([1,1,1,1],2) # return [1,1]
#   delete_nth ([20,37,20,21],1) # return [20,37,21]

def delete_nth(order,max_e):
    new = []
    for el in order:
        if new.count(el) < max_e:
            new.append(el)
    return new

# Task 4.70. Find The Duplicated Number in a Consecutive Unsorted List

# You are given an array of n+1 integers 1 through n. In addition there is a single duplicate integer.
# The array is unsorted.
# An example valid array would be [3, 2, 5, 1, 3, 4]. It has the integers 1 through 5 and 3 is duplicated. 
# [1, 2, 4, 5, 5] would not be valid as it is missing 3.
# You should return the duplicate value as a single integer.

def find_dup(arr):
    return [el for el in arr if arr.count(el) > 1][0]


#
