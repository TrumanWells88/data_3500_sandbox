
# lists

numbers = [10, 15, 3, 7]
k = 17

def target_num(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                print("Found", target, "in number list")
                break  
target_num(numbers, k)




# basics

colors = ["purple", "green", "aggie blue", "orange", "yellow", "green"]
print("colors: ", colors)
colors.append("fighting white")
print("colors: ", colors)
colors.pop()
print("colors: ", colors)
colors.pop(1)
print("colors: ", colors)
colors.insert("pink")
print("colors: ", colors)


# search/slicing and sorting list


for i in range(len(colors)):
    print("colors[i]: ", colors[1])

for color in colors:
    print("color: ", color)


# normal slice
print(colors[3:5])
# just the last element
print(colors[-1:])
# reversed list
print(colors[::-1])
# every other element of the list
print(colors[::2])

colors.sort()
print("sorted colors: ", colors)


# MIDTERM QUESTION - figure out if 2 words are anagrams

def is_anagram(word1, word2):
    word_1_list = []
    word_2_list = []
    if len(word1) == len(word2):
        for letter in word1:
            word_1_list.append(letter)
        for letter in word2:
            word_2_list.append(letter)
        return sorted(word_1_list) == sorted(word_2_list)
    return False

if is_anagram("silent", "listen"):
    print("the two words are anagrams")
else:
    print("nope")
