# Real code challenges. 
# Set #1. Completed_solutions 41-50

# Task 41. Get the Middle Character
https://www.codewars.com/kata/56747fd5cb988479af000028
#You are going to be given a word. Your job is to return the middle character of the word. 
# If the word's length is odd, return the middle character. 
# If the word's length is even, return the middle 2 characters.
#Examples:
#Kata.getMiddle("test") should return "es"
#Kata.getMiddle("testing") should return "t"
ata.getMiddle("middle") should return "dd"
#Kata.getMiddle("A") should return "A"

def get_middle(s):
    return  s[(len(s)-1)//2:(len(s)+2)//2]

# Task 42. Greet Me
https://www.codewars.com/kata/535474308bb336c9980006f2
# Write a method that takes one argument as name and then greets that name, capitalized 
# and ends with an exclamation point.
# "riley" --> "Hello Riley!"
# "JACK"  --> "Hello Jack!"

def greet(name): 
    return f"Hello {name.title()}!"

# Task 43. Remove String Spaces
https://www.codewars.com/kata/57eae20f5500ad98e50002c5
# Simple, remove the spaces from the string, then return the resultant string.

def no_space(x):
    return x.replace(" ","")

# Task 44. Reversed sequence
https://www.codewars.com/kata/5a00e05cc374cb34d100000d
# Get the number n (n>0) to return the reversed sequence from n to 1.
# Example : n=5 >> [5,4,3,2,1]

def reverse_seq(n):
    return [n for n in range(n,0,-1)]

#Solution #2

def reverse_seq(n):
    return list(range(n, 0, -1))
	
# Task 45. Simple equation reversal
https://www.codewars.com/kata/5aa3af22ba1bb5209f000037
# Given a mathematical equation that has *,+,-,/, reverse it as follows:
#For example: solve("100*b/y") = "y/b*100"
#solve("a+b-c/d*30") = "30*d/c-b+a"

def solve(eq):
    arr = list(eq.replace("*"," * ").replace("/"," / ").replace("-"," - ").replace("+"," + ").split(" "))
    return "".join(arr[::-1])
	
# Task 46. String ends with?
https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d
# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
# Examples: solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

def solution(string, ending):
    return string.endswith(ending)
	
# Task 47. String repeat
https://www.codewars.com/kata/57a0e5c372292dd76d000d7e
# Write a function called repeat_str which repeats the given string src exactly count times.
# repeatStr(6, "I") // "IIIIII"

def repeat_str(repeat, string):
    return string*repeat

# Task 48. Super Duper Easy
https://www.codewars.com/kata/55a5bfaa756cfede78000026
# Make a function that returns the value multiplied by 50 and increased by 6. 
# If the value entered is a string it should return "Error".

def problem(a):
    return 'Error' if type(a) is str else a*50+6
	
# Task 49. Cat and Mouse - Easy Version

# You will be given a string (x) featuring a cat 'C' and a mouse 'm'. The rest of the string will be made up of '.'.
# You need to find out if the cat can catch the mouse from it's current position. The cat can jump over three characters. So:
# C.....m returns 'Escaped!' <-- more than three characters between
# C...m returns 'Caught!' <-- as there are three characters between the two, the cat can jump.

def cat_mouse(x):
    c = x.index("C")
    m = x.index("m")
    return 'Caught!' if abs(c-m) <= 4 else 'Escaped!'
	
# Solution 2
def cat_mouse(x):
    return "Escaped!" if len(x) > 5 else "Caught!"

# Task 50. Mumbling
https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
# This time no story, no theory. The examples below show you how to write function accum:
# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(s):
    return '-'.join(el.upper() + el.lower() * i for i, el in enumerate(s))

#