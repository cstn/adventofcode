import advent.files as af
import re


def main(filename):
    lines = af.read_input(filename)
    parsed_lines = [re.split('-', line) for line in lines]
    fresh_ranges = [list(map(int, line)) for line in parsed_lines if len(line) == 2]
    ingredients = [list(map(int, line))[0] for line in parsed_lines if len(line) == 1 and line[0] != '']

    result = 0
    for i in ingredients:
        for r in fresh_ranges:
            if r[0] <= i <= r[1]:
                result += 1
                break

    return result


print('Part 1')
print('Sample result', main('sample1.txt'))
print('Main result', main('input1.txt'))
