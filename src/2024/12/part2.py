import numpy as np
from collections import defaultdict

import advent.parser as ap


def split_plants_into_regions(positions):
    if len(positions) == 1:
        return [positions]

    regions = []
    for p in positions:
        found = False
        for region in regions:
            near = [r for r in region if abs(r[0] - p[0]) == 1 or abs(r[1] - p[1]) == 1]
            if len(near) > 0:
                region.append(p)
                found = True
                break
        if not found:
            regions.append([p])

    return regions


def build_regions(garden):
    plant_dict = defaultdict()
    for plant_type in np.unique(garden):
        plant_dict[plant_type] = split_plants_into_regions(np.argwhere(garden == plant_type))

    return plant_dict


def calc_region_perimeter(region):
    if len(region) == 1:
        return 1 * 4

    min_y = np.min([r[0] for r in region])
    max_y = np.max([r[0] for r in region])
    min_x = np.min([r[1] for r in region])
    max_x = np.max([r[1] for r in region])

    perimeter = abs(max_y - min_y + 1) * 2 + abs(max_x - min_x + 1) * 2

    return perimeter


def calc_regions_costs(regions):
    return np.array([calc_region_perimeter(r) * len(r) for r in regions])


def main(filename):
    garden = ap.read_matrix_input(filename, None, dtype=str)
    regions = build_regions(garden)
    costs = np.array([calc_regions_costs(r) for r in regions.values()])

    return costs.sum()


print('Part 1')
print('Sample result', main('sample.txt'))
print('Main result', main('input.txt'))
