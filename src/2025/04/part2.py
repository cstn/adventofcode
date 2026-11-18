import numpy as np

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
    matrix = ap.read_matrix_input(filename, None, dtype=str)
    aprint.print_matrix(matrix)

    result = 0
    found = True
    matrix_copy = np.copy(matrix)
    while found:
        matrix = matrix_copy
        found = False
        matrix_copy = np.copy(matrix)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i, j] == ROLL and count_neighbors(matrix, i, j) < THRESHOLD:
                    result += 1
                    matrix_copy[i, j] = 'x'
                    found = True

    return result


print('Part 2')
print('Sample result', main('sample2.txt'))
print('Main result', main('input2.txt'))
