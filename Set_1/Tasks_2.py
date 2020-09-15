# Real code challenges. 
# Completed_solutions 11-20

# Task 11. Abbreviate a Two Word Name
https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3
# Write a function to convert a name into initials. 
# This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:

# Sam Harris => S.H
# Patrick Feeney => P.F

def abbrev_name(name):
    name = name.title()
    space = name.find(" ")
    return f"{name[0]}.{name[space+1]}"

# Task #12. Case swapping
https://www.codewars.com/kata/5590961e6620c0825000008f
# Given a string, swap the case for each of the letters.
# e.g. CodEwArs --> cODeWaRS
# Examples
# ""           ->   ""
# "CodeWars"   ->   "cODEwARS"
# "abc"        ->   "ABC"
# "ABC"        ->   "abc"
# "123235"     ->   "123235"

def swap(string):
    return string.swapcase()
	
# Task #13. Correct the mistakes of the character recognition software
# Character recognition software is widely used to digitise printed texts. 
# Thus the texts can be edited, searched and stored on a computer.
# When documents (especially pretty old ones written with a typewriter), 
# are digitised character recognition softwares often make mistakes.

# Your task is correct the errors in the digitised text. You only have to handle the following mistakes:
# S is misinterpreted as 5
# O is misinterpreted as 0
# I is misinterpreted as 1
# The test cases contain numbers only by mistake.

def correct(string):
    return string.replace("5", "S").replace("0", "O").replace("1", "I")

# Task #14. Remove the time
https://www.codewars.com/kata/56b0ff16d4aa33e5bb00008e

# You're re-designing a blog and the blog's posts have the following format for showing the date and time a post was made:
# Weekday Month Day, time e.g., Friday May 2, 7pm

# You're running out of screen real estate, and on some pages you want to display a shorter format, 
# Weekday Month Day that omits the time.
# Write a function, shortenToDate, that takes the Website date/time in its original string format, 
# and returns the shortened format.

# Assume shortenToDate's input will always be a string, e.g. "Friday May 2, 7pm". 
# Assume shortenToDate's output will be the shortened string, e.g., "Friday May 2".

def shorten_to_date(long_date):
    comma = long_date.find(",")
    return long_date[0:comma]

# Solution 2
def shorten_to_date(long_date):
    return long_date.split(',')[0]


# Task #15. Who ate the cookie?
https://www.codewars.com/kata/55a996e0e8520afab9000055
# For this problem you must create a program that says who ate the last cookie. If the input is a string then "Zach" ate the cookie. If the input is a float or an int then "Monica" ate the cookie. If the input is anything else "the dog" ate the cookie. The way to return the statement is: "Who ate the last cookie? It was (name)!"
# Ex: Input = "hi" --> Output = "Who ate the last cookie? It was Zach! (The reason you return Zach is because the input is a string)
# Note: Make sure you return the correct message with correct spaces and punctuation.
# Please leave feedback for this kata. Cheers!

def cookie(x):
    if type(x) == str:
        return "Who ate the last cookie? It was Zach!"
    elif type(x) == bool:
        return "Who ate the last cookie? It was the dog!"
    else: 
        return "Who ate the last cookie? It was Monica!"

# Task #16. Is this my tail?
https://www.codewars.com/kata/56f695399400f5d9ef000af5
# Some new animals have arrived at the zoo. 
# The zoo keeper is concerned that perhaps the animals do not have the right tails. 
# To help her, you must correct the broken function to make sure that the second argument (tail), 
#is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
# If the tail is right return true, else return false.
# The arguments will always be strings, and normal letters.
# For Haskell, body has the type of String and tail has the type of Char. 
# For Go, body has type string and tail has type rune.

def correct_tail(body, tail):
     return body[-1] == tail


# Task 17. Grasshopper - Terminal game move function
https://www.codewars.com/kata/563a631f7cbbc236cf0000c2

# In this game, the hero moves from left to right. 
# The player rolls the dice and moves the number of spaces indicated by the dice two times.
# Create a function for the terminal game that takes the current position of the hero 
# and the roll (1-6) and return the new position.

# Example:
# move(3, 6) should equal 15

position = int(input("position: "))
roll = int(input("roll: "))

def move(position, roll):
  if roll < 1 or roll > 6:
    return "Error"
  else:
    new_position = position + (roll * 2)
    return(new_position)

print(move(position, roll))

# Task 18. 8 inch pizza equivalence
# How much bigger is a 16-inch pizza compared to an 8-inch pizza? 
# A more pragmatic question is: How many 8-inch pizzas "fit" in a 16-incher?

# The answer, as it turns out, is exactly four 8-inch pizzas. 
# For sizes that don't correspond to a round number of 8-inchers, you must round the number of slices 
# (one 8-inch pizza = 8 slices), e.g.:
# how_many_pizzas(16) -> "pizzas: 4, slices: 0"
# how_many_pizzas(12) -> "pizzas: 2, slices: 2"
# how_many_pizzas(8) -> "pizzas: 1, slices: 0"
# how_many_pizzas(6) -> "pizzas: 0, slices: 4"
# how_many_pizzas(0) -> "pizzas: 0, slices: 0"

n = int(input("Please enter the diameter of the pizza: "))

def how_many_pizzas(n):
  import math
  area = math.pi * (n/2)**2
  area8 = math.pi * 4**2
  if n <= 0:
    return 0
  else: 
    pizzas = math.floor(area//area8)
    over_slices = round((area/8)%(area8/8))
	slices = math.floor(over_slices/(area8/8))
    return (f"pizzas: {pizzas}, slices: {slices}")

print (how_many_pizzas(n))

# Solution 2
def how_many_pizzas(n): 
  return f"pizzas: {(n ** 2) // 64}, slices: {(n ** 2) % 64 // 8}"
  
print (how_many_pizzas(n))


# Task 19. Holiday VIII - Duty Free
https://www.codewars.com/kata/57e92e91b63b6cbac20001e5/train/python

# The purpose of this kata is to work out just how many bottles of duty free whiskey 
# you would have to buy such that the saving over the normal high street price 
# would effectively cover the cost of your holiday.

# You will be given the high street price (normPrice), the duty free discount (discount) and the cost of the holiday.

# For example, if a bottle cost £10 normally and the discount in duty free was 10%, you would save £1 per bottle. 
#If your holiday cost £500, the answer you should return would be 500.

# All inputs will be integers. Please return an integer. Round down.
# Test.describe("Basic tests")
# Test.assert_equals(duty_free(12, 50, 1000), 166)
# Test.assert_equals(duty_free(17, 10, 500), 294

def duty_free(price, discount, holiday_cost):
      return int(holiday_cost // ( price * (discount / 100)))


# Task #20.
	





	

