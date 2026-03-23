
"""
Using a function rand7() thay returns an integer from 1-7 (inclusive) with uniform probability, implement a function rand5() that returns an integer from 1 to 5 (inclusive)
"""

import random

def rand7():
    return random.randint(1,7)

def rand5():
    while True:
        num = rand7()
        if num <= 5:
            return num
        
print(rand5())
