import numpy as np

import advent.parser as ap
import advent.print as aprint


def move(position, matrix):
    y, x = position

    if y >= len(matrix) - 1:
        return 0

    if matrix[y + 1, x] == '.':
        matrix[y + 1, x] = '|'

        return move((y + 1, x), matrix)
    elif matrix[y + 1, x] == '^':
        matrix[y + 1, x - 1] = '|'
        matrix[y + 1, x + 1] = '|'
        return 1 + move((y + 1, x - 1), matrix) + move((y + 1, x + 1), matrix)
    else:
        return 0


def main(filename):
    parsed_lines = ap.read_matrix_input(filename, '', dtype=str)

    pos = np.argwhere(parsed_lines == 'S')

    result = move(pos[0], parsed_lines)
    aprint.print_matrix(parsed_lines)

    return result


print('Part 1')
print('Sample result', main('sample1.txt'))
print('Main result', main('input1.txt'))
