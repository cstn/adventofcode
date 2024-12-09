import numpy as np
import re
import advent.files as af


def parse_input(lines, pattern = ', ', dtype=int):
    tokens = [re.split(pattern, line) for line in lines] if pattern is not None else [list(line) for line in lines]
    return np.array(tokens, dtype=dtype)


def read_matrix_input(filename, pattern =', ', dtype=int):
    read_lines = af.read_input(filename)
    parsed_lines = parse_input(read_lines, pattern, dtype)

    return parsed_lines


def read_lists_input(filename, dtype=int):
    read_lines = af.read_input(filename)
    parsed_lines = [list(map(dtype, line.split())) for line in read_lines]

    return parsed_lines
