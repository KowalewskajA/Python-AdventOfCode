import sys


if __name__ == '__main__':
    print("\n>", end="")
    packages = []
    for line in sys.stdin:
        line = line.rstrip()
        if line in ["exit", "q"]:
            exit()
        else:
            packages.append(int(line))
    print(
        f"#:{len(packages)}|sum:{sum(packages)}|stack:{int(sum(packages)/3)}\
        \n{packages}"
    )
