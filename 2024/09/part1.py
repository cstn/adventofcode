import numpy as np

from advent.parser import read_matrix_input


def convert2blocks(disk_map):
    result = []
    current_id = 0
    for i, d in enumerate(disk_map):
        if i % 2 == 0:
            a = np.full(shape=int(d), fill_value=str(current_id))
            result = np.append(result, a)
            current_id += 1
        else:
            a = np.full(shape=int(d), fill_value='.')
            result = np.append(result, a)

    return result


def sort_blocks(blocks):
    free_space = len([b for b in blocks if b == '.'])
    for i in range(len(blocks) - free_space):
        current = blocks[i]
        if current == '.':
            last_index = np.where(blocks != '.')[0][-1]
            blocks[i] = blocks[last_index]
            blocks[last_index] = '.'

    return blocks


def checksum(blocks):
    return np.add.reduce([int(x) * i for i, x in enumerate(blocks) if x != '.'])


def main(filename):
    [digits] = read_matrix_input(filename, None, str)
    disk_map = np.array(digits)
    blocks = convert2blocks(disk_map)
    sort_blocks(blocks)

    return checksum(blocks)


print('Part 1')
print('Sample result', main('sample.txt'))
print('Main result', main('input.txt'))
