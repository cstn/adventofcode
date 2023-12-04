import numpy as np

# filename = 'sample.txt'
filename = 'input.txt'


def part_number(line, pos):
    result = line[pos]
    left_pos = pos - 1
    right_pos = pos + 1
    while right_pos < len(line) and line[right_pos].isnumeric():
        result = result + line[right_pos]
        right_pos += 1
    while left_pos > -1 and line[left_pos].isnumeric():
        result = line[left_pos] + result
        left_pos -= 1

    return ''.join(result)


def adjacent(plan, x, y):
    if x > 0 and plan[y, x - 1] == -1: # left
        return 'left'
    elif y > 0 and plan[y - 1, x] == -1: # top
        return 'top'
    elif x < len(row) - 1 and plan[y, x + 1] == -1: # right
        return 'right'
    elif y < len(plan) - 1 and plan[y + 1, x] == -1: # bottom
        return 'bottom'
    elif x > 0 and y > 0 and plan[y - 1, x - 1] == -1: # left top
        return 'left top'
    elif x < len(row) - 1 and y < len(plan) - 1 and plan[y + 1, x + 1] == -1: # right bottom
        return 'bottom right'
    elif x > 0 and y < len(plan) - 1 and plan[y + 1, x - 1] == -1: # left bottom
        return 'bottom left'
    elif x < len(row) - 1 and y > 0 and plan[y - 1, x + 1] == -1: # right top
        return 'top right'
    else:
        return ''


def reset_numbers(row, x, offset):
    if x < 0 or x > len(row) - 1:
        return
    if row[x] <= 0:
        return
    row[x] = 0
    reset_numbers(row, x + offset, offset)


with open(filename, 'r') as f:
    read_data = list(map(lambda x: list(x), f.read().splitlines()))
f.close()

engine = np.array(read_data)
plan = np.zeros(shape=engine.shape)

print(engine)

# make plan
for y, row in enumerate(engine):
    for x, cell in enumerate(row):
        if cell.isnumeric():
            plan[y, x] = part_number(row, x)
        elif cell == '.':
            plan[y, x] = 0
        else:
            plan[y, x] = -1

print(plan)

# result
result = 0
for y, row in enumerate(plan):
    for x, cell in enumerate(row):
        if cell == 0 or cell == -1:
            continue

        if adjacent(plan, x, y) != '':
            result += cell
            plan[y, x] = 0
            reset_numbers(row, x - 1, -1)
            reset_numbers(row, x + 1, +1)

print(plan)
print(result)


