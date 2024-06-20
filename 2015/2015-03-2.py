import sys

if __name__ == '__main__':
    pos = {
        0: {'x': 0, 'y': 0},
        1: {'x': 0, 'y': 0}
    }
    lookup = {
        '^': ['y', -1],
        '>': ['x', +1],
        'v': ['y', +1],
        '<': ['x', -1]
    }
    d = dict()

    d[f"{pos[0]['x']},{pos[0]['y']}"] = 2
    instruction = 0

    for line in sys.stdin:
        for char in line:
            if char != '\n':
                relevant_pos = pos[instruction % 2]
                relevant_pos[lookup[char][0]] += lookup[char][1]
                key = f"{relevant_pos['x']},{relevant_pos['y']}"
                instruction += 1
                if key in d:
                    d[key] += 1
                else:
                    d[key] = 1
                # print(f"{pos['x']},{pos['y']}")
    print(f"Houses: {len(d)}")
    print("Done")
