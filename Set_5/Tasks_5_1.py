# Real code challenges. Set #5
# Completed_solutions 5.01-5.10

#  Task 5.01. Squash the bugs
https://www.codewars.com/kata/56f173a35b91399a05000cb7
# Simple challenge - eliminate all bugs from the supplied code so that the code runs and outputs the expected value. 
# Output should be the length of the longest word, as a number.
# There will only be one 'longest' word.

# Given:

def find_longest(string):
    spl = str.split(" ")
    longest = 0
    i=0
    while (i > spl.length):
    if (spl(i).length > longest): longest = spl[i].length
    return longest
	
# Solution

def find_longest(string):
    spl = string.split(" ")
    longest = 0
    i=0
    while (i < len(spl)):
        if (len(spl[i]) > longest):
            longest = len(spl[i])
        i +=1
    return longest

# Task 5.02. Human Readable Time
https://www.codewars.com/kata/52685f7382004e774f0001f7
# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)# 
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

def make_readable(seconds):
    return f"{str(seconds//3600).rjust(2,'0')}:{str(seconds%3600//60).rjust(2,'0')}:{str(seconds%60).rjust(2,'0')}"

# Task 5.03. https://www.codewars.com/kata/546f922b54af40e1e90001da
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

# Task 5.04. Simple directions reversal
https://www.codewars.com/kata/5b94d7eb1d5ed297680000ca
# In this Kata, you will be given directions and your task will be to find your way back.
# solve(["Begin on Road A","Right on Road B","Right on Road C","Left on Road D"]) = ['Begin on Road D', 'Right on Road C', 'Left on Road B', 'Left on Road A']
# solve(['Begin on Lua Pkwy', 'Right on Sixth Alley', 'Right on 1st Cr']) =  ['Begin on 1st Cr', 'Left on Sixth Alley', 'Left on Lua Pkwy']

def solve(arr):
    directions = []
    street = []
    for el in arr[::-1]:
        street.append(" ".join(el.split()[1:]))
        directions.append(el.split()[0]) 
    directions = directions[:-1]
    new_d = ["Begin"]
    for e in directions:
        if e == "Right":
            new_d.append("Left")
        elif e == "Left":
            new_d.append("Right")
    s = []
    for i in range(len(new_d)):
        s.append(new_d[i] + " " + street[i])
    return s

# Task 5.05. Simple string characters
https://www.codewars.com/kata/5a29a0898f27f2d9c9000058
# In this Kata, you will be given a string and your task will be to return a list of ints detailing the count of uppercase letters, lowercase, numbers and special characters, as follows.
# Solve("*'&ABCDabcde12345") = [4,5,5,3]. 
# --the order is: uppercase letters, lowercase, numbers and special characters.

def solve(s):
    u = len([el for el in s if el.isupper()])
    l = len([el for el in s if el.islower()])
    n = len([el for el in s if el.isdigit()])
    s = len(s)-u-l-n
    return [u,l,n,s]

# Task 5.06. Single Word Pig Latin
https://www.codewars.com/kata/558878ab7591c911a4000007
# Pig Latin is an English language game where the goal is to hide the meaning of a word from people not aware of the rules.
# So, the goal of this kata is to wite a function that encodes a single word string to pig latin.
# The rules themselves are rather easy:
# The word starts with a vowel(a,e,i,o,u) -> return the original string plus "way".
# The word starts with a consonant -> move consonants from the beginning of the word to the end of the word until the first vowel, then return it plus "ay".
# The result must be lowercase, regardless of the case of the input. If the input string has any non-alpha characters, the function must return None, null, Nothing (depending on the language).
# The function must also handle simple random strings and not just English words.
# The input string has no vowels -> return the original string plus "ay".
# For example, the word "spaghetti" becomes "aghettispay" because the first two letters ("sp") are consonants, so they are moved to the end of the string and "ay" is appended.

