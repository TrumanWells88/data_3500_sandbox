# functions
"""
Why use functions?
1. Modularity - smaller more manageable chunks
2. Readability - easier to read
3. Testing - easier to find bugs
4. Organization - organizes code better

"""
"""
Functions need 4 things
1. Defintion/Name
2. Arguments/Parameters
3. Main Body of Code
4. Return Statement

"""
degrees = int(input("What's the temperature in F?: "))

def f_to_c(degrees_f):
    degrees_c = (degrees_f - 32 * (5/9))
    print(degrees_c)

f_to_c(degrees)


def c_to_f(degrees_c):
    degrees_f = degrees_c * (9/5) + 32
    return(degrees_f)




# function arguments

age = int(input("How old is child: "))
weight = int(input("How much does child weigh: "))

def front_seat_check(age, weight = 50):

    if age >= 12:
        print("Child can sit in the front seat: ")
    elif age == 11 and weight >= 90:
        print("Child can sit in the front seat: ")
    elif age < 11 and weight > 100:
        print("Child can sit in the front seat")
    else: 
        print("Child can't sit in the front seat")

if front_seat_check == True:
    print("the child can sit in the front seat")
else:
    print("The child can't sit in the front seat")


# function defaults

print()