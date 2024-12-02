import numpy as np
import re


def read_input(name):
    with open(name, 'r') as f:
        lines = f.read().splitlines()
    f.close()

    return lines


def parse_input(lines, pattern = ', ', dtype=int):
    return np.array([re.split(pattern, line) for line in lines], dtype=dtype)


def read_parsed_input(filename, pattern = ', ', dtype=int):
    read_lines = read_input(filename)
    parsed_lines = parse_input(read_lines, pattern, dtype)

    return parsed_lines
