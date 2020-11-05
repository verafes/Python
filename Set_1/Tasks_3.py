# Real code challenges. 
# Set#1. Completed solutions 21-30

# Task 21. How many times should I go? 
# Lot of museum allow you to be a member, 
# for a certain amount amount_by_year you can have unlimitted acces to the museum.
# In this kata you should complete a function in order to know after 
# how many visit it will be better to take an annual pass. 
# The function take 2 arguments annual_price and individual_price.
# Test.describe('Basic Tests')
# Test.assert_equals(how_many_times(40,15), 3)
# Test.assert_equals(how_many_times(30,10), 3)
# Test.assert_equals(how_many_times(80,15), 6)

import math
def how_many_times(annual_price, individual_price):
    return math.ceil(annual_price/individual_price)
	

# Solution #2
def how_many_times(annual_price, individual_price):
    count = int(annual_price / individual_price)
    return count if annual_price % individual_price == 0 else count + 1

annual_price = int(input("Enter annual price:")) 
individual_price = int(input("individual price: "))

print(how_many_times(annual_price, individual_price))

# Task 22. Number of Decimal Digits 
https://www.codewars.com/kata/58fa273ca6d84c158e000052
# Determine the total number of digits in the integer (n>=0) given as input to the function. 
# For example, 9 is a single digit, 66 has 2 digits and 128685 has 6 digits. 
# Be careful to avoid overflows/underflows. All inputs will be valid.
# Example:
# digits(5) -> 1
# digits(12345) -> 5
# digits(9876543210) -> 10

def digits(n):
    return len(str(n))

n = int(input("Enter any number:"))
print(digits(n))

# Task 23. Over The Road
https://www.codewars.com/kata/58fa273ca6d84c158e000052
# You've just moved into a perfectly straight street with exactly n identical houses on either side of the road. 
# Naturally, you would like to find out the house number of the people on the other side of the street. 
# The street looks something like this:
# Street
# 1|   |6
# 3|   |4
# 5|   |2
# Evens increase on the right; odds decrease on the left. House numbers start at 1 and increase without gaps. 
# When n = 3, 1 is opposite 6, 3 opposite 4, and 5 opposite 2.
# Example 
# Given your house number address and length of street n, give the house number on the opposite side of the street.
# over_the_road(address, n)
# over_the_road(1, 3) = 6
# over_the_road(3, 3) = 4
# over_the_road(2, 3) = 5
# over_the_road(3, 5) = 8
# Both n and address could get upto 500 billion with over 200 random tests.

def over_the_road(address, n):
    return ((n * 2 + 1) - address)

address = int(input("Enter address:")) 
n = int(input("Number of houses: "))

print(over_the_road(address, n))

# Task 24. Opposite number
https://www.codewars.com/kata/56dec885c54a926dcd001095
# Very simple, given a number, find its opposite. 
# Examples: 1: -1, -34: 34

def opposite(number): 
	return -number

# Task 5. Count Odd Numbers below n
https://www.codewars.com/kata/59342039eb450e39970000a6/python

# Given a number n, return the number of positive odd numbers below n, EASY!

# oddCount(7) //=> 3, i.e [1, 3, 5] 
# oddCount(15) //=> 7, i.e [1, 3, 5, 7, 9, 11, 13]

def odd_count(n):
    if n < 1:
        return 0
    else:
        return n // 2

n = int(input("Enter n: "))
print(oddCount(n))

# Task 25. Expressions Matter
https://www.codewars.com/kata/5ae62fcf252e66d44d00008e

# Given three integers a ,b ,c, return the largest number obtained after inserting 
# the following operators and brackets: +, *, () 
# In other words , try every combination of a,b,c with [*+()], 
# and return the Maximum Obtained

# !!! Notes
# The numbers are always positive. 
# The numbers are in the range (1 ≤ a, b, c ≤ 10).
# You can use the same operation more than once.
# It's not necessary to place all the signs and brackets.
# Repetition in numbers may occur.
# You cannot swap the operands. For instance, 
# in the given example you cannot get expression (1 + 3) * 2 = 8.

def expressionsMatter(a,b,c):
  # for i in range(1,10):
  # for i in range(1,10):
    if a <= 0 or b<= 0 or c <= 0:
      return ("Error. Value of a, b, c should be greater than zero")
    else:
      n1 = a * (b + c) 
      n2 = a * b * c
      n3 = a + b * c
      n4 = (a + b) * c
      n5 = a + b + c
      n6 = a * b + c
    return(max(n1, n2, n3, n4, n5, n6))
	
a = int(input("Enter integer for a: "))
b = int(input("Enter integer for c: "))
c = int(input("Enter integer for c: "))

print(expressionsMatter(a,b,c))

# Task 26. Sum of angles
# Find the total sum of internal angles (in degrees) in an n-sided simple polygon. 
# N will be greater than 2.

def angle(n):
    return 180 * (n - 2)

n = int(input("Enter number of sides of a regular polygon: "))
print(angle(n))

# Task 27.	Convert a Number to a String!
https://www.codewars.com/kata/557b5e0bddf29d861400005d
# We need a function that can transform a number into a string.
# What ways of achieving this do you know?
# Examples:
# number_to_string(123) /* returns '123' */
# number_to_string(999) /* returns '999' */

def number_to_string(num):
    # Return a string of the number here!
    return str(num)

# Task 28. Drone Fly-By
https://www.codewars.com/kata/5265326f5fda8eb1160004c8
# The other day I saw an amazing video where a guy hacked some wifi controlled lightbulbs by flying 
# a drone past them. Brilliant.
# In this kata we will recreate that stunt... sort of.
# You will be given two strings: lamps and drone. 
# lamps represents a row of lamps, currently off, each represented by x. 
# When these lamps are on, they should be represented by o.
# The drone string represents the position of the drone T (any better suggestion for character??) and its flight path up until this point =. 
# The drone always flies left to right, and always begins at the start of the row of lamps. 
# Anywhere the drone has flown, including its current position, 
# will result in the lamp at that position switching on.
# Return the resulting lamps string. See example tests for more clarity.

Return the resulting lamps string. See example tests for more clarity.
def fly_by(lamps, drone):
    lend = len(drone)
    lenl = len(lamps)
    return lend * "o" + (lenl - lend)*'x' if lend <= lenl else lenl*"o"

# Task 29. Breaking chocolate problem
https://www.codewars.com/kata/534ea96ebb17181947000ada
# Your task is to split the chocolate bar of given dimension n x m into small squares. 
# Each square is of size 1x1 and unbreakable. 
# Implement a function that will return minimum number of breaks needed.
# For example if you are given a chocolate bar of size 2 x 1 you can split it 
# to single squares in just one break, but for size 3 x 1 you must do two breaks.
# If input data is invalid you should return 0 (as in no breaks are needed 
# if we do not have any chocolate to split). Input will always be a non-negative integer.

def breakChocolate(n, m):
    return m*n-1 if n > 0 and m > 0 else 0
#
# Task 30. I love you, a little , a lot, passionately ... not at all
https://www.codewars.com/kata/57f24e6a18e9fad8eb000296
# Who remembers back to their time in the schoolyard, 
# when girls would take a flower and tear its petals, 
# saying each of the following phrases each time a petal was torn:
# I love you, a little, a lot, passionately, madly, not at all
# When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.
# Your goal in this kata is to determine which phrase the girls would say for a flower of a given number of petals, where nb_petals > 0.

def how_much_i_love_you(nb_petals):
    n = nb_petals % 6 
    m = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"] 
    return m[n-1]
#