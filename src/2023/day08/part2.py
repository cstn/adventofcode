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
    nodes = dict({})
    for n in parsed_lines['nodes']:
        nodes[n[0]] = {'left': n[1], 'right': n[2]}
    starts = list(filter(lambda n: n.endswith('A'), nodes.keys()))
    positions = starts
    steps = 0
    while not end_position(positions):
        for i, turn in enumerate(instructions):
            steps += 1
            for p, position in enumerate(positions):
                node = nodes[position]
                if turn == 'L':
                    positions[p] = node['left']
                elif turn == 'R':
                    positions[p] = node['right']
    return steps


# print('Result', main('sample2.txt'))
print('Result', main('input.txt'))
