import numpy as np
import re


def read_input(name):
    with open(name, 'r') as f:
        lines = f.read().splitlines()
    f.close()

    return lines


def parse_input(lines):
    return np.array([re.split(', ', line) for line in lines])


def turn(direction, action):
    if action == 'L' and direction == 'N':
        return 'W'
    if action == 'L' and direction == 'W':
        return 'S'
    if action == 'L' and direction == 'S':
        return 'E'
    if action == 'L' and direction == 'E':
        return 'N'
    if action == 'R' and direction == 'N':
        return 'E'
    if action == 'R' and direction == 'W':
        return 'N'
    if action == 'R' and direction == 'S':
        return 'W'
    if action == 'R' and direction == 'E':
        return 'S'
    return direction


def move(position, direction, steps):
    if direction == 'N':
        return {'x': position['x'], 'y': position['y'] + steps}
    if direction == 'W':
        return {'x': position['x'] - steps, 'y': position['y']}
    if direction == 'S':
        return {'x': position['x'], 'y': position['y'] - steps}
    if direction == 'E':
        return {'x': position['x'] + steps, 'y': position['y']}
    return position


def distance(position1, position2):
    return abs(position1['x'] - position2['x']) + abs(position1['y'] - position2['y'])


def main(filename):
    read_lines = read_input(filename)
    parsed_lines = parse_input(read_lines)
    print('Parsed', parsed_lines)

    direction = 'N'
    position = {'x': 0, 'y': 0}
    positions = [position]
    for action in parsed_lines[0]:
        direction = turn(direction, action[0])
        steps = int(action[1:])
        for i in range(steps):
            position = move(position, direction, 1)
            if position in positions:
                return distance({'x': 0, 'y': 0}, position)
            positions.append(position)

    return 0


print('Result (sample)', main('sample.txt'))
print('Result (input)', main('input.txt'))
