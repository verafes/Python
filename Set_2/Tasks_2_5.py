# Real code challenges. Set #2
# Completed_solutions 41-50


# Task 41. How many animals are there?
https://www.codewars.com/kata/593406b8f3d071d83c00005d
# From a sentence, deduce the total number of animals.
# For example :
# "I see 3 zebras, 5 lions and 6 giraffes." The answer must be 14
# "Mom, 3 rhinoceros and 6 snakes come to us!" The answer must be 9

def remove_duplicate_words(s):
    arr = s.split()
    new_arr = []
    for el in arr:
        if not el in new_arr:
            new_arr.append(el)
    return " ".join(new_arr)
	
# Task 42. Plus - minus - plus - plus - ... - Count
https://www.codewars.com/kata/5bbb8887484fcd36fb0020ca
# Count how often sign changes in array.
#result: number from 0 to ... . Empty array returns 0
#example: # const arr = [1, -3, -4, 0, 5];
#/*
#| elem | count |
#|------|-------|
#|  1   |  0    |
#| -3   |  1    |
#| -4   |  1    |
#|  0   |  2    |
#|  5   |  2    |
#*/
#catchSignChange(arr) == 2;

def catch_sign_change(lst):
    count = 0
    print(lst)
    for i in range(len(lst)-1):
        if lst[i] >= 0 and lst[i+1] < 0 or lst[i] < 0 and lst[i+1] >= 0:
            count += 1
    return count

# Task 43. Take a Ten Minute Walk
https://www.codewars.com/kata/54da539698b8a2ad76000228
# You live in the city of Cartesia where all roads are laid out in a perfect grid. 
# You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. 
# The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button 
# it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). 
# You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, 
#so create a function that will return true if the walk the app gives you will take you exactly ten minutes 
#(you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.
# Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). 
#It will never give you an empty array (that's not a walk, that's standing still!).

def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    if walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e') and len(walk) == 10:
        return True
    return False

# Task 44. Sentence Smash
https://www.codewars.com/kata/53dc23c68a0c93699800041d
# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. 
# You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. 
# Be careful, there shouldn't be a space at the beginning or the end of the sentence!
# Example
#['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'

def smash(words):
    return " ".join(words)

# Task 45. 
https://www.codewars.com/kata/5b39e3772ae7545f650000fc
# Your task is to remove all duplicate words from a string, leaving only single (first) words entries.
# Example:
# Input: 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
# Output: 'alpha beta gamma delta'

def remove_duplicate_words(s):
    arr = s.split()
    new_arr = []
    for el in arr:
        if not el in new_arr:
            new_arr.append(el)
    return " ".join(new_arr)

# Task 46. Average Array
https://www.codewars.com/kata/596f6385e7cd727fff0000d6
# Create a function that takes a 2D array as an input, and outputs another array that contains the average values for the numbers in the nested arrays at the corresponding indexes.
# Note: the function should also work with negative numbers and floats.
# Examples
# [ [1, 2, 3, 4], [5, 6, 7, 8] ]  ==>  [3, 4, 5, 6]
# 1st array: [1, 2, 3, 4]
# 2nd array: [5, 6, 7, 8]
#             |  |  |  |
#             v  v  v  v
# average:   [3, 4, 5, 6]
An# d another one:
# [ [2, 3, 9, 10, 7], [12, 6, 89, 45, 3], [9, 12, 56, 10, 34], [67, 23, 1, 88, 34] ]  ==>  [22.5, 11, 38.75, 38.25, 19.5]
# 1st array: [  2,   3,    9,   10,    7]
# 2nd array: [ 12,   6,   89,   45,    3]
# 3rd array: [  9,  12,   56,   10,   34]
# 4th array: [ 67,  23,    1,   88,   34]
#               |    |     |     |     |
#               v    v     v     v     v
# average:   [22.5, 11, 38.75, 38.25, 19.5]

