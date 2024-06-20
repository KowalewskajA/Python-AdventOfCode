# import re
import sys
# from random import randint

if __name__ == '__main__':
    sum = 0
    pos = 1
    for line in sys.stdin:
        for char in line:
            if char == '(':
                sum = sum + 1
                pos = pos + 1
            elif char == ')':
                sum = sum - 1
                if sum < 0:
                    print(f"Pos: {pos}")
                    exit()
                else:
                    pos = pos + 1
            elif char != '\n':
                raise ValueError(
                    "Only '(', ')' '\\n'are valid, can not process '" 
                    + char + "'."
                )
        print(f"Sum: {sum}, no negative occured")
    
