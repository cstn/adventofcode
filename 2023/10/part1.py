import numpy as np


def read_input(name):
    with open(name, 'r') as f:
        lines = f.read().splitlines()
    f.close()

    return lines


def parse_input(lines):
    return np.array([list(line) for line in lines])


def tile(tile_map, x, y):
    return tile_map[y, x]


def find_start(tile_map, c='S'):
    for y, line in enumerate(tile_map):
        for x, col in enumerate(tile_map):
            if tile(tile_map, x, y) == c:
                return x, y
    return -1, -1


def move(tile_map, x, y):
    if tile(tile_map, x, y) == 'S' and y > 0 and tile(tile_map, x, y - 1) in ['|', '7', 'F']:
        # start noth
        return x, y - 1
    if tile(tile_map, x, y) == 'S' and y < len(tile_map) - 1 and tile(tile_map, x, y + 1) in ['|', 'L', 'J']:
        # start south
        return x, y + 1
    if tile(tile_map, x, y) == 'S' and x > 0 and tile(tile_map, x - 1, y) in ['-', 'F', 'L']:
        # start west
        return x - 1, y
    if tile(tile_map, x, y) == 'S' and x < len(tile_map[0]) - 1 and tile(tile_map, x + 1, y) in ['-', 'J', '7']:
        # start east
        return x + 1, y

    if tile(tile_map, x, y) in ['|', 'L', 'J'] and y > 0 and tile(tile_map, x, y - 1) != '.':
        # north
        return x, y - 1
    if tile(tile_map, x, y) in ['|', '7', 'F'] and y < len(tile_map) - 1 and tile(tile_map, x, y + 1) != '.':
        # south
        return x, y + 1
    if tile(tile_map, x, y) in ['-', 'J', '7'] and x > 0 and tile(tile_map, x - 1, y) != '.':
        # west
        return x - 1, y
    if tile(tile_map, x, y) in ['-', 'L', 'F'] and x < len(tile_map[0]) - 1 and tile(tile_map, x + 1, y) != '.':
        # east
        return x + 1, y
    return None, None


def main(filename):
    read_lines = read_input(filename)
    tile_map = parse_input(read_lines)
    x, y = find_start(tile_map)
    print('Start', x + 1, y + 1)
    steps = 0
    while x is not None and y is not None:
        steps += 1
        new_x, new_y = move(tile_map, x, y)
        if new_x is not None and y is not None:
            print('Step', new_x + 1, new_y + 1)
        tile_map[y, x] = '.'
        x = new_x
        y = new_y

    return steps / 2


# print('Sample result', main('sample.txt'))
print('Main result', main('input.txt'))
