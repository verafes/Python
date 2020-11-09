# Real code challenges. 
# Set #1. Completed_solutions 31-40

# Task 31. Beginner Series #4 Cockroach
https://www.codewars.com/kata/55fab1ffda3e2e44f00000c6
# The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).
# For example:
# cockroach_speed(1.08) == 30
# Note! The input is a Real number (actual type is language dependent) and is >= 0. The result should be an Integer.

def cockroach_speed(s):
    return int(s * 100000 / 3600)

# Task 32. Discover The Original Price
https://www.codewars.com/kata/552564a82142d701f5001228
# We need to write some code to return the original price of a product, the return type must be of type decimal and the number must be rounded to two decimal places.
# We will be given the sale price (discounted price), and the sale percentage, our job is to figure out the original price.

def discover_original_price(discounted_price, sale_percentage):
    return round(discounted_price / (1 - sale_percentage/100), 2)

# Task 33. Miles per gallon to kilometers per liter
https://www.codewars.com/kata/557b5e0bddf29d861400005d
# Create an application that will display the number of kilometers per liter (output) based on the number of miles per imperial gallon (input).
# Make sure to round off the result to two decimal points. If the answer ends with a 0, it should be rounded off without the 0. So instead of 5.50, we should get 5.5.
# Some useful associations relevant to this kata: 1 Imperial Gallon = 4.54609188 litres 1 Mile = 1.609344 kilometres

def converter(mpg):
    kml = mpg * 1.609344 / 4.54609188
    return round(kml, 2)

# Task 34. Triple Trouble
https://www.codewars.com/kata/5704aea738428f4d30000914/train/python
# Create a function that will return a string that combines all of the letters of the three inputed strings in groups. 
# Taking the first letter of all of the inputs and grouping them next to each other. Do this for every letter, see example below!
# E.g. Input: "aa", "bb" , "cc" => Output: "abcabc"
# Note: You can expect all of the inputs to be the same length.

def triple_trouble(one, two, three):
    str = ""
    for i in range(len(one)):
        str += one[i] + two[i] + three[i]
    return str

# Task 35. Formatting decimal places #1
https://www.codewars.com/kata/5641c3f809bf31f008000042
# Each floating-point number should be formatted that only the first two decimal places are returned. You don't need to check whether the input is a valid number because only valid numbers are used in the tests.
# Don't round the numbers! Just cut them after two decimal places!

def two_decimal_places(number):
    return int(number*100)/100

# Task 36. Happy Birthday, Darling!
https://www.codewars.com/kata/5e96332d18ac870032eb735f
# As you may know, once some people pass their teens, they jokingly only celebrate their 20th or 21st birthday, forever. 
# With some maths skills, that's totally possible - you only need to select the correct number base!
# For example, if they turn 32, that's exactly 20 - in base 16... Already 39? That's just 21, in base 19!
# Your task is to translate the given age to the much desired 20 (or 21) years, 
# and indicate the number base, in the format specified below.
# Note: input will be always > 21

def womens_age(n):
    if n%2 == 0:
        return f"{n}? That's just 20, in base {n//2}!"  
    else:
        return f"{n}? That's just 21, in base {n//2}!" 
		
# Solution 2
def womens_age(n):
    return f"{n}? That's just 2{n % 2}, in base {n // 2}!"

# Task 37. Third Angle of a Triangle
https://www.codewars.com/kata/5a023c426975981341000014
# You are given two interior angles (in degrees) of a triangle. Write a function to return the 3rd.
# Note: only positive integers will be tested.

def other_angle(a, b):
	if (a or b) < 0:
        return "angle cannot be smaller than 0"
    return 180 - (a + b)

# Task 38. DNA to RNA Conversion
https://www.codewars.com/kata/5556282156230d0e5e000089
# Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. 
# It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').
# Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. 
# In RNA Thymine is replaced by another nucleic acid Uracil ('U').
# Create a function which translates a given DNA string into RNA.
# For example: "GCAT"  =>  "GCAU"

def dna_to_rna(dna):
    return dna.replace("T","U")

# Task 39. Exes and Ohs
https://www.codewars.com/kata/55908aad6620c066bc00002a
# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
# Examples input/output:
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

def xo(s):
    count = 0
    for el in s:
        if el.lower() == "o":
            count += 1
        elif el.lower() == "x":
            count -= 1
    return True if count == 0 else False

# Solution #2
def xo(s):
    return s.lower().count('x') == s.lower().count('o')

# Task 40. MakeUpperCase
https://www.codewars.com/kata/57a0556c7cb1f31ab3000ad7
# Write a function which converts the input string to uppercase.

def make_upper_case(s):
    return s.upper()

