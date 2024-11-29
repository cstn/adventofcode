import matrix.parser as mp
import matrix.print as mprint


def main(filename):
    parsed_lines = mp.read_parsed_input(filename)
    print('Parsed')
    mprint.print_matrix(parsed_lines)

    return 0


print('Part 1')
print('Sample result', main('sample.txt'))
print('Main result', main('input.txt'))