def avg_array(arrs):
    m = []
    for x in range(len(arrs[0])):
        total = 0
        for el in arrs:
            total += el[x]
        average = total/len(arrs)
        m.append(average) 
    return m
	
# Task 47. Basic Sequence Practice
https://www.codewars.com/kata/5436f26c4e3d6c40e5000282
# A sequence or a series, in mathematics, is a string of objects, like numbers, that follow a particular pattern. 
# The individual elements in a sequence are called terms. A simple example is 3, 6, 9, 12, 15, 18, 21, ..., 
#where the pattern is: "add 3 to the previous term".
# In this kata, we will be using a more complicated sequence: 0, 1, 3, 6, 10, 15, 21, 28, ... 
#This sequence is generated with the pattern: "the nth term is the sum of numbers from 0 to n, inclusive".
#[ 0,  1,    3,      6,   ...]
#  0  0+1  0+1+2  0+1+2+3
# Your Task: Complete the function that takes an integer n and returns a list/array of length abs(n) + 1 of the arithmetic series explained above. 
# Whenn < 0 return the sequence with negative terms.
# Examples: 
#  5  -->  [0,  1,  3,  6,  10,  15]
# -5  -->  [0, -1, -3, -6, -10, -15]
#  7  -->  [0,  1,  3,  6,  10,  15,  21,  28]

def sum_of_n(n):
    step = 0
    arr = []
    el = 0
    sign = -1 if n < 0 else 1
    for i in range(n*sign+1):
        arr.append(el*sign)
        step += 1
        el += step
    return arr

# Task 48. Custom FizzBuzz Array
https://www.codewars.com/kata/5355a811a93a501adf000ab7
# Write a function that returns a (custom) FizzBuzz sequence of the numbers 1 to 100.
# The function should be able to take up to 4 arguments:
# The 1st and 2nd arguments are strings, "Fizz" and "Buzz" by default;
# The 3rd and 4th arguments are integers, 3 and 5 by default.
# Thus, when the function is called without arguments, it will return the classic FizzBuzz sequence up to 100:
# [ 1, 2, "Fizz", 4, "Buzz", "Fizz", 7, ... 14, "FizzBuzz", 16, 17, ... 98, "Fizz", "Buzz" ]
# When the function is called with (up to 4) arguments, it should return a custom FizzBuzz sequence, for example:
# ('Hey', 'There')      -->  [ 1, 2, "Hey", 4, "There", "Hey", ... ]
# ('Foo', 'Bar', 2, 3)  -->  [ 1, "Foo", "Bar", "Foo", 5, "FooBar", 7, ... ]

def fizz_buzz_custom(string_one="Fizz", string_two="Buzz", num_one=3, num_two=5): 
    arr = list(range(1,101))
    for i in range(len(arr)):
        if arr[i] % num_one == 0 and arr[i] % num_two == 0:
            arr[i] = string_one + string_two
        elif arr[i] % num_one == 0:
            arr[i] = string_one  
        elif arr[i] % num_two == 0:
            arr[i] = string_two
    return arr

# Task 49. Filling an array (part 1)
https://www.codewars.com/kata/571d42206414b103dc0006a1
# We want an array, but not just any old array, an array with contents!
# Write a function that produces an array with the numbers 0 to N-1 in it.
# For example, the following code will result in an array containing the numbers 0 to 4:
# arr(5) // => [0,1,2,3,4]
 
def arr(n=0): 
    return list(range(n)) 
 
# Task 50. Pre-FizzBuzz Workout #1
https://www.codewars.com/kata/569e09850a8e371ab200000b
# This is the first step to understanding FizzBuzz.
# Your inputs: a positive integer, n, greater than or equal to one. n is provided, you have NO CONTROL over its value.
# Your expected output is an array of positive integers from 1 to n (inclusive).
# Your job is to write an algorithm that gets you from the input to the output.

def pre_fizz(n):
    return list(range(1,n+1))



