import numpy as np

import advent.parser as ap


def score(topographic, position, tops):
    (size_y, size_x) = topographic.shape
    x, y = position[1], position[0]
    current_level = topographic[y, x]

    if current_level == 9:
        if not [y, x] in tops:
            tops.append([y, x])
            return 1
        else:
            return 0

    result = 0
    result += score(topographic, [y + 1, x], tops) if y + 1 < size_y and topographic[y + 1, x] == current_level + 1 else 0
    result += score(topographic, [y, x + 1], tops) if x + 1 < size_x and topographic[y, x + 1] == current_level + 1 else 0
    result += score(topographic, [y, x - 1], tops) if x > 0 and topographic[y, x - 1] == current_level + 1 else 0
    result += score(topographic, [y - 1, x], tops) if y > 0 and topographic[y - 1, x] == current_level + 1 else 0

    return result


def main(filename):
    topographic_map = ap.read_matrix_input(filename , pattern=None, dtype=int)

    trailheads = np.argwhere(topographic_map == 0)
    score_sum = np.array([score(topographic_map, t, []) for t in trailheads]).sum()

    return score_sum


print('Part 1')
print('Sample result', main('sample.txt'))
print('Main result', main('input.txt'))
