# import re
import sys
# from random import randint
# to run from 2015 directory
# python3 01-1.py < input/01-1.txt

if __name__ == '__main__':
    sum = 0
    for line in sys.stdin:
        for char in line:
            if char == '(':
                sum = sum + 1
            elif char == ')':
                sum = sum - 1
            else:
                raise ValueError(
                    "Only '(' and ')' are valid, can not process '" 
                    + char + "'."
                )
        print(f'Input : {line}')
    print("Sum: " + str(sum))
