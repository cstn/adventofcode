import numpy as np

import advent.parser as ap


MULTIPLIER = 2024
BLINKS = 25


def change(item):
    # rule 1
    if item == 0:
        return [1]

    # rule 2
    digits = str(item)
    digits_count = len(digits)
    if digits_count % 2 == 0:
        left = digits[:digits_count // 2]
        right = digits[digits_count // 2:]
        return [int(left), int(right)]

    # rule 3
    return [item * MULTIPLIER]


def blink(row):
    result = np.array([], dtype=int)
    for item in row:
        result = np.concat((result, change(item)), axis=None)
    return result



def main(filename):
    parsed_line = ap.read_lists_input(filename, dtype=int)

    stones = np.array(parsed_line[0], dtype=int)
    for i in range(BLINKS):
        stones = blink(stones)

    return len(stones)


print('Part 1')
print('Sample result', main('sample.txt'))
print('Main result', main('input.txt'))
