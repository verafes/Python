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

# Task 5. 

# 


# Task 6. 
	
# 


# Task 7. 

# 


# Task 8. 

# 


# Task 9. 
 
# 


# Task 0.

# 


#
