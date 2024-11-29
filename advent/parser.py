import numpy as np
import re


def read_input(name):
    with open(name, 'r') as f:
        lines = f.read().splitlines()
    f.close()

    return lines


def parse_input(lines, pattern = ', '):
    return np.array([re.split(pattern, line) for line in lines])


def read_parsed_input(filename, pattern = ', '):
    read_lines = read_input(filename)
    parsed_lines = parse_input(read_lines, pattern)

    return parsed_lines
