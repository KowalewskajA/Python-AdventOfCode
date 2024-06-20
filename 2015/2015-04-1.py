import sys
import hashlib

# input: ckczppom

if __name__ == '__main__':
    for line in sys.stdin:
        if line in ["exit\n", "q\n"]:
            exit()
        else:
            line = line.rstrip()
            # For understanding and testing the libs
            # string = 'abcdef609043'
            # result = hashlib.md5(str.encode(string))
            # print(f"Hash({string}): {result}")
            # string = "pqrstuv1048970"
            # result = hashlib.md5(str.encode(string))
            # print(f"Hash({string}): {result.hexdigest()}")
            number = 1
            hash = hashlib.md5(str.encode(line + str(number))).hexdigest()
            while hash[:5] != "00000":
                number += 1
                hash = hashlib.md5(str.encode(line + str(number))).hexdigest()
            print(f"Number: {number}")

