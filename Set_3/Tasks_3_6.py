# Real code challenges. Set #3
# Completed_solutions 51-60.

# Task 51. Mirror, mirror, on the wall...
https://www.codewars.com/kata/5f55ecd770692e001484af7d
# You get a list of integers, and you have to write a function mirror that returns the "mirror" (or symmetric) version of this list: 
# i.e. the middle element is the greatest, then the next greatest on both sides, the the next greatest, and so on...
# More info. The list will always consist of integers in range -1000..1000 and will vary in size between 0 and 10000. 
# Your function should not mutate the input array, and this will be tested (where applicable). 
# Notice that the returned list will always be of odd size, since there will always be a definitive middle element.
# Examples: []  -->  [], [1]  -->  [1], [2, 1]  -->  [1, 2, 1],  [1, 3, 2]  -->  [1, 2, 3, 2, 1]

def mirror(data: list) -> list:
    lst = sorted(data)
    if len(data) <=1: return data
    else:
        for i in reversed(range(len(lst)-1)):
            lst.append(lst[i]) 
    return lst

# Solution #2:

def mirror(data: list) -> list:
    arr = sorted(data)
    return arr + arr[-2::-1]
	
# Task 52. Simple Fun #63: Shape Area
https://www.codewars.com/kata/5893e0c41a88085c330000a0
# Task. Below we will define what and n-interesting polygon is and your task is to find its area for a given n. (use link to see pic)
# A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained 
# by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim side by side. 
# You can see the 1-, 2- and 3-interesting polygons in the picture below.
# For n = 1, the output should be 1; For n = 2, the output should be 5; For n = 3, the output should be 13.

def shape_area(n):
    return n**2+(n-1)**2

# Task 53. Swap the head and the tail
https://www.codewars.com/kata/5a34f087c5e28462d9000082
# You need to swap the head and the tail of the specified array:
# the head (the first half) of array moves to the end, the tail (the second half) moves to the start. 
# The middle element (if it exists) leaves on the same position.
# Return new array. For example: [ 1, 2, 3, 4, 5 ]   =>  [ 4, 5, 3, 1, 2 ]

def swap_head_tail(arr):
    i = int(len(arr) / 2)
    return arr[-i:] + arr[i:-i] + arr[:i]

# Task 54. Add Length
https://www.codewars.com/kata/559d2284b5bb6799e9000047
# What if we need the length of the words separated by a space to be added at the end of that same word and have it returned as an array?
# add_length('apple ban') => ["apple 5", "ban 3"]
# add_length('you will win') => ["you 3", "will 4", "win 3"]
# Your task is to write a function that takes a String and returns an Array/list with the length of each word added to each element .
# Note: String will have at least one element; words will always be separated by a space.

def add_length(str_):
    return [f'{el} {len(el)}' for el in str_.split(' ')]

# Task 55. Alphabet symmetry
https://www.codewars.com/kata/59d9ff9f7905dfeed50000b0
# Consider the word "abode". We can see that the letter a is in position 1 and b is in position 2. In the alphabet, a and b are also in positions 1 and 2. Notice also that d and e in abode occupy the positions they would occupy in the alphabet, which are positions 4 and 5.
# Given an array of words, return an array of the number of letters that occupy their positions in the alphabet for each word. For example,
# solve(["abode","ABc","xyzD"]) = [4, 3, 1]
# See test cases for more examples.
# Input will consist of alphabet characters, both uppercase and lowercase. No spaces.

def count_letter(word):
    count = 0
    word = word.lower()
    alp = "abcdefghijklmnopqrstuvwxyz"
    for i, el in enumerate(word):
        if i == alp.index(el):
            count += 1
    return count

def solve(arr):
    return [count_letter(el) for el in arr]

# Task 56. Breaking search bad
https://www.codewars.com/kata/52cd53948d673a6e66000576
# The function must return the sequence of titles that match the string passed as an argument.
# titles = ['Rocky 1', 'Rocky 2', 'My Little Poney']
# search(titles, 'ock') --> ['Rocky 1', 'Rocky 2']
# But the function return some weird result and skip some of the matching results.
# Does the function have special movie taste? Let's figure out !

def search(titles, term): 
    return [el for el in titles if term in el.lower()]

# Task 57. Build Tower
https://www.codewars.com/kata/576757b1df89ecf5bd00073b
# Build Tower by the following given argument: number of floors (integer and always greater than 0).
# Tower block is represented as * 
# Python: return a list

def tower_builder(n):
    lst = []
    for i in range(1,n*2, 2):
        lst.append(('*'*i).center(n*2-1))
    return lst  
	
# Solution 2

def tower_builder(n):
    return [('*' * i).center(2 * n - 1) for i in range(1,2 * n, 2)]

# Task 58. Convert number to reversed array of digits
https://www.codewars.com/kata/5583090cbe83f4fd8c000051
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
# Example: 348597 => [7,9,5,8,4,3]

def digitize(n):
    return [int(el) for el in reversed(str(n))] 

# Task 59. Count by X 
https://www.codewars.com/kata/5513795bd3fafb56c200049e
# Create a function with two arguments that will return an array of the first (n) multiples of (x).
# Assume both the given number and the number of times to count will be positive numbers greater than 0.
# Return the results as an array (or list in Python, Haskell or Elixir).
# Examples:
# count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
# count_by(2,5) #should return [2,4,6,8,10]

def count_by(x, n):
    return [i * x for i in range(1, n + 1)]

# Task 60. Duplicate sandwich
https://www.codewars.com/kata/5f8a15c06dbd530016be0c19
# In this kata you will be given a list consisting of unique elements except for one thing that appears twice.
# Your task is to output a list of everything inbetween both occurrences of this element in the list.

def duplicate_sandwich(arr):
    dups = [i for i, el in enumerate(arr) if arr.count(el) > 1]
    return arr[dups[0]+1:dups[1]]
