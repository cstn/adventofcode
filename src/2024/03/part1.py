import numpy as np
import re
import advent.files as af


def main(filename):
    lines = af.read_input(filename)
    line = "\n".join(lines)

    instruction_pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    matches = instruction_pattern.findall(line)

    result = np.sum([int(match[0]) * int(match[1]) for match in matches])

    return result


print('Part 1')
print('Sample result', main('sample.txt'))
print('Main result', main('input.txt'))
