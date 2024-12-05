import re


def read_input(name):
    with open(name, 'r') as f:
        lines = f.read().splitlines()
    f.close()

    return lines


def parse_input(lines):
    instructions = lines[0]
    nodes = [re.split(' = \(|, |\)', line)[:3] for line in lines[2:]]
    return {
        'instructions': instructions,
        'nodes': nodes
    }


def main(filename):
    read_lines = read_input(filename)
    parsed_lines = parse_input(read_lines)
    instructions = parsed_lines['instructions']
    nodes = parsed_lines['nodes']
    start = 'AAA'
    destination = 'ZZZ'
    position = start
    steps = 0
    while position != destination:
        for i, turn in enumerate(instructions):
            steps += 1
            node = next(filter(lambda n: n[0] == position, nodes))
            if turn == 'L':
                position = node[1]
            elif turn == 'R':
                position = node[2]
    return steps


print('Result', main('sample.txt'))
print('Result', main('input.txt'))
