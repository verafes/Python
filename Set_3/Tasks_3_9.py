# Real code challenges. Set #3
# Completed_solutions 81-90

#  Task 381. A wolf in sheep's clothing
https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15
# Wolves have been reintroduced to Great Britain. You are a sheep farmer, and are now plagued by wolves which pretend to be sheep. 
# Fortunately, you are good at spotting them.
# Warn the sheep in front of the wolf that it is about to be eaten. 
# Remember that you are standing at the front of the queue which is at the end of the array.
# If the wolf is the closest animal to you, return "Pls go away and stop eating my sheep". 
# Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue.
# Note: there will always be exactly one wolf in the array.

def warn_the_sheep(queue):
    s = queue[::-1].index('wolf')
    return f'Pls go away and stop eating my sheep' if s <= 0 else f'Oi! Sheep number {s}! You are about to be eaten by a wolf!'


# Task 382. Debug Basic Calculator 
https://www.codewars.com/kata/56368f37d464c0a43c00007f
# Debug a function called calculate that takes 3 values. The first and third values are numbers. The second value is a character. 
# If the character is "+" , "-", "*", or "/", the function will return the result of the corresponding mathematical function on the two numbers. 
# If the string is not one of the specified characters, the function should return null.

def calculate (a, o, b):
    if o == "+":
        return a + b
    if o == "-":
        return a - b
    if o == "*":
        return a * b
    if o == "/" and  b != 0:
        return a / b
    else:
        return None

# Task 383. Simple multiplication
https://www.codewars.com/kata/583710ccaa6717322c000105
# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

def simple_multiplication(number) :
    return number * (8 + number%2)

# Task 384. How much water do I need?
https://www.codewars.com/kata/575fa9afee048b293e000287
# My washing machine uses water amount of water to wash clothes amount of clothes. You are given a load amount of clothes to wash. For each single item of load above the standard amount of clothes, the washing machine will use 10% more water (multiplicative) to clean. For example, if the amount of clothes is 10, the amount of water it requires is 5 and the load is 14, then you need 5 * 1.1 ^ (14 - 10) amount of water.
# Write a function howMuchWater (JS)/how_much_water (Python) to work out how much water is needed if you have a clothes amount of clothes. The function will accept 3 parameters - howMuchWater(water, load, clothes) / how_much_water(water, load, clothes)
# My washing machine is an old model that can only handle double the amount of load. If the amount of clothes is more than 2 times the standard amount of load, return 'Too much clothes'. The washing machine also cannot handle any amount of clothes less than load. If that is the case, return 'Not enough clothes'.
# The answer should be rounded to the nearest 2 decimal places.

def how_much_water(water, load, clothes):
    if clothes > load * 2:
        return "Too much clothes"
    
    if clothes < load:
        return "Not enough clothes"

    return round(water * 1.1 ** (clothes - load), 2)

# Task 385. Between Extremes
https://www.codewars.com/kata/56d19b2ac05aed1a20000430
# Given an array of numbers, return the difference between the largest and smallest values.
# For example:
# [23, 3, 19, 21, 16] should return 20 (i.e., 23 - 3).
# [1, 434, 555, 34, 112] should return 554 (i.e., 555 - 1).
# The array will contain a minimum of two elements. Input data range guarantees that max-min will cause no integer overflow.

def between_extremes(numbers):
    if [numbers[0]]*len(numbers) == numbers:
        return 0
    else:
        return max(numbers) - min(numbers)

# Task 386. Count cubes in a Menger Sponge
https://www.codewars.com/kata/59d28768a25c8c51a6000057
# In this kata you will create a function that takes non negative integers (from 0 to n) 
# and return the amount of cubes that the Menger Sponge would have in that specific iteration.

def calc_ms(n):
    return 20 ** n
	
# Task 387. How old will I be in 2099?
https://www.codewars.com/kata/5761a717780f8950ce001473
# Philip's just turned four and he wants to know how old he will be in various years in the future such as 2090 or 3044. 
# His parents can't keep up calculating this so they've begged you to help them out by writing a programme that can answer Philip's endless questions.
# Your task is to write a function that takes two parameters: the year of birth and the year to count years in relation to. 
# As Philip is getting more curious every day he may soon want to know how many years it was until he would be born, so your function needs to work with both dates in the future and in the past.
# Provide output in this format: For dates in the future: "You are ... year(s) old." For dates in the past: "You will be born in ... year(s)." 
# If the year of birth equals the year requested return: "You were born this very year!"
# "..." are to be replaced by the number, followed and proceeded by a single space. Mind that you need to account for both "year" and "years", depending on the result.

def calculate_age(year_of_birth, current_year):
    y = current_year - year_of_birth
    if y == 0:
        return 'You were born this very year!'
    if y == -1:
        return 'You will be born in 1 year.'
    if y == 1:
        return f"You are 1 year old." 
    if y < 0: 
        return f"You will be born in {abs(y)} years."
    if y > 1:
        return f"You are {abs(y)} years old." 


# Task 388. Multiplication table for number
https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce
# Your goal is to return multiplication table for number that is always an integer from 1 to 10. 
# P. S. You can use \n in string to jump to the next line.

def multi_table(n):
    return "\n".join([f"{el} * {n} = {el*n}"  for el in range (1,11)]) 

# Task 389. Nth power rules them all!
https://www.codewars.com/kata/58aed2cafab8faca1d000e20
# You are provided with an array of positive integers and an additional integer n (n > 1).
# Calculate the sum of each value in the array to the nth power. Then subtract the sum of the original array.
# Examples
# {1, 2, 3}, 3  -->  (1^3 + 2^3 + 3^3 ) - (1 + 2 + 3)  -->  36 - 6  -->  30
# {1, 2}, 5     -->  (1^5 + 2^5) - (1 + 2)             -->  33 - 3  -->  30

def modified_sum(a, n):
    return sum([el**n for el in a]) - sum(a)

# Task 390. Regex count lowercase letters
https://www.codewars.com/kata/56a946cd7bd95ccab2000055
# Your task is simply to count the total number of lowercase letters in a string.
# Examples: lowercaseCount("abc"); ===> 3, lowercaseCount("abcABC123"); ===> 3

def lowercase_count(strng):
    return (len([x for x in strng if x.islower()]))

#
