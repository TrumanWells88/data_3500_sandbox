"""
Programming Activity 1

Write a Python program that creates a list of all even numbers from 2 to 100 using list comprehension.
"""

nums = [x for x in range(0, 101)]

evenNums = [num for num in nums if num % 2 == 0]
print(evenNums)

"""
Programming Activity 2

Write a Python program that takes a list of strings as input, where some strings might have leading or trailing spaces. Use list comprehension to remove these spaces from each string in the list.
"""
countStrings = 0
stringList = []

while countStrings < 5:
    strings = input("Please input a word: ")
    countStrings += 1
    stringList.append(strings)

print(stringList)


"""
Programming Activity 3

Write a Python program which asks the user their name.  
Store their name in a string variable. Use the Upper() function to make 
all of the letters in their name upper case. Then, print to the console: 
welcome, NAME ALLCAPS!.
 - using input get the user name
 - change the string to be all upper case
 - print to the console: "welcome, NAME ALLCAPS!" (adding an exclamation
"""
while True:
    nameAsk = str(input("What's your name?: ")).strip()
    if nameAsk.isaplha():
      break
    else:
      print("Please enter a valid name (letters only: )")
        
print(f"Welcome, {nameAsk.upper()}!")

"""
Programming Activity 4

Create a variable that stores the sentence below, and print the sentence to 
the console, before making any changes. Change the first letter in the 
sentence to be capitalized. Change the first instance of Whoa to be whoa 
(all lower case), and the second instance of Whoa to be WHOA(all upper case).  
Append a exclamation point to the end of the sentence. 
Then re-print the sentence to the console.

sentence = "dude, I just biked down that mountain and at first I was like 
Whoa, and then I was like Whoa"
 - using the string variable sentence, change the first letter to upper 
   case using capitalize()
 - create a list called "words" that stores all the words in the sentence 
   in a list using the split() function.
 - change the first "Whoa" to "whoa", and the second "Whoa" to "WHOA".
 - append an exclamation point.
 - print the new sentence.
"""

sentence = "dude, I just biked down that mountain and at first I was like Whoa, and then I was like Whoa"
print(sentence)

sentence.capitalize()
words = sentence.split()

count = 0
for i in words:
    if "Whoa" in words[count]:
      if count == 1:
        words[count] = words[count].replace("Whoa", "whoa")
      elif count == 2:
        words[count] = words[count].replace("Whoa", "WHOA")
    count += 1
newSentence = sentence + "!"
print(newSentence)



