import advent.parser as ap
import advent.print as aprint


def main(filename):
    parsed_lines = ap.read_matrix_input(filename, '\s+', dtype=int)
    print('Parsed')
    aprint.print_matrix(parsed_lines)

    return 0


print('Part 1')
print('Sample result', main('sample.txt'))
print('Main result', main('input.txt'))
