import re


def read_input(name):
    with open(name, 'r') as f:
        lines = f.read().splitlines()
    f.close()

    return lines


def find_dest_in_line(needle, line):
    source = line[1]
    dest = line[0]
    length = line[2]
    if source <= needle <= source + length:
        offset = needle - source - length
        return dest + length + offset
    return None


def find_dest_in_map(source, map_lines):
    for map_line in map_lines:
        dest = find_dest_in_line(source, map_line)
        if dest is not None:
            return dest
    return source


def build_maps(lines):
    maps = []
    category_map = []
    for line in lines:
        if line.strip() == '':
            continue
        if line.find('map:') > 0:
            if len(category_map) > 0:
                maps.append(category_map)
            category_map = []
        else:
            category_map.append(list(map(lambda x: int(x), re.split('\s+', line))))
    maps.append(category_map)
    return maps


def main(filename):
    read_lines = read_input(filename)
    seed_ranges = list(map(lambda x: int(x), re.split('\s+', read_lines[0].replace('seeds: ', ''))))
    maps = build_maps(read_lines[2:])

    result = 100000
    for i in range(0, len(seed_ranges), 2):
        seeds = list(range(seed_ranges[i], seed_ranges[i] + seed_ranges[i + 1]))
        destinations = seeds
        j = 1
        for current_map in maps:
            print(str(j) + '/' + str(i + 1) + '/' + str(len(seed_ranges) / 2))
            j = j + 1
            destinations = [find_dest_in_map(destination, current_map) for destination in destinations]
            minimum = min(destinations)
            result = minimum if minimum < result else result

    return result


# filename = 'sample.txt'
filename = 'input.txt'
print('Result', main(filename))
