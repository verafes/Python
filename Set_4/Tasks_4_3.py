# Real code challenges. Set #4
# Completed_solutions 421-30

#  Task 421. Working with arrays I (and why your code fails in some katas)
https://www.codewars.com/kata/5a4ff3c5fd56cbaf9800003e
# In this kata the function returns an array/list of numbers without its last element. 
# The function is already written for you and the basic tests pass, but random tests fail. Your task is to figure out why and fix it.
# Hint: watch out for side effects.

# Given
def without_last(lst):
    # Fix it
    lst.pop() # removes the last element
    return lst
	
# Solution
def without_last(lst):
    return lst[:-1]

# Task 422. Unique string characters
https://www.codewars.com/kata/5a262cfb8f27f217f700000b
# In this Kata, you will be given two strings a and b and your task will be to return the characters that are not common in the two strings.
# For example: solve("xyab","xzca") = "ybzc" 
# --The first string has 'yb' which is not in the second string. 
# --The second string has 'zc' which is not in the first string. 
# Notice also that you return the characters from the first string concatenated with those from the second string.

def solve(a,b):
    return "".join([c for c in a if not c in b]+[c for c in b if not c in a])
	
# Task 423. Find the index of the first occurrence of an item in a list (with a twist)
https://www.codewars.com/kata/585ba66ce08bae791b00011b
# Write a function index_finder/index-finder that returns the index of the first occurrence of an item (x) in the list (lst), but ignoring the first item in the list. 
# The item will always occur at least once after the first item in the list. For example:
# lst = ['a','b','c'], x = 'b' >>> returns 1 ('b' occurs first at position 1)
# lst = ['b','b','b'], x = 'b' >>> returns 1 ('b' occurs first at position 1 if you ignore index 0)
# lst = ['b','c','b','a'], x = 'b' >>> returns 2 ('b' occurs first at position 2 if you ignore index 0)
# lst = [0,2,'a','5',0,1,0], x = 0 >>> returns 4 (0 occurs first at position 4 if you ignore index 0)

def index_finder(lst, x):
    return lst.index(x, 1)

#Solution 2

def index_finder(lst, x):
    for i in range(1,len(lst)):
        if lst[i]==x:
            return i
    return i

# Task 424. Tetris - rotate the block
https://www.codewars.com/kata/594ff4005ceb2be738000018
# Implement the 'A'-button of Nintendo's Tetris: A tetris block is represented by a boolean matrix where true means a part of the block and false means background. 
# For instance, this would be the "L"-shaped block:
# [[T, F],
#  [T, F],
#  [T, T]]
# And this would be the square block
# [[T, T],
#  [T, T]]
# Each push of the A button will call your transform function, which will rotate the block 90 degrees clockwise. 
# So for instance, the transform of the square block will return the same block, and the transform of the L block will return:
# [[T, T, T],
# [T, F, F]]

def transform(block):
    lst = [[block[j][i] for j in range(len(block))][::-1] for i in range(len(block[0])-1,-1,-1)]
    return lst[::-1]

#Solution 2:

def transform(block):
    l = len(block)
    w = len(block[0])
    block_new = []
    for i in range(w):
        s = []
        for j in range(l):
            s.append(block[j][i])
        block_new.append(s[::-1])
    return block_new
	
# Task 425. Split By Value
https://www.codewars.com/kata/5a433c7a8f27f23bb00000dc 
# For an integer k rearrange all the elements of the given array in such way, that:
# all elements that are less than k are placed before elements that are not less than k;
# all elements that are less than k remain in the same order with respect to each other;
# all elements that are not less than k remain in the same order with respect to each other.
# For k = 6 and elements = [6, 4, 10, 10, 6], the output should be splitByValue(k, elements) = [4, 6, 10, 10, 6].
# For k = 5 and elements = [1, 3, 5, 7, 6, 4, 2], the output should be splitByValue(k, elements) = [1, 3, 4, 2, 5, 7, 6].

def split_by_value(k, elements):
    arr = []
    for el in elements:
        if el < k:
            arr.append(el)
    for el in elements:
        if el >= k:
            arr.append(el)
    return arr

