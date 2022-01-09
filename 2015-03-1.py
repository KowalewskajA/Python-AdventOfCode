import sys

if __name__ == '__main__':
    pos = {'x': 0, 'y': 0}
    lookup = {
        '^': ['y', -1],
        '>': ['x', +1],
        'v': ['y', +1],
        '<': ['x', -1]
    }
    d = dict()

    d[f"{pos['x']},{pos['y']}"] = 1

    for line in sys.stdin:
        for char in line:
            if char != '\n':
                pos[lookup[char][0]] += lookup[char][1]
                key = f"{pos['x']},{pos['y']}"
                if key in d:
                    d[key] += 1
                else:
                    d[key] = 1
                # print(f"{pos['x']},{pos['y']}")
    print(f"Houses: {len(d)}")
    print("Done")
    
