import advent.files as af
import re


def main(filename):
    lines = af.read_input(filename)
    parsed_lines = [re.split('-', line) for line in lines]
    ranges = [tuple(map(int, line)) for line in parsed_lines if len(line) == 2]

    ranges = sorted(ranges)
    result = [ranges[0]]

    for r in ranges[1:]:
        last = result[-1]

        if last[1] >= r[0]:
            result[-1] = (last[0], max(last[1], r[1]))
        else:
            result.append(r)

    return sum(r[1] - r[0] + 1 for r in result)


print('Part 2')
print('Sample result', main('sample2.txt'))
print('Main result', main('input2.txt'))
