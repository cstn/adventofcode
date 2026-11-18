from collections import Counter

import advent.parser as ap


MULTIPLIER = 2024
BLINKS = 75


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


def blink(counter):
    result = Counter()

    for item, count in counter.items():
        for c in change(item):
            result[c] += count

    return result


def main(filename):
    parsed_line = ap.read_lists_input(filename, dtype=int)
    counter = Counter(parsed_line[0])

    for i in range(BLINKS):
        counter = blink(counter)

    return sum(counter.values())


print('Part 1')
print('Sample result', main('sample.txt'))
print('Main result', main('input.txt'))
