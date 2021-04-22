# Real code challenges. Set #4-5
# Completed_solutions 4.41-4.50

#  Task 491. Fibonacci's FizzBuzz
https://www.codewars.com/kata/57bf599f102a39bb1e000ae5
# The goal of this kata is two-fold:
# 1.) You must produce a fibonacci sequence in the form of an array, containing a number of items equal to the input provided.
# 2.) You must replace all numbers in the sequence divisible by 3 with Fizz, those divisible by 5 with Buzz, and those divisible by both 3 and 5 with FizzBuzz.
# For the sake of this kata, you can assume all input will be a positive integer.# 
# Use Cases
# Return output must be in the form of an array, with the numbers as integers and the replaced numbers (fizzbuzz) as strings.

def fibs_fizz_buzz(n):
    prev = 0
    current = 1
    arr = [1]
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return arr
    else:
        for i in range(2,n+1):
            prev, current = current, current + prev
            arr.append(current)
    res = ['FizzBuzz' if (arr[x]%3 == 0 and arr[x]%5 == 0) else 'Fizz' if arr[x]%3 == 0 else 'Buzz' if arr[x]%5 == 0  else arr[x] for x in range(len(arr))]            
    return res

# Task 4.42. 21 Sticks
https://www.codewars.com/kata/5866a58b9cbc02c4f8000cac
# The game. In this game, there are 21 sticks lying in a pile. Players take turns taking 1, 2, or 3 sticks. The last person to take a stick wins. For example:
# 21 sticks in the pile
# Bob takes 2  -->  19 sticks left
# Jim takes 3  -->  16 sticks
# Bob takes 3  -->  13 sticks
# Jim takes 1  -->  12 sticks
# Bob takes 2  -->  10 sticks
# Jim takes 2  -->   8 sticks
# Bob takes 3  -->   5 sticks
# Jim takes 3  -->   2 sticks
# Bob takes 2  -->  Bob wins!
# Your task: Create a robot that will always win the game. Your robot will always go first. The function should take an integer and returns 1, 2, or 3.
# Note: The input will always be valid (a positive integer)

def make_move(sticks):
    return sticks % 4

# Task 4.43. Grasshopper - Bug Squashing
https://www.codewars.com/kata/56214b6864fe8813f1000019
# Terminal game bug squashing
# You are creating a text-based terminal version of your favorite board game. In the board game, each turn has six steps that must happen in this order: roll the dice, move, combat, get coins, buy more health, and print status.
# You are using a library that already has the functions below. Create a function named main that calls the functions in the proper order.
# - `combat`
# - `buy_health`
# - `get_coins`
# - `print_status`
# - `roll_dice`
# - `move`

Given:
health = 100
position = 0
coins = 0

def (main):
  getCoins()
  move()
  print_status()
  combat()
  rolDice()
  attack()
 
#Solution:

def main():
    roll_dice()
    move()
    combat()
    get_coins()
    buy_health()
    print_status()
	
# Task 4.44. Do you speak retsec?
https://www.codewars.com/kata/5516ab668915478845000780
# You and your friends want to play undercover agents. In order to exchange your secret messages, you've come up with the following system: 
# you take the word, cut it in half, and place the first half behind the latter. 
# If the word has an uneven number of characters, you leave the middle at its previous place:
# That way, you'll be able to exchange your messages in private.

# Task. # You're given a single word. Your task is to swap the halves. If the word has an uneven length, 
# leave the character in the middle at that position and swap the chunks around it.
# Examples
# reverse_by_center("secret")  == "retsec" # no center character
# reverse_by_center("agent")   == "nteag"  # center character is "e"

def reverse_by_center(s):
    i = len(s) // 2
    return s[i:] + s[:i] if len(s)%2 == 0 else s[i+1:] + s[i] + s[:i]
	
# Task 4.45. Bill & Bobs Secret Language
https://www.codewars.com/kata/58dd1c1710d1620c27000219
# Bill & Bob chat a lot but they don’t want people to understand what they’re talking about. 
# So they have created a secret language where they reverse each word in a sentence as well as reversing the sentence itself!
# They also add "#" at the start and the end of the sentence so they know it's the secret language.
# For example: -> Hello this is me = #em si siht olleH#,
# -> Bye! = #!eyB#
# Unfortunately Bob is a very lazy man and needs someone to convert sentences into their secret language.
# Please help Bob in constructing his secret conversations with Bill!

def reverser(string):
    return "#" + string [::-1 ] + "#"

# Task 4.46. Exclamation marks series #1: Remove a exclamation mark from the end of string
https://www.codewars.com/kata/57fae964d80daa229d000126
# Remove a exclamation mark from the end of string. For a beginner kata, you can assume that the input data is always a string, no need to verify it.
# Examples
# remove("Hi!") === "Hi"
# remove("Hi!!!") === "Hi!!"
# remove("!Hi") === "!Hi"
# remove("!Hi!") === "!Hi"
# remove("Hi! Hi!") === "Hi! Hi"
# remove("Hi") === "Hi"
# Note. Please don't post issue about difficulty or duplicate.

def remove(s):
    return s[:-1] if s and s[-1] == "!" else s 
	
# Task 4.47. Exclamation marks series #2: Remove all exclamation marks from the end of sentence
https://www.codewars.com/kata/57faece99610ced690000165
# Remove all exclamation marks from the end of sentence.
# Examples
# remove("Hi!") === "Hi"
# remove("Hi!!!") === "Hi"
# remove("!Hi") === "!Hi"
# remove("!Hi!") === "!Hi"
# remove("Hi! Hi!") === "Hi! Hi"
# remove("Hi") === "Hi"

def remove(s):
    return s.rstrip("!")
	
# Task 4.48. Exclamation marks series #3: Remove all exclamation marks from sentence except at the end
https://www.codewars.com/kata/57faefc42b531482d5000123
# Remove all exclamation marks from sentence except at the end.
# Examples
# remove("Hi!") == "Hi!"
# remove("Hi!!!") == "Hi!!!"
# remove("!Hi") == "Hi"
# remove("!Hi!") == "Hi!"
# remove("Hi! Hi!") == "Hi Hi!"
# remove("Hi") == "Hi"

def remove(s):
    count = len(s) - len(s.rstrip("!"))
    return s.replace("!", "") + "!"*count

# Task 4.49. Exclamation marks series #4: Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string
https://www.codewars.com/kata/57faf12b21c84b5ba30001b0
# Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string. For a beginner kata, you can assume that the input data is always a non empty string, no need to verify it.
# Examples
# remove("Hi!") === "Hi!"
# remove("Hi!!!") === "Hi!"
# remove("!Hi") === "Hi!"
# remove("!Hi!") === "Hi!"
# remove("Hi! Hi!") === "Hi Hi!"
# remove("Hi") === "Hi!"

def remove(s):
    return s.replace("!", "") + "!"

# Task 4.50. Backspaces in string
https://www.codewars.com/kata/5727bb0fe81185ae62000ae3
# Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"

Your task is to process a string with "#" symbols.

Examples
"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""

def clean_string(s):
    final = []
    for i in s:
        if i != "#":
            final.append(i)
        elif len(final) > 0: 
            final.pop()
    return "".join(final)

# Solution 2:
def clean_string(s):
    s2 = ""
    for el in s:
        if el != "#":
            s2 += el
        else:
            s2 = s2[:-1]
    return s2

#
