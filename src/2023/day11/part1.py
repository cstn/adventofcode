def read_input(name):
    with open(name, 'r') as f:
        lines = f.read().splitlines()
    f.close()

    return lines


def parse_input(lines):
    return [list(line) for line in lines]


def print_lines(label, lines):
    print(label)
    for line in lines:
        print(''.join(line))


def expand(lines, factor=2):
    result = []
    # rows
    for line in lines:
        if '#' in line:
            result.append(line)
        else:
            for i in range(factor):
                result.append(line)

    # columns
    final_result = []
    for y in range(len(result)):
        final_result.append([])
    for x in range(len(result[0])):
        column = [result[y][x] for y in range(len(result))]
        if '#' in column:
            for y in range(len(result)):
                final_result[y].append(result[y][x])
        else:
            for i in range(factor):
                for y in range(len(result)):
                    final_result[y].append(result[y][x])

    return final_result


def assign_numbers(lines):
    counter = 1
    for y, line in enumerate(lines):
        for x, col in enumerate(line):
            if col == '#':
                lines[y][x] = str(counter)
                counter += 1
    return lines, counter - 1


def positions(lines):
    result = []
    for y, line in enumerate(lines):
        for x, col in enumerate(line):
            if col == '#':
                result.append({'x': x, 'y': y})
    return result


def distance(pos1, pos2):
    return abs(pos1['x'] - pos2['x']) + abs(pos1['y'] - pos2['y'])


def main(filename):
    read_lines = read_input(filename)
    parsed_lines = parse_input(read_lines)
    expanded = expand(parsed_lines)
    pos = positions(expanded)
    print('Positions:', pos)

    result = 0
    for p, a in enumerate(pos):
        for q, b in enumerate(pos):
            if q > p:
                result += distance(a, b)

    return result


print('Sample result', main('sample.txt'))
print('Main result', main('input.txt'))
