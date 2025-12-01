import advent.parser as ap

size = 100
start = 50

def main(filename):
    parsed_lines = ap.read_input(filename)

    position = start
    result = 0
    for line in parsed_lines:
        direction = line[0]
        steps = int(line[1:]) if direction == 'R' else -int(line[1:])

        position += steps
        position = abs(position % size)

        if position == 0:
            result += 1

        print(line, ': The dial is rotated', direction, steps, 'to point at', position)

    return result

print('Part 1')
print('Sample result', main('sample1.txt'))
print('Main result', main('input1.txt'))
