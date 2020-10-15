# Real code challenges. Set #2
# Completed_solutions 91-100

# Task 91. Highest and Lowest
https://www.codewars.com/kata/554b4ac871d6813a03000035
# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
# Example:
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Notes: All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.

def high_and_low(numbers):
    a = [int(el) for el in numbers.split(' ')]
    return f'{max(a)} {min(a)}'

# Task 92. Find The Parity Outlier
https://www.codewars.com/kata/5526fc09a1bbd946250002dc
# You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. 
# Write a method that takes the array as an argument and returns this "outlier" N.
# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36] - Should return: 11 (the only odd number)
# [160, 3, 1719, 19, 11, 13, -21] - Should return: 160 (the only even number)

def find_outlier(integers):
    odd = [num for num in integers if num % 2 != 0]
    even = [num for num in integers if num % 2 == 0]
    return odd[0] if len(odd) == 1 else even[0]
	
# Task 93. Responsible Drinking
https://www.codewars.com/kata/5aee86c5783bb432cd000018
# Codewars Bar recommends you drink 1 glass of water per standard drink so you're not hungover tomorrow morning.
# Your fellow coders have bought you several drinks tonight in the form of a string. Return a string suggesting 
# how many glasses of water you should drink to not be hungover.
# Examples
# "1 beer"  =>  "1 glass of water"
# "1 shot, 5 beers and 1 glass of wine"  =>  "7 glasses of water"

def hydrate(drink_string): 
    s = drink_string.split(" ")
    dig = sum([int(el) for el in s if el.isdigit()])
    return f'1 glass of water' if dig == 1 else f'{dig} glasses of water'

# Task 94. Predict your age!
https://www.codewars.com/kata/5aff237c578a14752d0035ae

# My grandfather always predicted how old people would get, and right before he passed away he revealed his secret!
# In honor of my grandfather's memory we will write a function using his formula!
# Take a list of ages when each of your great-grandparent died.
# Multiply each number by itself. Add them all together.
# Take the square root of the result. Divide by two.
# Example
# predict_age(65, 60, 75, 55, 60, 63, 64, 45) == 86
# Note: the result should be rounded down to the nearest integer.

def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    array = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    s = sum([el*el for el in array])**0.5/2
    return int(s)

# Task 95. Number of People in the Bus
https://www.codewars.com/kata/5648b12ce68d9daa6b000099
# There is a bus moving in the city, and it takes and drop some people in each bus stop.
# You are provided with a list (or array) of integer arrays (or tuples). 
# Each integer array has two items which represent number of people get into bus (The first item) and number of people get off the bus (The second item) in a bus stop.
# Your task is to return number of people who are still in the bus after the last bus station (after the last array). 
# Even though it is the last bus stop, the bus is not empty and some people are still in the bus, and they are probably sleeping there :D
# Take a look on the test cases.
# Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the return integer can't be negative.
# The second value in the first integer array is 0, since the bus is empty in the first bus stop.

def number(bus_stops):
    return sum(el[0] - el[1] for el in bus_stops) 

# Task 96. Dominant array elements
https://www.codewars.com/kata/5a04133e32b8b998dc000089
# An element in an array is dominant if it is greater than all elements to its right. 
# You will be given an array and your task will be to return a list of all dominant elements. For example:
# solve([1,21,4,7,5]) = [21,7,5] because 21, 7 and 5 are greater than elments to their right. 
# solve([5,4,3,2,1]) = [5,4,3,2,1]
# Notice that the last element is always included.

def solve(arr):
    final = []
    for i in range(len(arr)-1):
        if  arr[i] > max(arr[i+1:]):
            final.append(arr[i])
    final.append(arr[-1])
    return final
	
# Solution 2. 

def solve(arr):
    return [arr[i] for i in range(len(arr)-1) if arr[i] > max(arr[i+1:])] + [arr[-1]]

# Task 97. Santa's Naughty List
https://www.codewars.com/kata/5a0b4dc2ffe75f72f70000ef
https://www.codewars.com/kata/5a0b4dc2ffe75f72f70000ef
Christmas is coming, and Santa has a long list to go through, to find who deserves presents for the big day. 
# Go through a list of children, and return a list containing every child who appeared on Santa's list. 
# Do not add any child more than once. Output should be sorted.
# Comparison should be case sensitive and the returned list should contain only one copy of each name: "Sam" and "sam" are different, but "sAm" and "sAm" are not.

def find_children(santas_list, children):
    return sorted([el for el in children if el in santas_list])

# Task 98. Return String of First Characters

# In this exercise, a string is passed to a method and a new string has to be returned with the first character of each word in the string.
# For example: "This Is A Test" ==> "TIAT"

def make_string(s):
    return "".join([el[0] for el in s.split()])

# Task 99. Shortest Word
https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9
# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.

def find_short(s):
    arr = s.split()
    arr2 = []
    for el in arr:
        l = len(el)
        arr2.append(l)
    return min(arr2)
	
Solution 2

def find_short(s):
    return min([len(el) for el in s.split()])


# Task 100. Dubstep
https://www.codewars.com/kata/551dc350bf4e526099000ae5
# Polycarpus works as a DJ in the best Berland nightclub, and he often uses dubstep music in his performance. 
# Recently, he has decided to take a couple of old songs and make dubstep remixes from them.
# Let's assume that a song consists of some number of words (that don't contain WUB). 
# To make the dubstep remix of this song, Polycarpus inserts a certain number of words "WUB" before the first word of the song (the number may be zero), 
# after the last word (the number may be zero), and between words (at least one between any pair of neighbouring words), and then the boy glues together all the words, 
# including "WUB", in one string and plays the song at the club.
# For example, a song with words "I AM X" can transform into a dubstep remix as "WUBWUBIWUBAMWUBWUBX" and cannot transform into "WUBWUBIAMWUBX".
# Recently, Jonny has heard Polycarpus's new dubstep track, but since he isn't into modern music, 
# he decided to find out what was the initial song that Polycarpus remixed. Help Jonny restore the original song.

def song_decoder(song):
    return " ".join([el for el in song.split("WUB") if el != ""])

