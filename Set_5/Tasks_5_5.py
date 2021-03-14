# Real code challenges. Set #5
# Completed_solutions 5.41-5.50

#  Task 5.41. 1/n- Cycle
https://www.codewars.com/kata/5a057ec846d843c81a0000ad
# Let be n an integer prime with 10 e.g. 7.
1/7 = 0.142857 142857 142857 ....
# We see that the decimal part has a cycle: 142857. The length of this cycle is 6. In the same way:
# 1/11 = 0.09 09 09 .... Cycle length is 2.
# Task
# Given an integer n (n > 1) the function cycle(n) returns the length of the cycle if there is one otherwise (n and 10 not coprimes) return -1.
# Examples:
# cycle(5) = -1
# cycle(13) = 6 -> 0.076923 076923 0769
# cycle(21) = 6 -> 0.047619 047619 0476
# cycle(27) = 3 -> 0.037 037 037 037 0370
# cycle(33) = 2 -> 0.03 03 03 03 03 03 03 03
# cycle(37) = 3 -> 0.027 027 027 027 027 0
# cycle(94) = -1 
# Notes: cycle(22) = -1 since 1/22 ~ 0.0 45 45 45 45 ...

def cycle(n) :
    if n%2 == 0 or n%5 == 0:
        return -1
    d = 9
    count = 1
    while d % n != 0:
        d = d % n * 10 + 9
        count += 1
    return count

# Task 5.42. Polydivisible Numbers 
https://www.codewars.com/kata/5e4217e476126b000170489b 
# Most of this problem is by the original author of the harder kata, I just made it simpler.
# I read a book recently, titled "Things to Make and Do in the Fourth Dimension" by comedian and mathematician Matt Parker ( Youtube ), 
# and in the first chapter of the book Matt talks about problems he likes to solve in his head to take his mind off the fact that he is in his dentist's chair, we've all been there!
# The problem he talks about relates to polydivisible numbers, and I thought a kata should be written on the subject as it's quite interesting. 
# (Well it's interesting to me, so there!)
# Polydivisib... huh what? So what are they?
# A polydivisible number is divisible in an unusual way. The first digit is cleanly divisible by 1, the first two digits are cleanly divisible by 2, the first three by 3, and so on.
# Examples
# Let's take the number 1232 as an example.
#  1     / 1 = 1     // Works
#  12    / 2 = 6     // Works
#  123   / 3 = 41    // Works
#  1232  / 4 = 308   // Works
# 1232 is a polydivisible number.

# However, let's take the number 123220 and see what happens.
#  1      /1 = 1    // Works
#  12     /2 = 6    // Works
#  123    /3 = 41   // Works
#  1232   /4 = 308  // Works
#  12322  /5 = 2464.4         // Doesn't work
#  123220 /6 = 220536.333...  // Doesn't work
# 123220 is not polydivisible.

# Your job: check if a number is polydivisible or not. Return true if it is, and false if it isn't.

def polydivisible(x):
    x = str(x)
    for i in range(1,len(x)+1):
        if int(x[:i])% i : return False
    return True
	
# Task 5.43. FizzBuzz++
https://www.codewars.com/kata/596925532f709fccf3000077 
# There is a common problem given to interviewees in software. It is called FizzBuzz. It works as follows: 
# For the numbers between 1 and 100, print fizz if it is a multiple of 3 and buzz if it is a mutiple of 5, else print the number itself.
# You are in an interview and they ask you to complete fizzbuzz (which can be done in a one-liner in a few langs) and you knock it out of the park.
# Surprised by your ability, the interviewer gives you a harder problem. Given a list of coprime numbers, 
# (that is that the g.c.d. of all the numbers == 1) and an equally sized list of words. 
# compute its fizzbuzz representation up until the pattern of strings repeats itself.
# Here's an example
# fizzbuzz_plusplus([2, 3, 5], ['fizz', 'buzz', 'bazz']); 
# // => [1, 'fizz', 'buzz', 'fizz', 'bazz', 'fizzbuzz', 7, 'fizz', 'buzz', 'fizzbazz', 11, 'fizzbuzz', 13, 'fizz', 'buzzbazz', 'fizz', 17, 'fizzbuzz', 19, 'fizzbazz', 'buzz', 'fizz', 23, 'fizzbuzz', 'bazz', 'fizz', 'buzz', 'fizz', 29 , 'fizzbuzzbazz']

def fizzbuzz_plusplus(nums, words):
    m=1
    for el in nums:
        m *=el
    arr = list(range(1,m+1))
    ar = []
    for elem in (arr):
        s = ''
        for i,num in enumerate(nums):
            if elem % num==0:
                s+=words[i]
        if s =='':
             ar.append(elem)
        else:
            ar.append(s)
    return ar

