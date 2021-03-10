# Real code challenges. Set #5
# Completed_solutions 5.31-5.40

#  Task 5.31. Xmas Tree
https://www.codewars.com/kata/577c349edf78c178a1000108
# Complete the function that returns a christmas tree of the given height. 
# The height is passed through to the function and the function should return a list containing each line of the tree.
# XMasTree(5) should return : ['____#____', '___###___', '__#####__', '_#######_', '#########', '____#____', '____#____']
# XMasTree(3) should return : ['__#__', '_###_', '#####', '__#__', '__#__']
# The final idea is for the tree to look like this if you decide to print each element of the list:
# XMasTree(5) will result in:
# ____#____              1
# ___###___              2
# __#####__              3
# _#######_              4
# #########       -----> 5 - Height of Tree
# ____#____        1      
# ____#____        2 - Trunk/Stem of Tree
# XMasTree(3) will result in:
# __#__                  1
# _###_                  2
# #####          ----->  3 - Height of Tree
# __#__           1
# __#__           2 - Trunk/Stem of Tree
# Pad with underscores i.e _ so each line is the same length. The last line forming the tree having only hashtags, no spaces. Also remember the trunk/stem of the tree.

def xmastree(n):
    width = n * 2 - 1
    arr = []
    for i in range (1, width + 1, 2):
        arr.append((i*'#').center(width, '_'))
    arr.extend([('#').center(width, '_')]*2)
    return arr

# Task 5.32. Custom Christmas Tree
https://www.codewars.com/kata/5a405ba4e1ce0e1d7800012e
# Task. Christmas is coming, and your task is to build a custom Christmas tree with the specified characters and the specified height.
# Inputs:
# chars: the specified characters.
# n: the specified height. A positive integer greater than 2.
# Output:
# A multiline string. Each line is separated by \n. A tree contains two parts: leaves and trunks.
# The leaves should be n rows. The first row fill in 1 char, the second row fill in 3 chars, and so on. 
# A single space will be added between two adjust chars, and some of the necessary spaces will be added to the left side, 
# to keep the shape of the tree. No space need to be added to the right side.
# The trunk should be at least 1 unit height, it depends on the value of the n. The minimum value of n is 3, and the height of the tree trunk is 1 unit height. 
# If n increased by 3, and the tree trunk increased by 1 unit. For example, when n is 3,4 or 5, trunk should be 1 row; when n is 6,7 or 8, trunk should be 2 row; and so on.
# Still not understand the task? Look at the following example ;-)

# Examples
# For chars = "*@o" and n = 3,the output should be:
#   *
#  @ o
# * @ o
#   |
# For chars = "*@o" and n = 6,the output should be:
# 
#      *
#     @ o
#    * @ o
#   * @ o *
#  @ o * @ o
# * @ o * @ o
#      |
#      |
# For chars = "1234" and n = 6,the output should be:
# 
#      1
#     2 3
#    4 1 2
#   3 4 1 2
#  3 4 1 2 3
# 4 1 2 3 4 1
#      |
#      |


def custom_christmas_tree(chars, n):
    arr = []
    copy_chars = chars
    for i in range(1, n + 1):
        line = " " * (n - i)
        for j in range(i):
            line += chars[0] + " "
            chars = chars[1:]
            if chars == "":
                chars = copy_chars
        line = line.rstrip()    
        arr.append(line)
    trunk = n // 3
    for i in range(trunk):
        arr.append(" " * (n - 1) + "|")    
    return "\n".join(arr)

