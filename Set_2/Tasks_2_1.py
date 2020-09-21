# Real code challenges. Set #2
# Completed_solutions 1-10

# Task 1. Convert boolean values to strings 'Yes' or 'No'.
https://www.codewars.com/kata/53369039d7ab3ac506000467
# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

def bool_to_word(boolean):
    return "Yes" if boolean == True else "No"
	
# Task 2. Keep Hydrated!
https://www.codewars.com/kata/582cb0224e56e068d800003c
# Nathan loves cycling.
# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
# You get given the time in hours and you need to return the number of litres Nathan will drink, 
# rounded to the smallest value.
# For example:
# time = 3 ----> litres = 1
# time = 6.7---> litres = 3
# time = 11.8--> litres = 5

def litres(time):
    return time // 2

# Task 3. How many times should I go?
https://www.codewars.com/kata/53369039d7ab3ac506000467
# Complete the method that takes a boolean value and return a "Yes" string for true, 
# or a "No" string for false.

def how_many_times(annual_price, individual_price):
    count = int(annual_price / individual_price)
    return count if annual_price % individual_price == 0 else count + 1

# Solution #2
https://www.codewars.com/kata/57efcb78e77282f4790003d8
# Lot of museum allow you to be a member, for a certain amount amount_by_year you can have unlimitted acces to the museum.
# In this kata you should complete a function in order to know after how many visit it will be better to take an annual pass. 
#  The function take 2 arguments annual_price and individual_price.

import math
def how_many_times(annual_price, individual_price):
    return math.ceil(annual_price/individual_price)
	
# Task 4. Number of Decimal Digits
https://www.codewars.com/kata/58fa273ca6d84c158e000052
# Determine the total number of digits in the integer (n>=0) given as input to the function. 
# For example, 9 is a single digit, 66 has 2 digits and 128685 has 6 digits. 
# Be careful to avoid overflows/underflows.

def digits(n):
    return len(str(n))

# Task 5. 
	
# Task 6.
	
# Task 7. 

# Task 8. 

# Task 9. 
		
# Task 0. 