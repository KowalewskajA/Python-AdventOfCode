import sys
import re

# Now, a nice string is one with all of the following properties:
# (DONE)
# -It contains a pair of any two letters that appears at least twice in the
#   string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not 
#   like aaa (aa, but it overlaps).
# (DONE)
# -It contains at least one letter which repeats with exactly one letter 
#   between them, like xyx, abcdefeghi (efe), or even aaa.


def symmetric_triplet(string):
    result = re.findall(r'([a-z])([a-z])(\1)', string)
    return len(result)


def double_pair(string):
    for x in range(len(string) - 3):
        if string[x:x+2] in string[x+2:]:
            return True
    return False


if __name__ == '__main__':
    nice_words = 0
    for line in sys.stdin:
        line = line.rstrip()
        if line in ["exit", "q"]:
            exit()
        else:
            if symmetric_triplet(line) > 0 and double_pair(line):
                nice_words += 1   
    print(f"nice words: {nice_words}")
