import numpy as np

import advent.parser as ap


def main(filename):
    parsed_lines = ap.read_matrix_input(filename, '', dtype=str)

    pos = np.argwhere(parsed_lines == 'S')

    result = 0

    return result


print('Part 2')
print('Sample result', main('sample2.txt'))
print('Main result', main('input2.txt'))
