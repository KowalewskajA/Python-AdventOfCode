import sys
import hashlib

# A nice string is one with all of the following properties:
# (DONE)
# -It contains at least three vowels (aeiou only), 
#     like aei, xazegov, or aeiouaeiouaeiou.
# (DONE)
# -It contains at least one letter that appears twice in a row,
#     like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# (TODO)
# -It does not contain the strings ab, cd, pq, or xy, even if 
#     they are part of one of the other requirements.


def count_vowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel = 0
    for char in string:
        if char in vowels:
            vowel += 1
    return vowel


def count_double(string):
    current_letter = ' '
    doubles = 0
    for char in string:
        if char == current_letter:
            doubles += 1
        else:
            current_letter = char
    return doubles


def forbidden_pairs(string):
    pairs = ["ab", "cd", "pq", "xy"]
    for pair in pairs:
        if string.count(pair) != 0:
            return True
    return False


if __name__ == '__main__':
    nice_words = 0
    for line in sys.stdin:
        line = line.rstrip()
        if line in ["exit", "q"]:
            exit()
        else:
            if count_vowel(line) >= 3 and \
                    count_double(line) >= 1 and \
                    not forbidden_pairs(line):
                nice_words += 1
    print(f"nice words: {nice_words}")
