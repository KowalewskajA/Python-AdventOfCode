import sys
import itertools
import math


def calc_stack_weight(stacks):
    s = 0
    for stack in stacks:
        s += sum(stack)
    return s


if __name__ == '__main__':

    packages = []
    for line in sys.stdin:
        line = line.rstrip()
        if line in ['exit', 'q']:
            exit()
        else:
            packages.append(int(line))

    # print(
    #     f"#:{len(packages)}|sum:{weight}|stack:{aim_weight}\
    #     \n{packages}"
    # )

    weight = sum(packages)
    aim_weight = int(weight/4)
    candidates = []

    for i in range(len(packages)):
        if len(candidates) > 0:
            break
        for res in itertools.combinations(packages, i + 1):
            if sum(res) == aim_weight:
                candidates.append(res)

    min_qe = sys.maxsize
    candidate = []
    for res in candidates:
        cur_prod = math.prod(res)
        if cur_prod < min_qe:
            min_qe = cur_prod
            candidate = res
        # print(f"#{len(res)}: {res} | QE: {math.prod(res)}")

    # This worked but usually we had to check whether the remaining packages
    # could form two sets by finding atleast 1 set of the remaining packages
    packages_backup = packages
    for package in candidate:
        packages.remove(package)

    candidates2 = []
    for i in range(len(packages)):
        if len(candidates2) > 0:
            break
        for res in itertools.combinations(packages, i + 1):
            if sum(res) == aim_weight:
                candidates2.append(res)
    for res in candidates2:
        print(f"#{len(res)}: {res} | QE: {math.prod(res)}")

    print(f"#{len(candidate)}: {candidate} | QE: {math.prod(candidate)}")
