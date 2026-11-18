import numpy
import numpy as np

from advent.parser import read_matrix_input


def convert2blocks(disk_map):
    result = []
    current_id = 0
    for i, d in enumerate(disk_map):
        if i % 2 == 0:
            a = np.full(shape=d, fill_value=current_id)
            result = np.append(result, a)
            current_id += 1
        else:
            a = np.full(shape=d, fill_value=-1)
            result = np.append(result, a)

    return result


def find_space(blocks, size, fromIndex, toIndex):
    for i in range(fromIndex, toIndex):
        sub = [b for b in blocks[i:i+size] if b == -1]
        if len(sub) == size:
            return i
    return -1


def sort_blocks(blocks):
    digits = numpy.unique([b for b in blocks if b != -1])
    for i in range(len(digits) - 1, 0, -1):
        current = digits[i]
        first_index = np.where(blocks == current)[0][0]
        last_index = np.where(blocks == current)[0][-1]
        size = last_index - first_index + 1
        position = find_space(blocks, size,0, first_index)
        if position != -1:
            for s in range(size):
                blocks[position + s] = current
                blocks[first_index + s] = -1

    return blocks


def checksum(blocks):
    return np.add.reduce([int(x) * i for i, x in enumerate(blocks) if x != -1])


def main(filename):
    [digits] = read_matrix_input(filename, None, int)
    disk_map = np.array(digits)
    blocks = convert2blocks(disk_map)
    sort_blocks(blocks)

    return checksum(blocks)


print('Part 2')
print('Sample result', main('sample.txt'))
print('Main result', main('input.txt'))
