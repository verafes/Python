# Real code challenges. Set #3-5
# Completed_solutions 3.41-3.50.

# Task 3.41. Sum of list values
https://www.codewars.com/kata/57a0515f53ba33ac5e000245
# Write function sumList (or sum_list) which will calculate the sum of the elements of the given list.
# For example: [1, 2, 3] -> 1 + 2 + 3 -> 6

def sum_list(lst):
    return sum(lst)

# Task 3.42. Pre-FizzBuzz Workout #1
https://www.codewars.com/kata/569e09850a8e371ab200000b
# Your inputs: a positive integer, n, greater than or equal to one. n is provided, you have NO CONTROL over its value.
# Your expected output is an array of positive integers from 1 to n (inclusive).
# Your job is to write an algorithm that gets you from the input to the output.

def pre_fizz(n):
    return list(range(1,n+1))
	
# Task 3.43. Series of integers from 0 to n
https://www.codewars.com/kata/5841f4fb673ea2a2ae000111
# Write a function generateIntegers/generate_integers that accepts a single argument n/$n 
# and generates an array containing the integers from 0 to n/$n inclusive.
# For example, generateIntegers(3)/generate_integers(3) should return [0, 1, 2, 3].
# n/$n can be any integer greater than or equal to 0.

def generateIntegers(n):
    return [el for el in range(n+1)]

# Solution #2:

def generateIntegers(n):
    return list(range(n + 1))

# Task 3.44. Lario and Muigi Pipe Problem
https://www.codewars.com/kata/56b29582461215098d00000f
# Issue Looks like some hoodlum plumber and his brother has been running around and damaging your stages again.
# The pipes connecting your level's stages together need to be fixed before you recieve any more complaints. 
# Each pipe should be connecting, since the levels ascend, you can assume every number in the sequence after the first index will be greater 
# than the previous and that there will be no duplicates.
# Task Given the a list of numbers, return the list so that the values increment by 1 for each index up to the maximum value.
# Example:
# Input: 1,3,5,6,7,8
# Output: 1,2,3,4,5,6,7,8

def pipe_fix(nums):
    arr = [nums[0]]
    c = dif = 0
    for i in range(0,len(nums)):
        dif = abs(nums[i] - nums[i-1])
        if dif > 1:
            while c < dif: 
                nums[i] = nums[i] + 1
                c +=1
                arr.append(nums[i])
    return arr

# Solution 2:

def pipe_fix(numbers):
    length = len(numbers) - 1
    y = []
    x = numbers[0]
    while x <= numbers[length]:
        y.append(x)
        x += 1
    return y

# Task 3.45. Fizz Buzz Cuckoo Clock
https://www.codewars.com/kata/58485a43d750d23bad0000e6
# Your story
# You've always loved both Fizz Buzz katas and cuckoo clocks, and when you walked by a garage sale and saw an ornate cuckoo clock with a missing pendulum, 
# and a "Beyond-Ultimate Raspberry Pi Starter Kit" filled with all sorts of sensors and motors and other components, 
# it's like you were suddenly hit by a beam of light and knew that it was your mission to combine the two to create a computerized Fizz Buzz cuckoo clock!
# You took them home and set up shop on the kitchen table, getting more and more excited as you got everything working together just perfectly. 
# Soon the only task remaining was to write a function to select from the sounds you had recorded depending on what time it was:
# Your plan
# When a minute is evenly divisible by three, the clock will say the word "Fizz".
# When a minute is evenly divisible by five, the clock will say the word "Buzz".
# When a minute is evenly divisible by both, the clock will say "Fizz Buzz", with two exceptions:
# On the hour, instead of "Fizz Buzz", the clock door will open, and the cuckoo bird will come out and "Cuckoo" between one and twelve times depending on the hour.
# On the half hour, instead of "Fizz Buzz", the clock door will open, and the cuckoo will come out and "Cuckoo" just once.
# With minutes that are not evenly divisible by either three or five, at first you had intended to have the clock just say the numbers ala Fizz Buzz, 
# but then you decided at least for version 1.0 to just have the clock make a quiet, subtle "tick" sound for a little more clock nature and a little less noise.
# Your input will be a string containing hour and minute values in 24-hour time, separated by a colon, and with leading zeros. For example, 1:34 pm would be "13:34".
# Your return value will be a string containing the combination of Fizz, Buzz, Cuckoo, and/or tick sounds that the clock needs to make at that time, 
# separated by spaces. Note that although the input is in 24-hour time, cuckoo clocks' cuckoos are in 12-hour time.

