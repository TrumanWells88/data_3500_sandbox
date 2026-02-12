"""
Programming Activity 1

Create a list called "colors" and assign it with your 3 favorite colors, as strings. Write a for loop to iterate through the list and print the values 
in the list.
- Create the list and assign the values.
- For loop through the values in the list.
"""
colors = ["red", "blue", "black"]

for color in colors:
    print("These are my favorite colors: ", colors)
    break

"""
Programming Activity 2 

Update the loop in activity 1 to not only iterate through the colors in the list, but also iterate through each character in each string.
- Nested for loop, to iterate through the characters in each color.
"""

for color in colors:
    print("These are my favorite colors: ", colors)
    for character in color:
        print(character)


"""
Programming Activity 3

Create a list that stores 10 random integers. Start with an empty list, then use the append(), and the random.randint() function to generate the list.
- Create an empty list.
- For loop 10 times and append a random number each time.
"""
import random
rand_nums = []

for i in range(10):
    rand_nums.append(random.randint(1, 10000))
print(sorted(rand_nums))


"""
Programming Activity 4

Using the list you generated in programming activity 3, extend your program to check if there are 2 even numbers in a row. If there are two even numbers in a row, print the numbers.
- There's a few ways to approach this, you could:
      1. use the index operator: lst[count] and lst[count+1]
      2. use slice operator: lst[count:count+2]
      3. use separate to store previous or next, and check if those are even
- No matter which way you chose you need to:
- Each iteration in the loop check if the current number and next number are both even.
"""

count = 0
for num in rand_nums:
    if count > 0:
        print("num: ", rand_nums[count])
        print("previous num: ", rand_nums[count - 1])
        if rand_nums[count] % 2 == 0 and rand_nums[count - 1] % 2 == 0:
            print(rand_nums[count])
            print(rand_nums[count - 1])
            print( "Two evens in a row!")
            print("It's even.")
        else:
            print("It's odd.")
    count += 1
    

"""
Programming Activity 5 (USE THE FILE IN CANVAS)

1. Download one year worth of stock data from yahoo finance. The instructions to do this are in the HW4 description.
2. After you have one year worth of stock data, use a for loop to iterate through the data, and calculate the average for the entire data set.
3. After you have calculated the average for the entire data set, see if you can calculate the average for the first 5 days only.  
(you will need this logic for your homework).
"""

stocks_file = open('programming_activities/AAPL.2023.txt')
file_lines = stocks_file.readlines()

sum = 0
for price in file_lines:
    sum += float(price)

avg = sum / len(file_lines)
print("Average = ", avg)

stocks_file.close()

"""
Programming Activity 5.2 
This activity is a continuation from the last one and is meant to help you with your homweork.
1. Write a Python program to read in the stock prices from a file, into a list.
2. Create a list of floats from the list of strings you read in, from step 2.
3. Calculate the average of the first 4 days in your list.
4. Calculate the average of the last 4 days in your list.
5. In a for loop, calculate a 4 day moving average for the floats in the list.
6. Add logic in the for loop to implement a simple moving average 
trading strategy.
7. Display the profit from the strategy, after the for loop has finished.
"""

stocks_file = open('programming_activities/AAPL.2023.txt', 'r')
prices = stocks_file.readlines()
stocks_file.close()

price_list = []

for price in prices:
    price_list.append(float(price))

first_four = 0
for i in range(4):
    first_four += price_list[i]

first_four_avg = first_four / 4
print("The average of the first 4 days was: ", first_four_avg)

last_four = 0
for i in range(len(price_list) - 4, len(price_list)):
    last_four += price_list[i]

last_four_avg = last_four / 4
print("The average of the last 4 days was: ", last_four_avg)

moving_avg = []
for i in range(len(price_list) - 3):
    total = 0
    for j in range(i ,i + 4):
        total += price_list[j]
    
    four_day_avg = total / 4
    moving_avg.append(four_day_avg)

position = 0
buy_price = 0
profit = 0

for i in range(len(moving_avg)):
    current_price = price_list[i + 3]
    current_avg = moving_avg[i]

    if position == 0 and current_price > current_avg:
        position = 1
        buy_price = current_price
    elif position == 1 and current_price < current_avg:
        position = 0
        profit += current_price - buy_price

print("Profit: ", profit)
