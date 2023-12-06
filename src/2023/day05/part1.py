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
    seeds = list(map(lambda x: int(x), re.split('\s+', read_lines[0].replace('seeds: ', ''))))
    maps = build_maps(read_lines[2:])

    print('Seeds', seeds)

    destinations = seeds
    for current_map in maps:
        print('Step', destinations)
        destinations = [find_dest_in_map(destination, current_map) for destination in destinations]

    print('Locations', destinations)

    return min(destinations)


# filename = 'sample.txt'
filename = 'input.txt'
print('Result', main(filename))
