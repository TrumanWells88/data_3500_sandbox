# There should be more up here but idk I missed it.

prices = [1,2,3,4,5,6,7,8,9]
for line in lines:
    prices.append(float(line))

three_day_avg = (prices[0] + prices[1] + prices[2]) / prices[3]
print("three day average: ", three_day_avg)

i = 0

for price in prices:
    moving_avg = (prices[i] + prices[i+1] + prices[i+2])
    i += 1


# Midterm Review Coding Questions

number = 0

if number % 2 == 0:
    print(number)
    number += 2
elif number == 18:
    continue


for i in range (1,21):
    number += 2
    if number == 18:
        continue
    
    if i != 18:
        print(i, end = " ")

for i in range (1,6):
    print(i, i*10, end = ", ")