# Task 426. Total amount of points
https://www.codewars.com/kata/5bb904724c47249b10000131
# Our football team finished the championship. The result of each match look like "x:y". 
# Results of all matches are recorded in the collection.
# For example: ["3:1", "2:2", "0:1", ...]
# Write a function that takes such collection and counts the points of our team in the championship. Rules for counting points for each match:
# if x>y - 3 points
# if x<y - 0 point
# if x=y - 1 point
# Notes: there are 10 matches in the championship
# 0 <= x <= 4
# 0 <= y <= 4

def points(games):
    count = 0
    for el in games:
        x = el[0]
        y = el[2]
        if x > y: 
            count += 3
        if x == y:
            count += 1
    return count
	
# Shorter solution:

def points(games):
	return sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in games))
	
# Task 427. Vowel remover
https://www.codewars.com/kata/5547929140907378f9000039
# Create a function called shortcut to remove all the lowercase vowels in a given string.
# Examples
# shortcut("codewars") # --> cdwrs
# shortcut("goodbye")  # --> gdby
# Don't worry about uppercase vowels.

def shortcut( s ):
    return "".join([el for el in s if el not in "aoeiu"]) 

# Task 428. noobCode 03: CHECK THESE LETTERS... see if letters in "String 1" are present in "String 2"
https://www.codewars.com/kata/57470efebf81fea166001627
# Write a function that checks if all the letters in the second string are present in the first one at least once, regardless of how many times they appear:
# ["ab", "aaa"]    =>  true
# ["trances", "nectar"]    =>  true
# ["compadres", "DRAPES"]  =>  true
# ["parses", "parsecs"]    =>  false
# Function should not be case sensitive, as indicated in example #2. Note: both strings are presented as a single argument in the form of an array.

def letter_check(arr): 
    return len(set(arr[1].lower())-set(arr[0].lower())) == 0

# Task 429. Trumpness detector
https://www.codewars.com/kata/57829376a1b8d576640000d6
# We all love the future president (or Führer or duce or sōtō as he could find them more fitting) donald trump, but we might fear that some of his many fans like John Miller or John Barron are not making him justice, sounding too much like their (and our as well, of course!) hero and thus risking to compromise him.
# For this reason we need to create a function to detect the original and unique rythm of our beloved leader, typically having a lot of extra vowels, all ready to fight the estabilishment.
# The index is calculated based on how many vowels are repeated more than once in a row and dividing them by the total number of vowels a petty enemy of America would use.
# For example:
# trump_detector("I will build a huge wall")==0 #definitely not our trump: 0 on the trump score
# tump_detector("HUUUUUGEEEE WAAAAAALL")==4 #4 extra "U", 3 extra "E" and 5 extra "A" on 3 different vowel groups: 12/3 make for a trumpy trumping score of 4: not bad at all!
# trump_detector("listen migrants: IIII KIIIDD YOOOUUU NOOOOOOTTT")==1.56 #14 extra vowels on 9 base ones
# Notes: vowels are only the ones in the patriotic group of "aeiou": "y" should go back to Greece if she thinks she can have the same rights of true American vowels; there is always going to be at least a vowel, as silence is the option of coward Kenyan/terrorist presidents and their friends.
# Round each result by two decimal digits: there is no place for small fry in Trump's America.

def trump_detector(trump):
    trump = trump.lower()
    vowels = "aoieu"
    count_v = 0
    count_r = 0
    for i in range(1,len(trump)):
        if trump[i] in vowels and trump[i-1] != trump[i]:
            count_v += 1
        elif trump[i] in vowels and trump[i-1] == trump[i]:
            count_r +=1
    if trump[0] in vowels and trump[1]:
        count_v += 1
    return round((count_r)/count_v, 2) if count_v != 0 else 0

# Task 430. C.Wars
https://www.codewars.com/kata/55968ab32cf633c3f8000008
# Normally we have firstname, middle and the last name but there may be more than one word in a name like a South Indian one.
# Similar to those kinda names we need to initialize the names.
# See the pattern below:
# initials('code wars') => returns C.Wars 
# initials('Barack Hussain obama') => returns B.H.Obama 
# Complete the function initials.

def initials(name):
    name = name.title().split()
    n = []
    for el in name[:-1]:
        n.append(el[0])
    n.append(name[-1])
    return ".".join(n)

# Shorter solution:

def initials(name):
    name = name.title().split()
    return ".".join([el[0] if i != len(name)-1 else el for i,el in enumerate(name)])
#