# Task 5.44. Bubblesort Once
https://www.codewars.com/kata/56b97b776ffcea598a0006f2
# Bubblesort Algorithm
# Overview
# The Bubblesort Algorithm is one of many algorithms used to sort a list of similar items (e.g. all numbers or all letters) into either ascending order or descending order. Given a list (e.g.):
# [9, 7, 5, 3, 1, 2, 4, 6, 8]
# To sort this list in ascending order using Bubblesort, you first have to compare the first two terms of the list. 
# If the first term is larger than the second term, you perform a swap. The list then becomes:
# [7, 9, 5, 3, 1, 2, 4, 6, 8] # The "9" and "7" have been swapped because 9 is larger than 7 and thus 9 should be after 7
# You then proceed by comparing the 2nd and 3rd terms, performing a swap when necessary, and then the 3rd and 4th term, then the 4th and 5th term, etc. etc. 
# When you reach the end of the list, it is said that you have completed 1 complete pass.
# Task
# Given an array of integers, your function bubblesortOnce/bubblesort_once/BubblesortOnce (or equivalent, depending on your language's naming conventions) 
# should return a new array equivalent to performing exactly 1 complete pass on the original array. Your function should be pure, i.e. it should not mutate the input array.

def bubblesort_once(l):
    a = l[::]
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
    return a

# Task 5.45. Replacement 
https://www.codewars.com/kata/598d89971928a085c000001a
# Introduction
# Little Petya very much likes sequences. However, recently he received a sequence as a gift from his mother.
# Petya didn't like it at all! He decided to make a single replacement. 
# After this replacement, Petya would like to the sequence in increasing order.
# He asks himself: What is the lowest possible value I could have got after making the replacement and sorting the sequence?
# About the replacement
# Choose exactly one element from the sequence and replace it with another integer > 0. 
# You are not allowed to replace a number with itself, or to change no number at all.
# Task. Find the lowest possible sequence after performing a valid replacement, and sorting the sequence.
# Input: Input contains sequence with N integers. All elements of the sequence > 0. The sequence will never be empty.
# Output: Return sequence with N integers — which includes the lowest possible values of each sequence element, 
# after the single replacement and sorting has been performed.
# Examples:
# ([1,2,3,4,5])  =>  [1,1,2,3,4]
# ([4,2,1,3,5])  =>  [1,1,2,3,4]
# ([2,3,4,5,6])  =>  [1,2,3,4,5]
# ([2,2,2])      =>  [1,2,2]
# ([42])         =>  [1]

def sort_number(a): 
    a = sorted(a)
    if a[-1] != 1:
        a[-1] = 1
    else:
        a[-1] = 2
    return sorted(a)

# Task 5.46. Bouncy Numbers
https://www.codewars.com/kata/5769a78c6f2dea72b3000027
# A bouncy number is a positive integer whose digits neither increase nor decrease. 
# For example, 1235 is an increasing number, 5321 is a decreasing number, and 2351 is a bouncy number. 
# By definition, all numbers under 100 are non-bouncy, and 101 is the first bouncy number. 
# To complete this kata, you must write a function that takes a number and determines if it is bouncy.
# Input numbers will always be positive integers, but it never hurts to throw in some error handling : )
# For clarification, the bouncy numbers between 100 and 125 are: 101, 102, 103, 104, 105, 106, 107, 108, 109, 120, and 121.

def is_bouncy(number):
    return str(number) != "".join(sorted(str(number))) and str(number) != "".join(sorted(str(number), reverse=True))


# Task 5.47. Will the present fit? 
https://www.codewars.com/kata/52b23340c65ea422b1000045 
# Santa's elves are boxing presents, and they need your help! Write a function that takes two sequences of dimensions 
# of the present and the box, respectively, and returns a Boolean based on whether or not the present will fit in the box provided. 
# The box's walls are one unit thick, so be sure to take that in to account.
# Examples: Present and box respectively
# [10, 7, 16], [13, 32, 10] --> true, box is bigger than present
# [5, 7, 9], [9, 5, 7]      --> false, present and box are same size
# [17, 22, 10], [5, 5, 10]) --> false, box is too small

def will_fit(present, box):
    present = sorted(present)
    box = sorted(box)
    return all([box[i] - present[i] > 0 for i in range(3)])

# Task 5.48. Sort array by string length
https://www.codewars.com/kata/57ea5b0b75ae11d1e800006c
# Write a function that takes an array of strings as an argument and returns a sorted array 
# containing the same strings, ordered from shortest to longest.
# For example, if this array were passed as an argument:
# ["Telescopes", "Glasses", "Eyes", "Monocles"]
# Your function would return the following array:
# ["Eyes", "Glasses", "Monocles", "Telescopes"]
# All of the strings in the array passed to your function will be different lengths, 
# so you will not have to decide how to order multiple strings of the same length.

def sort_by_length(arr):
    return sorted(arr, key=len)

# Task 5.49. Binary sort
https://www.codewars.com/kata/5c8e99ba171e834117a0e905
# You have a string with zeroes and ones. Your task is to sort this line :
# "001110011" -> "000011111"
# "rry01066554thhg" -> "001"
# "code" -> ""

def binary_sort(strng):
    string = [el for el in strng if el in "01"]
    return "".join(sorted(string))

# Task 5.50. Alphabetically ordered
https://www.codewars.com/kata/5a8059b1fd577709860000f6
# Your task is very simple. Just write a function isAlphabetic(s), which takes an input string s in lowercase 
# and returns true/false depending on whether the string is in alphabetical order or not.
# For example, isAlphabetic('kata') is False as 'a' comes after 'k', but isAlphabetic('ant') is True.

def alphabetic(s):
    return sorted(s) == list(s)

#
