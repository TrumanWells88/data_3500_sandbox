"""
Programming Activity 1

 1. make a variable called apple_price (set it to whatever you want)
 2. make a variable called number_purchased (set it to whatever you want)
 3. make a variable called tax and set it equal to 1.07
 4. make a variable, total_bill and calculate it by: total_bill = apple_price * number_purchased * tax
 5. print clearly and cleanly how many apples were purchased and the total_bill
 6. add a check before the final print statement to see if total_bill is equal to 0.  If so, print a message to the user to check their inputs.

 """

apple_price = 3
number_purchased = 12
tax = 1.07
total_bill = apple_price * number_purchased * tax

if total_bill == 0:
    print("Please check your inputs. Your bill should not be equal to $0")
else:
    print("Total # of apples purchased: ", number_purchased)
    print("Total cost: ", total_bill)




"""
Programming Activity 2

Write a program that asks the user how old they are, and what age they would like to live to. Calculate how long they have left to live (approximately), and then print a friendly message telling the user how long they have to 
live.
"""

age = int(input("How old are you?: "))
age_wanted = int(input("What age would you like to live to?: "))
life_left = age_wanted - age
print("You have", life_left, "years left to live!")





"""
Programming Activity 3

Write a program that gets a user's score in this class, as a percentage i.e. 90 or 95. Write an if statement that checks to see if their score is equal to or greater than 93.  If so, print "Congratulations you got an A" else print "Congratulations, you still learned a ton!!!!"
"""

score = float(input("What is your score in the class?: "))

if score >= 93:
    print("Congratulations, you got an A in the class!")
else:
    print("Congratulations, you still learned a ton!")