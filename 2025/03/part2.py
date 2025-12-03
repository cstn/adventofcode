import advent.parser as ap

LENGTH = 12

def find_maximum(line, start, end):
    index = -1
    maximum = 0
    for i in range(end - 1, start - 1, -1):
        if line[i] >= maximum:
            maximum = line[i]
            index = i

    return maximum, index


def main(filename):
    parsed_lines = ap.read_matrix_input(filename, '', dtype=int)

    result = 0
    for line in parsed_lines:
        index = 0
        buffer = ''

        for i in range(LENGTH):
            maximum, index = find_maximum(line, index, len(line) - LENGTH + i + 1)
            index += 1
            buffer += str(maximum)

        result += int(buffer)

    return result


print('Part 2')
print('Sample result', main('sample2.txt'))
print('Main result', main('input2.txt'))
