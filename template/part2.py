import advent.parser as ap
import advent.print as aprint


def main(filename):
    parsed_lines = ap.read_matrix_input(filename, '\s+', dtype=int)
    aprint.print_matrix(parsed_lines)

    result = 0

    return result


print('Part 2')
print('Sample result', main('sample2.txt'))
print('Main result', main('input2.txt'))