# Solution 2
def custom_christmas_tree(chars, n):
    l = sum(list(range(1,n+1)))
    st = (chars * l)[:l]
    arr = []
    for i in range(1,n+1):
        arr.append(' '.join(st[:i]).rjust(n + i - 1, ' '))
        st = st[i:]
    for i in range(1, n// 3 +1):
        arr.append("|".rjust(len(arr[0]), ' '))
    return '\n'.join(arr)
	

# Task 5.33. Complete The Pattern #3 (Horizontal Image of #2)
https://www.codewars.com/kata/557341907fbf439911000022
# Task: You have to write a function pattern which creates the following pattern upto n number of rows. 
# If the Argument is 0 or a Negative Integer then it should return "" i.e. empty string.
# Pattern:
# (n)
# (n)(n-1)
# (n)(n-1)(n-2)
# ................
# (n)(n-1)(n-2)....4
# (n)(n-1)(n-2)....43
# (n)(n-1)(n-2)....432
# (n)(n-1)(n-2)....4321

ef pattern(n):
    s = ""
    arr = []
    for i in reversed(range(1,n+1)):
        s += str(i)
        arr.append(s)
    return "" if n <=0 else str("\n".join(arr))

# Task 5.34. Complete The Pattern #4
https://www.codewars.com/kata/55736129f78b30311300010f
# You have to write a function pattern which creates the following pattern upto n number of rows.
# If the Argument is 0 or a Negative Integer then it should return "" i.e. empty string.
##Examples:
# pattern(4):
# 1234
# 234
# 34
# 4

def pattern(n):
    arr = []
    for i in reversed(range(1,n+1)):
        el = "".join([str(x) for x in range(i,n+1)])
        arr.append(el)
    return "" if n <=0 else str("\n".join(arr[::-1]))

# Task 5.35. Complete The Pattern #6 - Odd Ladder
https://www.codewars.com/kata/5574940eae1cf7d520000076
# You have to write a function pattern which creates the following pattern (see examples) up to the desired number of rows.
# If the Argument is 0 or a Negative Integer then it should return "" i.e. empty string.
# If any even number is passed as argument then the pattern should last upto the largest odd number 
# which is smaller than the passed even number.
###Examples:
# pattern(9):
# 1
# 333
# 55555
# 7777777
# 999999999
# Note: There are no spaces in the pattern
# Hint: Use \n in string to jump to next line

def pattern(n):
    arr = []
    for i in range(1,n+1):
        if i%2 != 0:
            arr.append(str(i)*i)
    return "\n".join(arr)
	
# Short solution:
	
def pattern(n):
    return "\n".join(str(i)*i for i in range(1,n+1) if i%2 != 0)

# Task 5.36. Complete The Pattern #5 - Even Ladder
https://www.codewars.com/kata/55749101ae1cf7673800003e
# Task: You have to write a function pattern which creates the following pattern up to n/2 number of lines.
# If n <= 1 then it should return "" (i.e. empty string).
# If any odd number is passed as argument then the pattern should last up to the largest even number which is smaller than the passed odd number.
# Examples:
# pattern(8):
# 22
# 4444
# 666666
# 88888888
# Note: There are no spaces in the pattern
# Hint: Use \n in string to jump to next line

def pattern(n):
    return "\n".join(str(i)*i for i in range(2, n+1, 2))

# Task 5.37. Summations: 1
https://www.codewars.com/kata/55c02535bf0974404b0000f9
# Make a program that will take an int (x) and give you the summation of all numbers from 1 up to x included. 
# If the given input is not an integer, return "Invalid Value".
# Examples:
# summation(25)==325
# summation(2.56)=="Invalid Value"

def summation(x):
    return sum(range(x+1)) if type(x) is int else "Invalid Value"

# Task 5.38. Check for prime numbers
https://www.codewars.com/kata/53daa9e5af55c184db00025f
# In this kata you will create a function to check a non-negative input to see if it is a prime number.
# The function will take in a number and will return True if it is a prime number and False if it is not.
# A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True

# Task 5.39. Where is my parent!?(cry)
https://www.codewars.com/kata/58539230879867a8cd00011c
# Mothers arranged a dance party for the children in school. At that party, there are only mothers and their children. All are having great fun on the dance floor when suddenly all the lights went out. It's a dark night and no one can see each other. But you were flying nearby and you can see in the dark and have ability to teleport people anywhere you want.
# Legend:
# -Uppercase letters stands for mothers, lowercase stand for their children, i.e. "A" mother's children are "aaaa".
# -Function input: String contains only letters, uppercase letters are unique.
# Task:
# Place all people in alphabetical order where Mothers are followed by their children, i.e. "aAbaBb" => "AaaBbb".

def find_children(dancing_brigade):
    arr = []
    d = dancing_brigade.lower()
    for c in d:
        arr.append((c*d.count(c)).title())
    return ''.join(sorted(set(arr)))

# Task 5.40. Sort Out The Men From Boys
https://www.codewars.com/kata/5af15a37de4c7f223e00012d
# Scenario
# Now that the competition gets tough it will Sort out the men from the boys .
# Men are the Even numbers and Boys are the odd
# Task
# Given an array/list [] of n integers , Separate The even numbers from the odds , or Separate the men from the boys
# Notes
# Return an array/list where Even numbers come first then odds
# Since , Men are stronger than Boys , Then Even numbers in ascending order While odds in descending .
# Array/list size is at least 4 .
# Array/list numbers could be a mixture of positives , negatives .
# Have no fear , It is guaranteed that no Zeroes will exists

def men_from_boys(arr):
    arr = list(set(arr))
    men = sorted([x for x in arr if x%2==0])
    boys = sorted([x for x in arr if x not in men], reverse=True)
    return men + boys
	
#
