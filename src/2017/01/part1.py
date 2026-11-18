import advent.parser as ap


def checksum(numbers):
    result = 0

    for index in range(len(numbers)):
        index_to_compare = index + 1 if index < len(numbers) else 0
        if numbers[index] == numbers[index_to_compare]:
            result += numbers[index]

    return result


def main(filename):
    parsed_lines = ap.read_matrix_input(filename)
    puzzle_input = list(map(int, parsed_lines[0][0]))

    result = checksum(puzzle_input)

    return result


print('Part 1')
print('Sample result', main('sample.txt'))
print('Main result', main('input.txt'))
