import numpy as np
import re
import advent.files as af


def parse_input(lines, pattern = ', ', dtype=int):
    return np.array([re.split(pattern, line) for line in lines], dtype=dtype)


def read_matrix_input(filename, pattern =', ', dtype=int):
    read_lines = af.read_input(filename)
    parsed_lines = parse_input(read_lines, pattern, dtype)

    return parsed_lines


def read_lists_input(filename):
    read_lines = af.read_input(filename)
    parsed_lines = [list(map(int, line.split())) for line in read_lines]

    return parsed_lines
