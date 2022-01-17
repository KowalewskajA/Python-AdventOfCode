import sys


if __name__ == '__main__':
    print("Input pos=('row col'):\n>", end="")
    for line in sys.stdin:
        line = line.rstrip()
        if line in ['exit', 'q']:
            exit()
        else:
            # "200 50" for row 200 col 50
            pos = line.split()
            # calculate next top right ending
            # than subtract the entries ahead
            row = int(pos[0]) 
            col = int(pos[1])
            s = row + col - 1
            end = int(((s)*(s+1))/2 - (s-col))
            current = 20151125
            factor = 252533
            divisor = 33554393
            
            if end == 1:
                print(f"#1|val:{current}\n>", end="")
            else:
                for i in range(end - 1):
                    current = current * factor % divisor
                print(f"#:{end}|val:{current}\n>", end="")
