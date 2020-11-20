# Real code challenges. Set #1
# Completed_solutions 71-80

# Task 71. L1: Set Alarm
https://www.codewars.com/kata/568dcc3c7f12767a62000038/train/python
# Write a function named setAlarm which receives two parameters. The first parameter, employed, 
# is true whenever you are employed and the second parameter, vacation is true whenever you are on vacation.
# The function should return true if you are employed and not on vacation 
# (because these are the circumstances under which you need to set an alarm). It should return false otherwise. Examples:
# setAlarm(true, true) -> false
# setAlarm(false, true) -> false
# setAlarm(false, false) -> false
# setAlarm(true, false) -> true

def set_alarm(employed, vacation):
    return employed and not vacation 

# Task 72. Cat and Mouse - Harder Version
https://www.codewars.com/kata/57ee2a1b7b45efcf700001bf
# You will be given a string (x) featuring a cat 'C', a dog 'D' and a mouse 'm'. The rest of the string will be made up of '.'.
# You need to find out if the cat can catch the mouse from it's current position. The cat can jump (j) characters.
# Also, the cat cannot jump over the dog.
# So: if j = 5:
# ..C.....m. returns 'Caught!' <-- not more than j characters between
# .....C............m...... returns 'Escaped!' <-- as there are more than j characters between the two, the cat can't jump far enough
# if j = 10:
# ...m.........C...D returns 'Caught!' <--Cat can jump far enough and jump is not over dog
# ...m....D....C....... returns 'Protected!' <-- Cat can jump far enough, but dog is in the way, protecting the mouse
# Finally, if all three animals are not present, return 'boring without all three'

def cat_mouse(x,j):
    cat = x.index("C") if x.count("C") == 1 else 0
    dog = x.index("D") if x.count("D") == 1 else 0
    mouse = x.index("m") if x.count("m") == 1 else 0
    if cat == 0 or dog == 0 or mouse == 0:
        return "boring without all three"
    elif (cat < dog < mouse or mouse < dog < cat):
        if abs(cat-mouse)<= j:
            return "Protected!"
        else:
            return "Escaped!"
    elif abs(cat-mouse)<= j:
        return "Caught!"
    else:
        return "Escaped!"

# Task 73. Simple Fun #1: Seats in Theater
https://www.codewars.com/kata/588417e576933b0ec9000045
# Your friend advised you to see a new performance in the most popular theater in the city. He knows a lot about art and his advice is usually good, but not this time: the performance turned out to be awfully dull. It's so bad you want to sneak out, which is quite simple, especially since the exit is located right behind your row to the left. All you need to do is climb over your seat and make your way to the exit.
# The main problem is your shyness: you're afraid that you'll end up blocking the view (even if only for a couple of seconds) of all the people who sit behind you and in your column or the columns to your left. To gain some courage, you decide to calculate the number of such people and see if you can possibly make it to the exit without disturbing too many people.
# Given the total number of rows and columns in the theater (nRows and nCols, respectively), and the row and column you're sitting in, return the number of people who sit strictly behind you and in your column or to the left, assuming all seats are occupied.
# Example: For nCols = 16, nRows = 11, col = 5 and row = 3, the output should be == 96

def seats_in_theater(tot_cols, tot_rows, col, row):
    return (tot_cols - col + 1) * (tot_rows - row)
	
# Task 74. What's the real floor?
https://www.codewars.com/kata/574b3b1599d8f897470018f6
# Americans are odd people: in their buildings, the first floor is actually the ground floor and there is no 13th floor (due to superstition).
# Write a function that given a floor in the american system returns the floor in the european system.
# With the 1st floor being replaced by the ground floor and the 13th floor being removed, the numbers move down to take their place. In case of above 13, they move down by two because there are two omitted numbers below them.
# Basements (negatives) stay the same as the universal level.
# Examples: 1  =>  0, 0  =>  0, 5  =>  4, 15  =>  13, -3  =>  -3

