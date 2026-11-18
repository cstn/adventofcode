import numpy as np
from advent.parser import read_matrix_input


def main(filename):
    matrix = read_matrix_input(filename, None, str)

    result = 0

    for i in range(4):
        for y in range(1, len(matrix) - 1):
            for x in range(1, len(matrix[y]) - 1):
                shape = [matrix[y - 1, x - 1], matrix[y - 1, x + 1], matrix[y + 1, x - 1],  matrix[y + 1, x + 1]]
                if matrix[y, x] == 'A' and shape == ['M', 'S', 'M', 'S']:
                    result += 1

        matrix = np.rot90(matrix)

    return result


print('Part 2')
print('Sample result', main('sample.txt'))
print('Main result', main('input.txt'))
