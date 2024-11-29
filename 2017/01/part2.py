import advent.parser as ap


def checksum(numbers):
    result = 0

    for index in range(len(numbers)):
        distance = len(numbers) // 2
        index_to_compare = index + distance if index + distance < len(numbers) else index + distance - len(numbers)
        if numbers[index] == numbers[index_to_compare]:
            result += numbers[index]

    return result


def main(filename):
    parsed_lines = ap.read_parsed_input(filename)
    puzzle_input = list(map(int, parsed_lines[0][0]))

    result = checksum(puzzle_input)

    return result


print('Part 2')
print('Sample result', main('sample.txt'))
print('Main result', main('input.txt'))
