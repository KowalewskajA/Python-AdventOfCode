import sys
import re
from itertools import permutations

# python3 09-1.py < input/09-1.txt

line_re = re.compile(r"(\w+) to (\w+) = (\d+)")

def parse_line(line:str) -> tuple[str, str, int]:
    split = line_re.match(line)
    if split:
        start, end, distance = split.groups()
        return start, end, int(distance)
    return "", "", 0

def populate_distances(nodes:set, edges:list, distances:dict) -> None:
    for node in nodes:
        distances[node] = dict()
    for edge in edges:
        start, end, distance = edge
        distances[start][end] = distance
        distances[end][start] = distance

if __name__ == '__main__':
    nodes = set()
    edges = []
    distances = dict()
    for line in sys.stdin:
        line = line.rstrip()
        if line in ["exit", "q"]:
            exit()
        else:
            start, end, distance = parse_line(line)
            # print(f"From {start} to {end} in {distance}")
            # Populate our Datastructures
            if start is not None:
                nodes.add(start)
                nodes.add(end)
                edges.append((start, end, distance))
    populate_distances(nodes, edges, distances)
    # print(f"{distances}")
    # Build all Path
    results = []
    for i, path in enumerate(permutations(nodes)):
        # print(f"{i} : {path}")
        distance = 0
        for start, end in zip(path[0:], path[1:]):
            # print(f"from: {start} to: {end}")
            distance += distances[start][end]
        results.append((distance, path))
    results.sort()
    print(f"Shortest: {results[0][0]}")
    print(f"Longest: {results[-1][0]}")
# print(candidates)
