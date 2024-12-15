import numpy as np

import advent.parser as ap

def visit_position(garden, y, x, value, region, visited):
    (size_y, size_x) = np.shape(garden)
    if (y < 0 or y >= size_y or x < 0 or x >= size_x or
            visited[y, x] == 1 or garden[y][x] != value):
        return
    visited[y, x] = 1
    region.append((y, x))
    visit_position(garden, y + 1, x, value, region, visited)
    visit_position(garden, y - 1, x, value, region, visited)
    visit_position(garden, y, x + 1, value, region, visited)
    visit_position(garden, y, x - 1, value, region, visited)


def build_regions(garden):
    (size_y, size_x) = np.shape(garden)
    visited = np.empty((size_y, size_x), dtype=int)
    regions = []

    for y in range(size_y):
        for x in range(size_x):
            if visited[y, x] != 1:
                region = []
                visit_position(garden, y, x, garden[y][x], region, visited)
                regions.append(region)

    return regions


def main(filename):
    garden = ap.read_matrix_input(filename, None, dtype=str)
    (size_y, size_x) = np.shape(garden)
    grouping = np.empty((size_y, size_x), dtype=int)
    fences = np.empty((size_y, size_x), dtype=int)

    # calculate fence per element
    for (y, x), element in np.ndenumerate(garden):
        fence = 4
        # element need fence on 4 sides except it has same element as neighbor
        if y > 0 and garden[y - 1, x] == element:
            fence -= 1
        if x > 0 and garden[y, x - 1] == element:
            fence -= 1
        if y < size_y - 1 and garden[y + 1, x] == element:
            fence -= 1
        if x < size_x - 1 and garden[y, x + 1] == element:
            fence -= 1

        fences[y, x] = fence

    # split into regions
    regions = build_regions(garden)

    # set size per plat type
    for region in regions:
        for position in region:
            grouping[position[0], position[1]] = len(region)

    return np.sum(fences * grouping)


print('Part 1')
print('Sample result', main('sample.txt'))
print('Sample 2 result', main('sample2.txt'))
print('Sample 3 result', main('sample3.txt'))
print('Main result', main('input.txt'))
