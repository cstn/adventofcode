import numpy as np
from advent.parser import read_matrix_input

XMAS = 'XMAS'

def diagonal(matrix):
    copy = np.copy(matrix)
    a = copy.shape[0]
    return [np.diag(copy, k=i).tolist() for i in range(-a+1,a)]


def main(filename):
    matrix = read_matrix_input(filename, None, str)

    result = 0

    for i in range(4):
        for r in matrix:
            result += ''.join(r).count(XMAS)

        diagonals = diagonal(matrix)
        for d in diagonals:
            result += ''.join(d).count(XMAS)

        matrix = np.rot90(matrix)

    return result


print('Part 1')
print('Sample result', main('sample.txt'))
print('Main result', main('input.txt'))
