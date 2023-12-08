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


def end_position(positions):
    for p in positions:
        if p[-1] != 'Z':
            return False
    return True


def main(filename):
    read_lines = read_input(filename)
    parsed_lines = parse_input(read_lines)
    instructions = parsed_lines['instructions']
    nodes = parsed_lines['nodes']
    starts = list(map(lambda n: n[0], filter(lambda n: n[0].endswith('A'), nodes)))
    positions = starts
    steps = 0
    while not end_position(positions):
        for i, turn in enumerate(instructions):
            steps += 1
            for p, position in enumerate(positions):
                node = next(filter(lambda n: n[0] == position, nodes))
                if turn == 'L':
                    positions[p] = node[1]
                elif turn == 'R':
                    positions[p] = node[2]
    return steps


print('Result', main('sample2.txt'))
print('Result', main('input.txt'))
