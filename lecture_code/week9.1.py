
"""
Write a function that implements division with two positive integers without using the division, multiplication, or modulous opperator. Return the quotient as an integer and ignore the remainder.
"""
import math

def num():
    return int(10 ** math.log10(3))

print(num())

# Second Way

def division(divisor, dividend):
    quotient = 0
    sum = 0
    while dividend >= divisor:
        sum += dividend
        quotient += 1
    
    return quotient

division(25,5)


# List Comprehension

"""
newList = [expression for item in iterable if condition]
"""

nums = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10]
evenNums = [num for num in nums if num % 2 == 0]
print(evenNums)


# New list of unique characters that aren't spaces

text = "teach a man to fish"

chars = [char for char in text if char != " "]
print(chars)

chars = []
for char in text:
    if char != " ":
        chars.append(char)



# palindromes

words = ["level", "dog", "racecar", "rain", "swag", "civic"]

pals = [word for word in words if word[::-1] == word]
print("palindromes:", pals)