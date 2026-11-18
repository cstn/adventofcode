import advent.parser as ap
import advent.print as aprint

THRESHOLD = 4
ROLL = '@'

def count_neighbors(matrix, x, y):
    result = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (i != x or j != y) and i >= 0 and j >= 0 and i < len(matrix) and j < len(matrix[0]):
                if matrix[i, j] == ROLL:
                    result += 1
    return result


def main(filename):
    parsed_lines = ap.read_matrix_input(filename, None, dtype=str)
    aprint.print_matrix(parsed_lines)

    result = 0
    for i in range(len(parsed_lines)):
        for j in range(len(parsed_lines[0])):
            if parsed_lines[i, j] == ROLL and count_neighbors(parsed_lines, i, j) < THRESHOLD:
                result += 1

    return result


print('Part 1')
print('Sample result', main('sample1.txt'))
print('Main result', main('input1.txt'))
