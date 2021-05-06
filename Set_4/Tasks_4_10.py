# Real code challenges. Set #4-10
# Completed_solutions 4.91-5.00

#  Task 4.91. Vowel Count
https://www.codewars.com/kata/54ff3102c1bad923760001f3 
# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

def get_count(str):
    num_vowels = 0
    for el in str:
        if el in "aouie":
            num_vowels += 1
    return num_vowels

# Task 492. Which string is worth more?
https://www.codewars.com/kata/5840586b5225616069000001
# You will be given two ASCII strings, a and b. Your task is write a function to determine which one of these strings is "worth" more, and return it.
# A string's worth is determined by the sum of its ASCII codepoint indexes. So, for example, the string HELLO has a value of 372: H is codepoint 72, E 69, L 76, and O is 79. The sum of these values is 372.
# In the event of a tie, you should return the first string, i.e. a.

def highest_value(a, b):
    sa, sb = 0, 0
    for el in a:
        sa += ord(el)
    for el in b:
        sb += ord(el)
    return a if sa >= sb else b

# Short solution

def highest_value(a, b):
    return a if sum(ord(c) for c in a) >= sum(ord(c) for c in b) else b

# Task 4.93. This is odd
https://www.codewars.com/kata/554003323fd6af1c4200004e
# Create a function that checks if a number is odd.
# Expect negative and decimal numbers too. Remember... all negative numbers can also be either odd or even.
# Decimal numbers always return false
# Examples
# is_odd(2)--> false
# is_odd(5)--> true
# is_odd(4)--> false
# is_odd(-17)--> true
# is_odd(-7.0)--> true
# is_odd(-7.1)--> false
# is_odd(4.23)--> false
# is_odd(5.0)--> true

def is_odd(n):
    return n % 2 !=0 and n % 1 == 0 

# Task 4.94. Is it a vowel on this position?
https://www.codewars.com/kata/5a2b7edcb6486a856e00005b
# Check if it is a vowel(a, e, i, o, u,) on the n position in a string (the first argument). Don't forget about uppercase.
# A few cases:
# checkVowel('cat', 1)  ->   true // 'a' is a vowel
# checkVowel('cat', 0)  ->   false // 'c' is not a vowel
# checkVowel('cat', 4)  ->   false // this position doesn't exist

def check_vowel(string, position):
    print(string, position)
    return 0 <= position < len(string) and string[position].lower() in 'aouei'

# Task 4.95. Check if a triangle is an equable triangle!
https://www.codewars.com/kata/57d0089e05c186ccb600035e
# A triangle is called an equable triangle if its area equals its perimeter. 
# Return true, if it is an equable triangle, else return false. 
# You will be provided with the length of sides of the triangle. Happy Coding!

def equable_triangle(a,b,c):
    p = (a + b +c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return a + b + c == s

# Task 4.96. You're a square!
https://www.codewars.com/kata/54c27a33fb7da0db0100040e
# You like building blocks. You especially like building blocks that are squares. 
# And what you even like more, is to arrange them into a square of square building blocks!
# However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! 
# Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! 
# You just have to check if your number of building blocks is a perfect square.
# Task. Given an integral number, determine if it's a square number:
# In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, 
# it is the product of some integer with itself.
#  The tests will always use some integral number, so don't worry about that in dynamic typed languages.

# Examples
# -1  =>  false
#  0  =>  true
#  3  =>  false
#  4  =>  true
# 25  =>  true
# 26  =>  false

def is_square(n):    
    if n < 0: return False
    return n**0.5 % 1 == 0

# Task 4.97. Hello World without strings, numbers and booleans
https://www.codewars.com/kata/5b0148133e9715bf6f000154
# Create the hi_all() function without using strings, numbers and booleans. The return value is "Hello World". 
# No, it is not impossible, use the builtin functions. Good luck :)

def hi_all():
    one = len([[]])
    two = one + one
    three = one + two
    four = two * two
    five = four + one
    six = two * three
    seven = six + one
    eight = two * four
    nine = eight + one
    ten = two * five
    H = chr(ten * seven + two)
    e = chr(ten * ten + one)
    l = chr(ten * ten + eight)
    o = chr(ten * ten + ten + one)
    space  = chr(ten * three + two)
    W = chr(ten * eight + seven)
    r = chr(ten * ten + ten + four)
    d = chr(ten * ten)
    return H + e + l + l + o + space + W + o + r + l + d

# Task 4.98. Hello World - Without Strings
https://www.codewars.com/kata/584c7b1e2cb5e1a727000047
# You need to create a function, helloWorld, that will return the String Hello, World! without actually using raw strings. 
# This includes quotes, double quotes and template strings. You can, however, use the String constructor and any related functions.
# You cannot use the following: "Hello, World!" or 'Hello, World!' or `Hello, World!`

def hello_world():
    return chr(72)+chr(101)+chr(108)+chr(108)+chr(111)+chr(44)+chr(32)+chr(87)+chr(111)+chr(114)+chr(108)+chr(100)+chr(33) 
	
# Task 4.99. Numbers to Letters
https://www.codewars.com/kata/57ebaa8f7b45ef590c00000c
# Given an array of numbers (in string format), you must return a string. The numbers correspond 
# to the letters of the alphabet in reverse order: a=26, z=1 etc. 
# You should also account for '!', '?' and ' ' that are represented by '27', '28' and '29' respectively.
# All inputs will be valid.

def switcher(arr):
    alph = "0zyxwvutsrqponmlkjihgfedcba!? "
    s = ""
    for el in arr:
        s += alph[int(el)]
    return s
	
# Task 5.00. Replace With Alphabet Position
https://www.codewars.com/kata/546f922b54af40e1e90001da
# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.
# Example
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)

def alphabet_position(text):
    abc = "abcdefghijklmnopqrstuvwxyz" 
    text = text.lower() 
    return " ".join([str(abc.index(el)+1) for el in text if el.isalpha()])
	
#
