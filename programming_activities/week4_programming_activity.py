"""
Programming Activity 1

Write a program that asks the user the year they were born. Display a message telling the user what generation they belong to based on the following rules/years:
 - Gen Beta 2024
 - Gen Alpha 2010
 - Gen Z 1997
 - Millennial 1981
 - Gen X 1965
 - Baby Boomer 1946
"""
year_born = int(input("What year were you born?"))

if year_born < 1946:
    print("You are a dinosaur.")
elif year_born < 1965:
    print("You are a Baby Boomer")
elif year_born < 1981:
    print("You are Gen X")
elif year_born < 1997:
    print("You are a Millennial.")
elif year_born < 2010:
    print("You are Gen Z")
elif year_born < 2024:
    print("You are Gen Alpha.")
elif year_born < 2026:
    print("You're Gen Beta")
else: 
    print("You're still a fetus. Stop using my program.")


"""
Programming Activity 2:

Write a program which asks the user their age, then using a while loop displays the year they were born, using the following rules:
 - continue the loop while age is greater than 1
 - print each time "you were alive in year: " current_year
 - decrease age and current_year by one each time
 - add an else saying "you were born in year: " current_year
"""

age = int(input("What is your age?: "))
current_year = 2026 - 1

while age > 1:
    print(f"You were alive in {current_year}.")

    age -= 1
    current_year -= 1

else: 
    print(f"You were born in {current_year}")


"""
Programming Activity 3

Write a program that prints all the multiples of 5, from 5 to 95 using a for loop. 
"""

start, end = 5, 100
for i in range (5, 100, 5):
    print(i)

"""
Programming Activity 4

Write a program that prints all the multiples of 5, from 5 to 95 using a while loop.
"""
 
counter = 5

while counter <= 95:
    print(counter)
    counter += 5