def pig_latin(s):
    s = s.lower()
    vowels = [el for el in s if el in "aeiou"]
    notletter = [el for el in s if not el.isalpha() ]

    if s == "" or len(notletter) > 0:
        return None
    if len(vowels) == 0:
        return s + "ay"
    if s[0] in "aeiou":
        return s + "way"
    for i in range(len(s)):
        if s[i] in "aeiou":
            return s[i:] + s[:i] + "ay"

# Task 5.07. String array duplicates
https://www.codewars.com/kata/59f08f89a5e129c543000069
# In this Kata, you will be given an array of strings and your task is to remove all consecutive duplicate letters from each string in the array.
# For example:
# dup(["abracadabra","allottee","assessee"]) = ["abracadabra","alote","asese"].# 
# dup(["kelless","keenness"]) = ["keles","kenes"].
# Strings will be lowercase only, no spaces. See test cases for more examples.

def dup(arry):
    arr = []
    for word in arry:
        s = word[0]
        for i in range(len(word)-1):
            if word[i] != word[i+1]:
                s += word[i+1]
        arr.append(s)
    return (arr)  

# Task 5.08. Remove B M W
https://www.codewars.com/kata/59de795c289ef9197f000c48
# It happened decades before Snapchat, years before Twitter and even before Facebook. Targeted advertising was a bit of a challenge back then. 
# One day, the marketing professor at my university told us a story that I am yet to confirm using reliable sources. 
# Nevertheless, I retold the story to dozens of my students already, so, sorry BMW if it is all a big lie.
# Allegedly, BMW, in an attempt to target the educated, produced billboard posters featuring the English alphabet with three letters missing: B, M and W. 
# Needless to say, many were confused, some to the extent of road accidents.
# Your task is to write a function that takes one parameter str that MUST be a string and removes all capital and small letters B, M and W.
# If data of the wrong data type was sent as a parameter the function must throw an error with the following specific message:

TypeError("This program only works for text.")

def remove_bmw(string):
    for c in list('BMWbmw'):
        try: 
            string = string.replace(c, '')
        except AttributeError: 
            return "This program only works for text."
    return string
	
# Task 5.09. Reverse and Invert
https://www.codewars.com/kata/5899e054aa1498da6b0000cc
# Reverse and invert all integer values in a given list.
# Example: reverse_invert([1,12,'a',3.4,87,99.9,-42,50,5.6]) = [-1,-21,-78,24,-5]
# Ignore all other types than integer.

def reverse_invert(lst):
    f, arr = -1, []
    for el in lst:
        if type(el) is int:
            if el < 0:
                arr.append(int(str(el*f)[::-1]))
            else: 
                arr.append(int(str(el)[::-1])*f)
    return [el for el in arr]

# Task 5.10. Percentage of amino acids
https://www.codewars.com/kata/59759761e30a19cfe1000024
# You are a biologist working on the amino acid composition of proteins. Every protein consists of a long chain of 20 different amino acids with different properties. 
# Currently, you are collecting data on the percentage, various amino acids make up a protein you are working on. 
# As manually counting the occurences of amino acids takes too long (especially when counting more than one amino acid), you decide to write a program for this task:
# Write a function that takes two arguments,
# A (snippet of a) protein sequence
# A list of amino acid residue codes
# and returns the rounded percentage of the protein that the given amino acids make up. 
# If no amino acid list is given, return the percentage of hydrophobic amino acid residues ["A", "I", "L", "M", "F", "W", "Y", "V"].

def aa_percentage(seq, a=""):
    amino =  ["A", "I", "L", "M", "F", "W", "Y", "V"]
    percentage1 = [seq.count(el) for el in amino]
    percentage2 = [seq.count(el) for el in a]
    if a ==  []: return 0
    return round(sum(percentage1)*100/len(seq)) if len(a) == 0 else round(sum(percentage2)*100/len(seq)) 

#
