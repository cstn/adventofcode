import numpy as np

from advent.parser import read_matrix_input


def main(filename):
    city = read_matrix_input(filename, None, dtype=str)
    locations = np.copy(city)
    max_x = len(city[0])
    max_y = len(city)

    frequencies = [str(f) for f in np.unique(city) if f != '.']
    for f in frequencies:
        positions = np.argwhere(city == f)
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                a, b = positions[i], positions[j]
                x = b[1] - a[1]
                y = b[0] - a[0]
                ax = a[1] - x
                ay = a[0] - y
                bx = b[1] + x
                by = b[0] + y

                if ax in range(max_x) and ay in range(max_y):
                    locations[ay, ax] = '#'
                if bx in range(max_x) and by in range(max_y):
                    locations[by, bx] = '#'

    return len(np.argwhere(locations == '#'))


print('Part 1')
print('Sample result', main('sample.txt'))
print('Main result', main('input.txt'))
