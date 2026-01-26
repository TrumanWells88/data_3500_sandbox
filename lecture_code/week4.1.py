# pseudo code

# given a list of numbers, count how many of the numbers are above the average of all the numbers in the list 

# maybe :[
nums = [1, 2, 3, 4, 5]
count = 0
for nums in nums:
     avg = avg + nums / 5
     if nums > avg:
        count = count + 1

"""
1. Establish a list of numbers
2. Calculate the average
3. Set up a counter to track the desired results
4. Loop
5. Compare the number to the average and increment a counter appropriately

"""

# 1 
nums = [1, 2, 3, 4, 5]
# 2
# avg = mean(nums)
# 3 
counter = 0


# leap year
year = 2028

if year % 4 == 0:
    if year % 100 == 0:
        print("It's not a leap year. :(")
    print("It's a leap year!")
else:
    print("It's not a leap year. :(")

# while loops/statements
while year % 4 == 0:
    print("It's a leap year!")
    year = year + 1


age = 2

while age < 9:
    print("aww you're so cute!")
    age = age + 1
else: 
    print("You're jot cute anymore, sorry.")

# guess the secret number
# if the user guesses too high, tell them and let them keep guessing
# if they're too low, tell them and let them keep guessing
# if they're corect, print out that they are correct and stoop running the code


# pseudocode
# 0. Variable to keep loop going
# 1. Set up a loop to have the user keep guessing
# 2. Create variables to track user guesses
# 3. compare guesses to actual #
# 4. print responses for each guess
# 5. in an else statement, if they guessed the number, print that they did
import random

secret_num = random.randit(1, 100)
num = int(input("Guess the secret number: "))
not_guessed = True

while not_guessed == True:
    guess = int(input("Enter your guess: "))

    if guess > secret_num:
        print("Too high, guess again.")
    elif guess < secret_num:
        print("Too low, guess again.")
    else:
        print("Congrats, you got it!")
        not_guessed = False





