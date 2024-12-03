import re
import advent.files as af


def main(filename):
    lines = af.read_input(filename)
    line = "\n".join(lines)

    instruction_pattern = re.compile(r'(mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\)))')
    matches = instruction_pattern.findall(line)

    result = 0
    enabled = True
    for match in matches:
        if match[0] == "do()":
            enabled = True
        elif match[0] == "don't()":
            enabled = False
        elif match[0].startswith('mul') and enabled:
            result += int(match[1]) * int(match[2])

    return result


print('Part 1')
print('Sample result', main('sample2.txt'))
print('Main result', main('input.txt'))
