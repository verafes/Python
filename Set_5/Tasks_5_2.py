# Real code challenges. Set #5
# Completed_solutions 511-520

#  Task 511. Jumping Number (Special Numbers Series 
https://www.codewars.com/kata/5a54e796b3bfa8932c0000ed
# Definition. # Jumping number is the number that All adjacent digits in it differ by 1.
# Task. # Given a number, Find if it is Jumping or not .
# Notes. Number passed is always Positive .
# Return the result as String .
# The difference between ‘9’ and ‘0’ is not considered as 1 .
# All single digit numbers are considered as Jumping numbers.

# Input >> Output Examples
# jumpingNumber(9) ==> return "Jumping!!" - Explanation: It's single-digit number
# jumpingNumber(79) ==> return "Not!!" - Explanation: Adjacent digits don't differ by 1
# jumpingNumber(23) ==> return "Jumping!!" - Explanation: Adjacent digits differ by 1
# jumpingNumber(556847) ==> return "Not!!" - Explanation: Adjacent digits don't differ by 1

def jumping_number(number):
    s = 0 
    if number < 10: return 'Jumping!!'
    for i in range(len(str(number))):
        dif = abs(int(str(number)[i]) - int(str(number)[i-1]))
        if  dif == 1: s += 1
    return "Not!!" if s < len(str(number))-1 else 'Jumping!!' 
 
# Task 512. Special Number (Special Numbers Series #5)
https://www.codewars.com/kata/5a55f04be6be383a50000187/
# Definition. A number is a Special Number if it’s digits only consist 0, 1, 2, 3, 4 or 5
# Given a number determine if it special number or not .
# Notes. The number passed will be positive (N > 0) .
# All single-digit numbers with in the interval [0:5] are considered as special number.

def special_number(number):
    num = [digit for digit in str(number) if digit in "012345"]
    return "Special!!" if len(num) == len(str(number)) else "NOT!!"

# Task 513. Disarium Number (Special Numbers Series #3)
https://www.codewars.com/kata/5a53a17bfd56cb9c14000003
# Definition. Disarium number is the number that The sum of its digits powered with their respective positions is equal to the number itself.
# Task. Given a number, Find if it is Disarium or not .
#  Input >> Output Examples
# disariumNumber(89) ==> return "Disarium !!"
# Explanation: Since , 81 + 92 = 89 , thus output is "Disarium !!"
# disariumNumber(564) ==> return "Not !!"
# Explanation:
# Since , 51 + 62 + 43 = 105 != 564 , thus output is "Not !!"

def disarium_number(number):
    arr = [int(digit)**(i+1) for i, digit in enumerate(str(number))]
    return 'Disarium !!' if sum(arr) == number else 'Not !!'

