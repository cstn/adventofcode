import advent.parser as ap

size = 100
start = 50


def main(filename):
    parsed_lines = ap.read_input(filename)

    position = start
    result = 0
    print('The dial starts by pointing at', position)
    for line in parsed_lines:
        direction = line[0]
        steps = int(line[1:]) if direction == 'R' else -int(line[1:])
        points = 0
        if steps > 0:
            for i in range(steps):
                position += 1
                if position == size:
                    position -= size
                if position == 0:
                    points += 1
        if steps < 0:
            for i in range(-steps):
                position -= 1
                if position == -1:
                    position += size
                if position == 0:
                    points += 1

        result += points

        print(line, ': The dial is rotated', steps, 'to point at', position, '; during this rotation, it points to 0:',
              points)

    return result


print('Part 2')
print('Sample result', main('sample2.txt'))
print('Main result', main('input2.txt'))
