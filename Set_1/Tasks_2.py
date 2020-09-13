# Real code challenges. 
# Completed_solutions 11-20

# Task 11. Grasshopper - Terminal game move function
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

# Task 12. 8 inch pizza equivalence
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
    slices = round((area/8)%(area8/8))
    return (f"pizzas: {pizzas}, slices: {slices}")

print ("pizzas, slices", how_many_pizzas(n))

# Task 4. 

# Task 5. 
	
# Task #6.
	
# Task 7. 

# Task 8. 

# Task 19. 
		
# Task 20. 




	

