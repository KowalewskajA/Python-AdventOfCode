import sys


def turn(val, f_x, f_y, t_x, t_y, array):
    for x in range(f_x, t_x + 1):
        for y in range(f_y, t_y + 1):
            if val == 'toggle':
                array[x][y] = not array[x][y]
            else:
                array[x][y] = val


def count(array):
    count = 0
    for _list in array:
        for val in _list:
            if val:
                count += 1
    return count


if __name__ == '__main__':
    lights = [[False for j in range(1000)] for i in range(1000)]
    for line in sys.stdin:
        line = line.rstrip()
        if line in ["exit", "q"]:
            exit()
        else:
            array = line.split()
            if array[0] == 'toggle':
                f = array[1].split(',')
                t = array[3].split(',')
                turn(
                    'toggle', int(f[0]), int(f[1]), 
                    int(t[0]), int(t[1]), lights
                )
                # print(f"f_x={f[0]},f_y={f[1]}|t_x={t[0]},t_y={t[1]}")
            else:
                f = array[2].split(',')
                t = array[4].split(',')
                val = False
                if array[1] == 'on':
                    val = True
                turn(
                    val, int(f[0]), int(f[1]), 
                    int(t[0]), int(t[1]), lights
                )
    print(f"light: {count(lights)}")
