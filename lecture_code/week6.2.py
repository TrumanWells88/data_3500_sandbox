# random numbers

import random

random.randint()
random.randrange()

# files

file1 = open('/workspaces/data_3500_sandbox/lecture_code/spectrum_magic.txt')
print("file: ", file1)

file_lines = file1.readlines()
print("lines of the file: ", file_lines)

# open numbers.txt

file = open("/workspaces/data_3500_sandbox/lecture_code/numbers.txt")
number_lines = file.readlines()
sum = 0
for number in number_lines:
    # print("number: ", number)
    sum += int(number)

avg = sum / len(number_lines)
print("average: ", avg)

# create a new file
"""
3 ways to open a file
    1. read mode (r)
    2. write mode (w)
    3. append mode (a)
"""
wednesday_file = open("wednesday.txt", "a")

# for line in file_lines:
#     file.write(line)

wednesday_file.writelines(file_lines)

wednesday_file.write("/n" + str(avg))
wednesday_file.close()



