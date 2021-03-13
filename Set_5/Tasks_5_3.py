# Real code challenges. Set #5
# Completed_solutions 5.21-5.30

#  Task 5.21. Classic Hello World
https://www.codewars.com/kata/57036f007fd72e3b77000023
# You are given a method called main, make it print Hello World! and don't return anything
# Note that for some languages, the function main is the entry point of the program.
# Here's how it will be tested:
#    Solution.main("parameter1", "parameter2","parametern")

class Solution:
    def main(self):
        print("Hello World!")

# Task 5.22. Where is my parent!?(cry)
https://www.codewars.com/kata/58539230879867a8cd00011c
# Mothers arranged a dance party for the children in school. At that party, there are only mothers and their children. 
# All are having great fun on the dance floor when suddenly all the lights went out. It's a dark night and no one can see each other. 
# But you were flying nearby and you can see in the dark and have ability to teleport people anywhere you want.
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

# Task 5.23. Baby shark lyrics generator
https://www.codewars.com/kata/5d076515e102162ac0dc514e
# Create a function, as short as possible, that returns this lyrics.
# Your code should be less than 300 characters. Watch out for the three points at the end of the song.

# Baby shark, doo doo doo doo doo doo
# Baby shark, doo doo doo doo doo doo
# Baby shark, doo doo doo doo doo doo
# Baby shark!
# Mommy shark, doo doo doo doo doo doo
# Mommy shark, doo doo doo doo doo doo
# Mommy shark, doo doo doo doo doo doo
# Mommy shark!
# Daddy shark, doo doo doo doo doo doo
# Daddy shark, doo doo doo doo doo doo
# Daddy shark, doo doo doo doo doo doo
# Daddy shark!
# Grandma shark, doo doo doo doo doo doo
# Grandma shark, doo doo doo doo doo doo
# Grandma shark, doo doo doo doo doo doo
# Grandma shark!
# Grandpa shark, doo doo doo doo doo doo
# Grandpa shark, doo doo doo doo doo doo
# Grandpa shark, doo doo doo doo doo doo
# Grandpa shark!
# Let's go hunt, doo doo doo doo doo doo
# Let's go hunt, doo doo doo doo doo doo
# Let's go hunt, doo doo doo doo doo doo
# Let's go hunt!
# Run away,…

def baby_shark_lyrics():
    s = ''
    doo = ',' + ' doo'*6 + '\n'
    arr = ['Baby shark', 'Mommy shark', 'Daddy shark', 'Grandma shark', 'Grandpa shark', 'Let\'s go hunt']
    for el in arr:
        s += (el + doo)*3 + el + '!\n'
    return s + 'Run away,…'   

# Task 5.24. Fix the loop!
https://www.codewars.com/kata/55ca43fb05c5f2f97f0000fd
# Your collegue wrote an simple loop to list his favourite animals. 
# But there seems to be a minor mistake in the grammar, which prevents the program to work. Fix it! :)
# If you pass the list of your favourite animals to the function, you should get the list of the animals with orderings and newlines added.
# For example, passing in:
# animals = [ 'dog', 'cat', 'elephant' ]
# will result in:

list_animals(animals) == '1. dog\n2. cat\n3. elephant\n'

# Given (Broken code)

def list_animals(animals):
    list = ''
    for i in range(animals):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list

# Solution

def list_animals(animals):
    lst = ''
    for i in range(len(animals)):
        lst += str(i + 1) + '. ' + animals[i] + '\n'
    return lst

# Task 5.25. Exclamation marks series #13: Count the number of exclamation marks and question marks, return the product
https://www.codewars.com/kata/57fb142297e0860073000064
# Description:
# Count the number of exclamation marks and question marks, return the product.
# Examples
# Product("") == 0
# product("!") == 0
# Product("!ab? ?") == 2
# Product("!!") == 0
# Product("!??") == 2
# Product("!???") == 3
# Product("!!!??") == 6
# Product("!!!???") == 9
# Product("!???!!") == 9
# Product("!????!!!?") == 20

def product(s):
    return s.count("!") * s.count("?") 

# Task 5.26. Encrypt this!
https://www.codewars.com/kata/5848565e273af816fb000449
# Description: Encrypt this!
# You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:
# Your message is a string containing space separated words.
# You need to encrypt each word in the message using the following rules:
# The first letter needs to be converted to its ASCII code.
# The second letter needs to be switched with the last letter
# Keepin' it simple: There are no special characters in input.
# Examples:
# encrypt_this("Hello") == "72olle"
# encrypt_this("good") == "103doo"
# encrypt_this("hello world") == "104olle 119drlo"

def encrypt_this(text):
    text = text.split()
    arr = []
    for w in (text):
        w = str(ord(w[0])) + w[2:][-1:] + w[2:len(w)-1] + w[1:2]
        arr.append(w)
    return " ".join(arr)

# Task 5.27. WeIrD StRiNg CaSe
https://www.codewars.com/kata/52b757663a95b11b3d00062d
# Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string 
# with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. 
# The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased.
# The passed in string will only consist of alphabetical characters and spaces(' '). 
# Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').
# Examples:
# to_weird_case('String'); # => returns 'StRiNg'
# to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'

def to_weird_case(string):
    s = string.split(" ")
    n = []
    for word in s:
        new = ""
        for i, el in enumerate(word):
            if i %2 == 0:
                new += el.upper()
            else:
                new += el.lower()
        n.append(new)
    return " ". join(n)

# Task 5.28. Vowel Count
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

# Task 5.29. Valid Spacing
https://www.codewars.com/kata/5f77d62851f6bc0033616bd8
#  our task is to write a function called valid_spacing() or validSpacing() which checks if a string has valid spacing. The function should return either True or False.
# For this kata, the definition of valid spacing is one space between words, and no leading or trailing spaces. Below are some examples of what the function should return.
# 'Hello world' = True
# ' Hello world' = False
# 'Hello world  ' = False
# 'Hello  world' = False
# 'Hello' = True
# Even though there are no spaces, it is still valid because none are needed
# 'Helloworld' = True 
# True because we are not checking for the validity of words.
# 'Helloworld ' = False
# ' ' = False
# '' = True
# Note - there will be no punctuation or digits in the input string, only letters.

def valid_spacing(s):
    if s == "": return True
    return False if "" in s.split(" ") else True

# Task 5.30. Unique In Order
https://www.codewars.com/kata/54e6533c92449cc251001667
# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements 
# with the same value next to each other and preserving the original order of elements.
# For example:
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

def unique_in_order(s):
    if s == "" or s == []:
        return []
    new = [s[0]]
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            new.append(s[i+1])
    return new

#