def get_real_floor(n):
    return n-1 if 0 < n < 13 else n - 2 if n > 13 else n
	
# Task 75. Holiday VI - Shark Pontoon
https://www.codewars.com/kata/57e921d8b36340f1fd000059
# Your friend invites you out to a cool floating pontoon around 1km off the beach. 
# Among other things, the pontoon has a huge slide that drops you out right into the ocean, a small way from a set of stairs used to climb out.
# As you plunge out of the slide into the water, you see a shark hovering in the darkness under the pontoon... Crap!
# You need to work out if the shark will get to you before you can get to the pontoon. 
# To make it easier... as you do the mental calculations in the water you either freeze when you realise you are dead, or swim when you realise you can make it!
# You are given 5 variables;
# sharkDistance = distance from the shark to the pontoon. The shark will eat you if it reaches you before you escape to the pontoon.
# sharkSpeed = how fast it can move in metres/second.
# pontoonDistance = how far you need to swim to safety in metres.
# youSpeed = how fast you can swim in metres/second.
# dolphin = a boolean, if true, you can half the swimming speed of the shark as the dolphin will attack it.
# The pontoon, you, and the shark are all aligned in one dimension.
# If you make it, return "Alive!", if not, return "Shark Bait!".

def shark(pontoon_distance, shark_distance, your_speed, shark_speed, dolphin):
    if dolphin:
        shark_speed = shark_speed / 2
    your_time = pontoon_distance/your_speed
    shark_time = shark_distance/shark_speed
    return "Alive!" if your_time < shark_time else "Shark Bait!"  

# Task 76. Is he gonna survive?
https://www.codewars.com/kata/59ca8246d751df55cc00014c
# A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! 
# each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry. 
# Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?
# Return True if yes, False otherwise :)

def hero(bullets, dragons):
    return dragons * 2 <= bullets

# Task 77. Is n divisible by x and y?
https://www.codewars.com/kata/5545f109004975ea66000086
# Create a function that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero digits.
# Examples:
# 1) n =   3, x = 1, y = 3 =>  true because   3 is divisible by 1 and 3
# 2) n =  12, x = 2, y = 6 =>  true because  12 is divisible by 2 and 6
# 3) n = 100, x = 5, y = 3 => false because 100 is not divisible by 3
# 4) n =  12, x = 7, y = 5 => false because  12 is neither divisible by 7 nor 5

def is_divisible(n,x,y):
    return n % x == 0 and n % y == 0

# Task 78. ATM
https://www.codewars.com/kata/5635e7cb49adc7b54500001c
# There is enough money available on ATM in nominal value 10, 20, 50, 100, 200 and 500 dollars.
# You are given money in nominal value of n with 1<=n<=1500.
# Try to find minimal number of notes that must be used to repay in dollars, or output -1 if it is impossible.

def solve(n):
    count=0
    y = [500,200,100,50,20,10]
    i = 0
    if n % 10 != 0: return -1
    while n > 0:
        count=count + (n//y[i])
        n = int(n%y[i])
        i = i + 1
    return count

# Task 79. Sum of Digits / Digital Root
https://www.codewars.com/kata/541c8630095125aba6000c00
# Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. 
# The input will be a non-negative integer.
# Examples
#     16  -->  1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

def digital_root(n):
    while len(str(n))>1:
        s=0
        for i in str(n):
            s=s+ int(i)
        n=s
    return n

#Solution #2

def digital_root(n):
    return 1 + ((int(n) - 1) % 9) if n>0 else 0
	
# Task 80. Jenny's secret message
https://www.codewars.com/kata/55225023e1be1ec8bc000390
# Jenny has written a function that returns a greeting for a user. 
# However, she's in love with Johnny, and would like to greet him slightly different. 
# She added a special case to her function, but she made a mistake.
# Can you help her?

def greet(name):
    return "Hello, my love!" if name == "Johnny" else f"Hello, {name}!"
#