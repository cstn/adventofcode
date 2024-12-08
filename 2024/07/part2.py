import re
from advent.files import read_input


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def concat(a, b):
    return int(str(a) + str(b))


def is_equal(result, numbers):
    if len(numbers) == 1:
        return result == numbers[0]
    if is_equal(result, [add(numbers[0],  numbers[1])] + numbers[2:]):
        return True
    if is_equal(result, [mul(numbers[0], numbers[1])] + numbers[2:]):
        return True
    if is_equal(result, [concat(numbers[0], numbers[1])] + numbers[2:]):
        return True

    return False


def main(filename):
    lines = read_input(filename)
    parsed_lines = [list(map(int, re.split(r':\s|\s+', l))) for l in lines]

    result = 0
    for l in parsed_lines:
        if is_equal(l[0], l[1:]):
            result += l[0]

    return result


print('Part 2')
print('Sample result', main('sample.txt'))
print('Main result', main('input.txt'))
