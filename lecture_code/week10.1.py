# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range (2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

# def gbp(num):
#     if num <= 2 or num % 2 != 0:
#         return "The input must be an even number or greater than 2."
    
#     for i in range(2, num):
#         if is_prime(i) and is_prime(num - i):
#             return (f"{i} + {num - i} = {num}")

# number = 8
# print(gbp(number))


# # string substrings

# emojis = "😼🥹🤡😱🤯😳🧅🍤🔇🚼"
# message = "I love python 😼😼🧅"
# new_emojis = [char for char in message if char in emojis]
# print(new_emojis)

# letters = ["z", "t", "c", "l"]

# if "l" in letters:
#     print("l is in letters")
# word_list = ["l", "e", "a", "d"]
# word2_list = ["d", "a", "l", "e"]

# for letter in word_list:
#     if letter in word2_list:
#         pass

# # string replacing

# sentence = "Our offices are in New York and California."

# sentence = sentence.replace("New York", "NY")
# sentence = sentence.replace("California", "CA")

# print(sentence)

# string 

file = open('/workspaces/data_3500_sandbox/lecture_code/tweets.txt', 'r')
lines = file.readlines()

total = 0
for line in lines:
    tweet = line.replace("@VirginAmerica", "")
    total += len(tweet)

print("The average tweet length is: ", total / len(lines))