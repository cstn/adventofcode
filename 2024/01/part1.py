import advent.parser as ap
import advent.matrix as m

def distance(matrix):
    result = 0
    for i in range(len(matrix[0])):
        result += abs(matrix[0, i] - matrix[1, i])

    return result


def main(filename):
    parsed_lines = ap.read_parsed_input(filename, '\s+', dtype=int)
    transposed_lines = parsed_lines.transpose()
    m.sort(transposed_lines)

    return distance(transposed_lines)


print('Part 1')
print('Sample result', main('sample.txt'))
print('Main result', main('input.txt'))
