
with open("/workspaces/data_3500_sandbox/lecture_code/TSLA.txt") as file:
    lines = file.readlines() 

prices = []
for line in lines:
    line = float(line)
    prices.append(line)

prices = prices[::-1]

daily_prices = [float(line) for line in open("/workspaces/data_3500_sandbox/lecture_code/TSLA.txt").readlines()]

print(daily_prices)

# THIS DOESNT WORK RIGHT