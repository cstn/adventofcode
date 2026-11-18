import advent.parser as ap
import numpy as np

def direction(line, threshold = 3):
    result = 0
    for i in range(1, len(line)):
        if abs(line[i - 1] - line[i]) > threshold:
            return 0
        if line[i] > line[i - 1]:
            if result < 0:
                return 0
            result = 1
        elif line[i] < line[i - 1]:
            if result > 0:
                return 0
            result = -1
        else:
            return 0

    return result


def is_safe(line):
    if direction(line) != 0:
        return True
    else:
        for i in range(len(line)):
            reduced_list = line.copy()
            reduced_list.pop(i)
            if direction(reduced_list) != 0:
                return True

    return False


def main(filename):
    parsed_lines = ap.read_lists_input(filename)

    return np.sum([1 if is_safe(line) else 0 for line in parsed_lines])


print('Part 2')
print('Sample result', main('sample.txt'))
print('Main result', main('input.txt'))
