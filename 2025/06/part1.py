import math
import numpy as np
import advent.parser as ap


def main(filename):
    parsed_lines = ap.read_matrix_input(filename, '\s+', dtype=str, strip=True)
    worksheet = np.rot90(parsed_lines, 3)

    result = 0
    for row in worksheet:
        values = [int(n) for n in row[1:]]
        if row[0] == "+":
            result += sum(values)
        elif row[0] == "*":
            result += math.prod(values)

    return result


print('Part 1')
print('Sample result', main('sample1.txt'))
print('Main result', main('input1.txt'))