def fizz_buzz_cuckoo_clock(time):
    hour, minutes = time.split(':')
    hour, minutes = int(hour), int(minutes)
    res = []
    if hour >= 13: 
        hour -= 12
    if minutes == 0:
        return ("Cuckoo " * hour)[:-1] if hour > 0 else ("Cuckoo "  * 12)[:-1]
    if minutes == 30:
        return "Cuckoo"
    if minutes % 3 == 0:
        res.append("Fizz")
    if minutes % 5 == 0:
        res.append("Buzz")
    return "tick" if res == [] else " ".join(res)

# Task 3.46. Generating Markdowns 
https://www.codewars.com/kata/5f656199132bf60027275739
# Your friend has recently started using Codewars to learn more advanced coding. 
# They have just created their first kata, and they want to write a proper description for it, using codeblocks, images and hyperlinks.
# However, they are struggling to understand how to use Markdown formatting properly, 
# so they decide to ask for your help, by having you write a program that will generate some of the syntaxes for you.
# Markdown syntaxes
# links: [displayed text](url address)
# images: ![replacement message](url address)
# codeblocks: we'll use multiline codeblocks like the following
# ```language
# code
# ```
# Task: Your task is to create a function called generate_markdowns. It will take three parameters:
# markdown - The type of markdown to return. It can be "link", "img" or "code".
# text - The text,message or code to display
# url_or_language or urlOrLanguage - gives either the url address to use or the name of the language for the codeblock.

def generate_markdowns(markdown, text, url_or_language):
    if markdown == "link":
        return f'[{text}]({url_or_language})'
    if markdown == "img":
        return f'![{text}]({url_or_language})'
    if markdown == "code":
        return f'```{url_or_language}\n{text}\n```'

# Task 3.47. Sum of positive
https://www.codewars.com/kata/5715eaedb436cf5606000381
# You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.

def positive_sum(arr):
    s = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            s += arr[i]
    return 0 if len(arr) == 0 else s 
	
# Solution #2

def positive_sum(arr):
    return sum(i for i in arr if i > 0)


# Task 3.48. Sum without highest and lowest number
https://www.codewars.com/kata/576b93db1129fcf2200001e6
# Sum all the numbers of the array (in F# and Haskell you get a list) except the highest and the lowest element (the value, not the index!).
# (The highest/lowest element is respectively only one element at each edge, even if there are more than one with the same value!)
# Example:
# { 6, 2, 1, 8, 10 } => 16
# { 1, 1, 11, 2, 3 } => 6
# If array is empty, null or None, or if only 1 Element exists, return 0.

def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0


# Task 3.49. You only need one - Beginner
https://www.codewars.com/kata/57cc975ed542d3148f00015b
# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.
# Array can contain numbers or strings. X can be either.
# Return true if the array contains the value, false if not.

only need def check(seq, elem):
    return elem in seq


# Task 3.50. What is between?
https://www.codewars.com/kata/55ecd718f46fba02e5000029
# Complete the function that takes two integers (a, b, where a < b) 
# and return an array of all integers between the input parameters, including them.
# For example: a = 1, b = 4 --> [1, 2, 3, 4]

def between(a,b):
    return [i for i in range(a,b+1)]
