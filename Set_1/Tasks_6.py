# Real code challenges. 
# Set #1. Completed_solutions 61-70

# Task 41. Initialize my name
https://www.codewars.com/kata/5768a693a3205e1cc100071f
# Some people just have a first napaypalme; some people have first and last names and some people have first, middle and last names.
#You task is to initialize the middle names (if there is any).
#Examples
#'Jack Ryan'                   => 'Jack Ryan'
#'Lois Mary Lane'              => 'Lois M. Lane'
#'Dimitri'                     => 'Dimitri'
#'Alice Betty Catherine Davis' => 'Alice B. C. Davis'

def initialize_names(name):
    l = name.split()
    for i in range(1, len(l)-1):
        l[i] = l[i][0] + '.'
    return ' '.join(l)

# Task 42. Sum The Strings
https://www.codewars.com/kata/5966e33c4e686b508700002d
# Create a function that takes 2 positive integers in form of a string as an input, and outputs the sum (also as a string):
#  sumStr("4", "5")    // should output "9"
#  sumStr("34", "5")   // should output "39"
# If either input is an empty string, consider it as zero.

def sum_str(a, b):
    return str(int('0' + a) + int('0' + b))

# Task 43. Validate code with simple regex
https://www.codewars.com/kata/56a25ba95df27b7743000016
#Basic regex tasks. Write a function that takes in a numeric code of any length. 
#The function should check if the code begins with 1, 2, or 3 and return true if so. Return false otherwise.
#You can assume the input will always be a number.
	
def validate_code(code):
    return str(code).startswith(('1', '2', '3'))
	
# Task 44. repeatIt
https://www.codewars.com/kata/557af9418895e44de7000053
# Create a function that takes a string and an integer (n).
# The function should return a string that repeats the input string n number of times.
# If anything other than a string is passed in you should return "Not a string"

def repeat_it(string,n):
    return string*n if type(string) is str else 'Not a string'


# Task 45. Tortoise racing
https://www.codewars.com/kata/55e2adece53b4cdcb900006c
# Two tortoises named A and B must run a race. A starts with an average speed of 720 feet per hour. 
# Young B knows she runs faster than A, and furthermore has not finished her cabbage.
# When she starts, at last, she can see that A has a 70 feet lead but B's speed is 850 feet per hour. How long will it take B to catch A?
# More generally: given two speeds v1 (A's speed, integer > 0) and v2 (B's speed, integer > 0) and a lead g (integer > 0) how long will it take B to catch A?
# The result will be an array [hour, min, sec] which is the time needed in hours, minutes and seconds (round down to the nearest second) or a string in some languages.
# If v1 >= v2 then return nil, nothing, null, None or {-1, -1, -1} for C++, C, Go, Nim, [] for Kotlin or "-1 -1 -1".

def race(v1, v2, g):
    if v1 <= v2:
        return None
    else:
        t = g/(v2-v1)*3600
        hour = int(t//3600)
        min = int((t - hour*3600)//60)
        sec = int(t - (hour*3600 + min*60))
        return [hour, min, sec]

# Task 45. Are You Playing Banjo?
https://www.codewars.com/kata/53af2b8861023f1d88000832
# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
#The function takes a name as its only argument, and returns one of the following strings:
# name + " plays banjo" 
# name + " does not play banjo"

def areYouPlayingBanjo(name):
    return f"{name} plays banjo" if name.startswith(("R", "r")) else f"{name} does not play banjo"

# Task 47. Cat years, Dog years
https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b
# I have a cat and a dog. I got them at the same time as kitten/puppy. That was humanYears years ago.
# Return their respective ages now as [humanYears,catYears,dogYears]
# NOTES: humanYears >= 1, humanYears are whole numbers only
#Cat Years
#15 cat years for first year
#+9 cat years for second year
#+4 cat years for each year after that
#Dog Years
#15 dog years for first year
#+9 dog years for second year
#+5 dog years for each year after that

def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        cat = 15
        dog = 15
    elif human_years == 2:
        cat = 24
        dog = 24
    else: 
        cat = 24 + (human_years-2)*4
        dog = 24 + (human_years-2)*5
    return [human_years, cat, dog]

# Task 48. Beginner Series #1 School Paperwork
https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd
# Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.
# Your task is to calculate how many blank pages do you need.
# Example: paperwork(5, 5) == 25, Note: if n < 0 or m < 0 return 0!

def paperwork(n, m):
    if n < 0 or m < 0: 
        return 0
    return n * m

# Task 49. Calculate BMI
https://www.codewars.com/kata/57a429e253ba3381850000fb
# Write function bmi that calculates body mass index (bmi = weight / height ^ 2).
#if bmi <= 18.5 return "Underweight"
#if bmi <= 25.0 return "Normal"
#if bmi <= 30.0 return "Overweight"
#if bmi > 30 return "Obese"

def bmi(weight, height):
    bmi = weight / height**2
    if bmi <= 18.5: return "Underweight"
    if bmi <= 25.0: return "Normal"
    if bmi <= 30.0: return "Overweight"
    if bmi > 30: return "Obese"

# Task 50. Calculate Two People's Individual Ages
https://www.codewars.com/kata/58e0bd6a79716b7fcf0013b1
# Create a function that takes in the sum and age difference of two people, calculates their individual ages, 
# and returns a pair of values (oldest age first) if those exist or null/None if:
# sum < 0, difference < 0 -> Either of the calculated ages come out to be negative

def get_ages(sum, difference):
    if sum < 0 or difference < 0 or sum < difference:
        return None
    a = (sum + difference)/2
    b = sum - a
    if sum == difference:
        return a, 0
    return a, b
