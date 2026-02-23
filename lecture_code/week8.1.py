
prics = []
for line in lines:
    prices.append(float(line))

five_day_avg = (prices[0] + prices[1] + prices[2] + prices[3] + prices[4]) / prices[5]
print("five day average: ", five_day_avg)

i = 0

for price in prices:
    moving_avg = (prices[i] + prices[i+1] + prices[i+2] + prices[i+3] + prices[1+4])
    i += 1