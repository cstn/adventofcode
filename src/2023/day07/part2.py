import numpy as np
import re


def read_input(name):
    with open(name, 'r') as f:
        lines = f.read().splitlines()
    f.close()

    return lines


def main(filename):
    read_lines = read_input(filename)
    return 0


filename = 'sample.txt'
# filename = 'input.txt'
print('Result', main(filename))
