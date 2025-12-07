import math
import numpy as np
import advent.parser as ap
import advent.files as af

n = 3
def main(filename):
    read_lines = af.read_input(filename)
    parsed_lines = [[line[i:i + n] for i in range(0, len(line), n)] for line in read_lines]
    result = 0

    return result


print('Part 2')
print('Sample result', main('sample2.txt'))
# print('Main result', main('input2.txt'))
