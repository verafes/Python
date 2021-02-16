# Real code challenges. Set #2
# Completed_solutions 2.71-2.80

# Task 2.71. Filter the number
https://www.codewars.com/kata/55b051fac50a3292a9000025/
# Your task is to return a number from a string.
# Details: You will be given a string of numbers and letters mixed up, 
# you have to return all the numbers in that string in the order they occur.

def filter_string(string):
    return int("".join(s for s in string if s.isdigit()))

# Task 2.72. Simple Pig Latin
https://www.codewars.com/kata/520b9d2ad5c005041100000f
# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    arr = []
    words = text.split()
    for el in words:
        if el not in ";:.,!?":
            el = el[1:]+el[0] + 'ay'
        arr.append(el)
    return " ".join(arr)
	
# Solution 2:

def pig_it(text):
    words = text.split()
    return " ".join([el[1:]+el[0] + 'ay' if el not in ";:.,!?" else el for el in words])

# Task 2.73. Love vs friendship
https://www.codewars.com/kata/59706036f6e5d1e22d000016
# If　a = 1, b = 2, c = 3 ... z = 26
# Then l + o + v + e = 54
# and f + r + i + e + n + d + s + h + i + p = 108
# So friendship is twice stronger than love :-)
# The input will always be in lowercase and never be empty.

def words_to_marks(s):
    abc = " abcdefghijklmnopqrstuvwxyz"
    return sum([abc.index(el) for el in s])


# Task 2.74. filterEvenLengthWords
https://www.codewars.com/kata/59564f3bcc15b5591a00004a
# Write a function called "filterEvenLengthWords".
# Given an array of strings, "filterEvenLengthWords" returns an array containing only the elements of the given array whose length is an even number.
# var output = filterEvenLengthWords(['word', 'words', 'word', 'words']);
# console.log(output); // --> ['word', 'word']

def filter_even_length_words(words):
    return [word for word in words if len(word)%2 == 0 ]

# Task 2.75. Can Santa save Christmas?
https://www.codewars.com/kata/5857e8bb9948644aa1000246
# Oh no! Santa's little elves are sick this year. He has to distribute the presents on his own.
# But he has only 24 hours left. Can he do it?
# Your Task:
# You will get an array as input with time durations as string in the following format: HH:MM:SS. 
# Each duration is a present Santa has to distribute. Determine whether he can do it in 24 hours or not.

def determine_time(arr):
    c = []
    for el in arr:
        h,m,s = el.split(":")
        c.append(int(h)*3600 + int(m)*60 + int(s))
    return sum(c) < 24*3600 

# solution 2:

def determine_time(arr):
    times = [el.split(":") for el in arr]
    return sum([int(el[0])*3600 + int(el[1])*60 +int(el[2]) for el in times]) < 24*3600 

# Task 76. 2.Sum even numbers
https://www.codewars.com/kata/586beb5ba44cfc44ed0006c3
# Write a function named sumEvenNumbers, taking a sequence of numbers as single parameter. 
# Your function must return the sum of the even values of this sequence.
# Only numbers without decimals like 4 or 4.0 can be even.
# Input: # sequence of numbers: those numbers could be integers and/or floats.
# For example, considering this input value : [4,3,1,2,5,10,6,7,9,8], 
# then your function should return 30 (because 4 + 2 + 10 + 6 + 8 = 30).

def sum_even_numbers(seq): 
    return sum([int(el) for el in seq if el%2==0])  

# Task 77. 2.Invert values
https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad
# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []
# You can assume that all values are integers. Do not mutate the input array/list.

def invert(lst):
    return [-el for el in lst]

# Task 2.78. If you can't sleep, just count sheep!!
https://www.codewars.com/kata/5b077ebdaf15be5c7f000077
# Given a non-negative integer, 3 for example, return a string with a murmur: 
# "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

def count_sheep(n):
     s = list(range(n))
     a=[]
     for el in s:
         el = str(el+1) + " sheep..."
         a.append(el)   
     return "".join(a)

# Solution 2

def count_sheep(n):
    return "".join([str(el+1) + " sheep..." for el in list(range(n))])

#Solution 3

def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))

# Task 2.79. Draw stairs
https://www.codewars.com/kata/5b4e779c578c6a898e0005c5
# Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest in the top left.
# For example n = 3 result in:
# "I\n I\n  I"

return '\n'.join[' '*i + "I" for i in range(n)]

# Task 2.80. Interview Question (easy)
https://www.codewars.com/kata/5b358a1e228d316283001892
# You receive the name of a city as a string, and you need to return a string that shows how many times 
# each letter shows up in the string by using an asterisk (*).
# For example:
# "Chicago"  -->  "c:**,h:*,i:*,a:*,g:*,o:*"
# As you can see, the letter c is shown only once, but with 2 asterisks.# 
# The return string should include only the letters (not the dashes, spaces, apostrophes, etc). 
# There should be no spaces in the output, and the different letters are separated by a comma (,) 
# as seen in the example above.
# Note that the return string must list the letters in order of their first appearence in the original string.

def get_strings(city):
    city = city.replace(" ","").lower()
    unique = []
    for el in city:
        if el not in unique:
            unique.append(el)
    return ",".join([f"{el}:{city.count(el) * '*' }" for el in unique])
