import numpy as np
import re


def read_input(name):
    with open(name, 'r') as f:
        lines = f.read().splitlines()
    f.close()

    return lines


def parse_input(lines):
    return np.array([re.split(', ', line) for line in lines])


def main(filename):
    read_lines = read_input(filename)
    parsed_lines = parse_input(read_lines)
    print('Parsed', parsed_lines)
    return 0


print('Sample result', main('sample.txt'))
print('Main result', main('inout.txt'))
