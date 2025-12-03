import numpy as np
import advent.parser as ap


def main(filename):
    parsed_lines = ap.read_matrix_input(filename, '', dtype=int)

    result = 0
    for line in parsed_lines:
        maximum = max(line[:len(line) - 1])
        i = np.where(line == maximum)[0][0]
        second_maximum = max(line[i+1:])
        output = maximum * 10 + second_maximum
        result += output

    return result


print('Part 1')
print('Sample result', main('sample1.txt'))
print('Main result', main('input1.txt'))