# Task 514. https://www.codewars.com/kata/5a4e3782880385ba68000018
Balanced Number (Special Numbers Series #1 )
# Definition. Balanced number is the number that * The sum of all digits to the left of the middle digit(s) 
# and the sum of all digits to the right of the middle digit(s) are *equal**.
# Task. Given a number, Find if it is Balanced or not .
# Notes.
# If the number has an odd number of digits then there is only one middle digit, e.g. 92645 has middle digit 6; 
# otherwise, there are two middle digits , e.g. 1301 has middle digits 3 and 0
# The middle digit(s) should not be considered when determining whether a number is balanced or not, 
# e.g 413023 is a balanced number because the left sum and right sum are both 5.
# Number passed is always Positive. Return the result as String.

def balanced_num(number):
    i = int(len(str(number)) / 2)
    if (len(str(number)))%2 != 0:
        left = [int(d) for d in str(number)[:i]]
    else:        
        left = [int(d) for d in str(number)[:i-1]]
    right = [int(d) for d in str(number)[i+1:]]
    return "Balanced" if int(len(str(number))) <= 2 or sum(left) == sum(right) else 'Not Balanced'

# Task 515. By 3, or not by 3? That is the question . . .
https://www.codewars.com/kata/59f7fc109f0e86d705000043
# A trick I learned in elementary school to determine whether or not a number was divisible by three 
# is to add all of the integers in the number together and to divide the resulting sum by three. 
# If there is no remainder from dividing the sum by three, then the original number is divisible by three as well.
# Given a series of digits as a string, determine if the number represented by the string is divisible by three.
# You can expect all test case arguments to be strings representing values greater than 0.
# Example:
# "123"      -> true
# "8409"     -> true
# "100853"   -> false
# "33333333" -> true
# "7"        -> false
# Try to avoid using the % (modulo) operator.

def divisible_by_three(st): 
    s = 0
    for el in st:
        s += int(el)
    while int(s) > 0:
        s -= 3
    return s == 0

# Task 516. Powers of 3
https://www.codewars.com/kata/57be674b93687de78c0001d9
# Given a positive integer N, return the largest integer k such that 3^k < N.
# For example,
# largest_power(3) == 0
# largest_power(4) == 1
# You may assume that the input to your function is always a positive integer.

def largest_power(N):
    i=0
    while 3**i < N:
        i+=1
    return i-1

# Task 517. CubeSummation
https://www.codewars.com/kata/550e9fd127c656709400024d
# Write a function cubeSum(n, m) that will calculate a sum of cubes of numbers in a given range, 
# starting from the smaller (but not including it) to the larger (including). 
# The first argument is not necessarily the larger number.
# If both numbers are the same, then the range is empty and the result should be 0.
# Examples:
# cube_sum(2,3); # => 3^3 = 27
# cube_sum(3,2); # => 3^3 = 27
# cube_sum(0,4); # => 1^3+2^3+3^3+4^3 = 100
# cube_sum(17, 14); # => 15^3+16^3+17^3 = 12384
# cube_sum(9, 9); # => 0

def cube_sum(n, m):
    if n > m:
        n, m = m, n
    return sum([x**3 for x in range(n+1,m+1)])

# Task 518. Get the square of a number without ** or * or pow()
https://www.codewars.com/kata/58a8807c5336a3f613000157
# #Task: Write a function that gets a square of a number without the following:
# Your code musn't contain any *s and you cannot use the pow function. Edit: You also cannot use **__mul__ function**
# You cannot import any external libraries (unless you are satisfied with random being pre-imported).
# Only one function can be defined.
# Your code must be under or equal to 50 characters (and you already have to use 6 for the function name).
# Loophole solutions will not be accepted.
# If I use test.expect in my restriction tests, that is okay. This is not an issue.
# Input will always be positive or 0

def square(n):
    return sum(range(1, n+n, 2))

# Solution 2:
	
def square(n):
    return sum(n for i in range(n))

# Task 519. Square root without using library : math
https://www.codewars.com/kata/5979d27b630baf1509000064
# The challenge to you is to return the square root of the integers. You will only be given perfect square numbers.
# Restrictions are as follows:
# You're not allowed to use the word require in your code.
# You're not allowed to use the ** 

def square_root_me(sqrt):
    x = sqrt
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + sqrt // x) // 2
    return x

# Task 520. To square(root) or not to square(root)
https://www.codewars.com/kata/57f6ad55cca6e045d2000627
# You are the host of a game show that only allows people whose height in centimeters is a perfect square. 
# A perfect square is a number that is the result of a single whole number being multiplied by itself.
# For example, a person who is 169 cm (13 * 13) tall would be able to get in, but a person who is 173 cm tall would not.
# You can assume that all given heights will be whole, and positive. All true outputs should evaluate to be whole numbers.

def square_or_square_root(arr):
    lst = []
    for n in arr:
        # check if a number is an perfect square
        if n**0.5 == int(n**0.5):
            lst.append(n**0.5)
        else:
            lst.append(n**2)
    return lst

#
