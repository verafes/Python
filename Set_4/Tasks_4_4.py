# Real code challenges. Set #4-4
# Completed_solutions 4.31-4.40

#  Task 4.31. Simple Fun #17: Rounders
https://www.codewars.com/kata/58846d50f54f021d90000012
# We want to turn the given integer into a number that has only one non-zero digit using a tail rounding approach. This means that at each step we take the last non 0 digit of the number and round it to 0 or to 10. If it's less than 5 we round it to 0 if it's larger than or equal to 5 we round it to 10 (rounding to 10 means increasing the next significant digit by 1). The process stops immediately once there is only one non-zero digit left.
# Example:  For value = 15, the output should be 20
# For value = 1234, the output should be 1000. E.g. 1234 -> 1230 -> 1200 -> 1000.
# For value = 1445, the output should be 2000. E.g. 1445 -> 1450 -> 1500 -> 2000.

import math
def rounders(value):
    for c in range(1,len(str(value))):
        if str(value).find("5") > 0:
            value = int(math.ceil(value/10**c)*10**c)
        else:
            value = int(round(value/10**c)*10**c)
    return value

# Solution 2

def rounders(value):
    count = 0
    
    while value > 10:
        digit = value % 10
        value //= 10
        count += 1
        
        if digit >= 5:
            value += 1
    
    return value * 10**count

# Task 4.32. Abbreviate a Two Word Name (#2)
https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3
# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:
# Sam Harris => S.H
# Patrick Feeney => P.F

def abbrev_name(name):
    names = name.title().split(' ')
    return '.'.join([f"{n[0]}" for n in names])

# Task 4.33. All Star Code Challenge #3
https://www.codewars.com/kata/58640340b3a675d9a70000b9
# Create a function, called removeVowels (or remove_vowels), that takes a string argument 
# and returns that same string with all vowels removed (vowels are "a", "e", "i", "o", "u").
# removeVowels("drake") // => "drk"
# removeVowels("aeiou") // => ""

def remove_vowels(strng):
    return ''.join([el for el in strng if el not in "aoieu"])  

# Task 4.34. All Star Code Challenge #16
https://www.codewars.com/kata/586566b773bd9cbe2b000013
# Create a function called noRepeat() that takes a string argument and returns a single letter string of the first not repeated character in the entire string.
# noRepeat("aabbccdde") // => "e"
# noRepeat("wxyz") // => "w"
# noRepeat("testing") // => "e"
# Note: ONLY letters from the english alphabet will be used as input There will ALWAYS be at least one non-repeating letter in the input string

def no_repeat(string):
    return [x for x in string if string.count(x) == 1][0]

# Task 4.35. Alternate capitalization
https://www.codewars.com/kata/59cfc000aeb2844d16000075 
# Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. 
# Index 0 will be considered even.
# For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.
# The input will be a lowercase string with no spaces.

def capitalize(s):
    a = ""
    b = ""
    for i, el in enumerate(s):
        if i % 2 == 0:
            a += el.upper()
            b = b + el
        else:
            b += el.upper()
            a = a + el
            
    return [a, b]
	
# Task 4.36. ltERnaTIng cAsE <=> ALTerNAtiNG CaSe
https://www.codewars.com/kata/56efc695740d30f963000557
# Define function that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. For example:
# "hello world".toAlternatingCase() === "HELLO WORLD"
# "HELLO WORLD".toAlternatingCase() === "hello world"
# "hello WORLD".toAlternatingCase() === "HELLO world"
# "HeLLo WoRLD".toAlternatingCase() === "hEllO wOrld"
# "12345".toAlternatingCase() === "12345" // Non-alphabetical characters are unaffected
# "1a2b3c4d5e".toAlternatingCase() === "1A2B3C4D5E"
# "String.prototype.toAlternatingCase".toAlternatingCase() === "sTRING.PROTOTYPE.TOaLTERNATINGcASE"

def to_alternating_case(string):
    s = ""
    for el in string:
        if el.isalpha():
            s += el.swapcase()
        else:
            s += el
    return s

# Short solution:

def to_alternating_case(string):
    return string.swapcase()

# Task 4.37. Autocomplete! Yay!

# It's  time to create an autocomplete function! Yay!
# The autocomplete function will take in an input string and a dictionary array and return the values from the dictionary that start with the input string. If there are more than 5 matches, restrict your output to the first 5 results. If there are no matches, return an empty array.
# Example:
# autocomplete('ai', ['airplane','airport','apple','ball']) = ['airplane','airport']
# For this kata, the dictionary will always be a valid array of strings. Please return all results in the order given in the dictionary, even if they're not always alphabetical. The search should NOT be case sensitive, but the case of the word should be preserved when it's returned.
# For example, "Apple" and "airport" would both return for an input of 'a'. However, they should return as "Apple" and "airport" in their original cases.

def autocomplete(input_, dictionary):
    input_ = "".join([el for el in input_ if el.isalpha()])
    return [el for el in dictionary if el.lower().startswith(input_.lower())][:5]

# Task 4.38. Backspaces in string
https://www.codewars.com/kata/5727bb0fe81185ae62000ae3
# Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"
# Your task is to process a string with "#" symbols.
# Examples
# "abc#d##c"      ==>  "ac"
# "abc##d######"  ==>  ""
# "#######"       ==>  ""
# ""              ==>  ""

def clean_string(s):
    final = []
    for i in s:
        if i != "#":
            final.append(i)
        elif len(final) > 0: 
            final.pop()
    return "".join(final)
	
# Task 4.39. Basics 03: Strings, Numbers and Calculation
 https://www.codewars.com/kata/56b5dc75d362eac53d000bc8
# Here you have to do some mathematical operations on a "dirty string". This kata checks some basics, it's not too difficult.
# So what to do?
# Input: String which consists of two positive numbers (doubles) and exactly one operator like +, -, * or / always between these numbers. The string is dirty, which means that there are different characters inside too, not only numbers and the operator. You have to combine all digits left and right, perhaps with "." inside (doubles), and to calculate the result which has to be rounded to an integer and converted to a string at the end.
# Easy example:
# Input: "gdfgdf234dg54gf*23oP42"
# Output: "54929268" (because 23454*2342=54929268)
# First there are some static tests, later on random tests too...

def calculate_string(st): 
    st = [el for el in st if el in "1234567890/*-+."]
    st1 = "".join(st)
    for i, el in enumerate(st1):
        if el in "*/-+":
            pos = i
    a = float(st1[:pos])
    b = float(st1[pos+1:])
    
    if st1[pos] == "/":
        c = a / b
    if st1[pos] == "+":
        c = a + b
    if st1[pos] == "*":
        c = a * b
    if st1[pos] == "-":
        c = a - b
    return str(round(c))

# Solution 2

def calculate_string(st): 
    arr = [el for el in st if el.isnumeric() or el in '.+-*/']
    return str(round(eval("".join(arr))))

# Task 4.40. CamelCase Method
https://www.codewars.com/kata/587731fda577b3d1b0001196
# Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. All words must have their first letter capitalized without spaces.
# For instance:
# camelcase("hello case") => HelloCase
# camelcase("camel case word") => CamelCaseWord
# Don't forget to rate this kata! Thanks :)

def camel_case(string):
    return string.title().replace(" ","")

#
