import sys


class Package():
    def __init__(self, dimensions):
        # height < width < length
        self.height = dimensions[0]
        self.width = dimensions[1]
        self.length = dimensions[2]
        self.paper = 3 * self.height * self.width + \
            2 * self.height * self.length + \
            2 * self.width * self.length


def process_line(string):
    numbers = list(map(int, string.removesuffix('\n').split('x')))
    numbers.sort()
    return numbers


if __name__ == '__main__':
    sumPaper = 0
    for line in sys.stdin:
        sumPaper += Package(process_line(line)).paper
    print(f"paper: {sumPaper} squarefeet")
