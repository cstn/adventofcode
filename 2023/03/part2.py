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
        elif cell == '*':
            plan[y, x] = -1
        elif cell == '#':
            plan[y, x] = -2
        elif cell == '$':
            plan[y, x] = -3
        else:
            plan[y, x] = -4

print(plan)

# result
result = 0
for y, row in enumerate(plan):
    for x, cell in enumerate(row):
        if cell == -1:
            gears = 0
            ratio = 1
            if y > 0 and x > 0 and plan[y - 1, x - 1] > 0:
                ratio *= plan[y - 1, x - 1]
                gears += 1
                reset_numbers(plan[y - 1], x - 2, -1)
                reset_numbers(plan[y - 1], x, +1)
            if y > 0 and plan[y - 1, x] > 0:
                ratio *= plan[y - 1, x]
                gears += 1
                reset_numbers(plan[y - 1], x + 1, -1)
                reset_numbers(plan[y - 1], x - 1, +1)

            if y > 0 and x < len(row) - 1 and plan[y - 1, x + 1] > 0:
                ratio *= plan[y - 1, x + 1]
                gears += 1
                reset_numbers(plan[y - 1], x, -1)
                reset_numbers(plan[y - 1], x + 2, +1)

            if y < len(plan) - 1 and x > 0 and plan[y + 1, x - 1] > 0:
                ratio *= plan[y + 1, x - 1]
                gears += 1
                reset_numbers(plan[y + 1], x - 2, -1)
                reset_numbers(plan[y + 1], x, +1)
            if y < len(plan) - 1 and plan[y + 1, x] > 0:
                ratio *= plan[y + 1, x]
                gears += 1
                reset_numbers(plan[y + 1], x + 1, -1)
                reset_numbers(plan[y + 1], x - 1, +1)
            if y < len(plan) - 1 and x < len(row) - 1 and plan[y + 1, x + 1] > 0:
                ratio *= plan[y + 1, x + 1]
                gears += 1
                reset_numbers(plan[y + 1], x, -1)
                reset_numbers(plan[y + 1], x + 2, +1)

            if x > 0 and plan[y, x - 1] > 0:
                ratio *= plan[y, x - 1]
                gears += 1
                reset_numbers(plan[y], x - 2, -1)
                reset_numbers(plan[y], x, +1)
            if x < len(row) - 1 and plan[y, x + 1] > 0:
                ratio *= plan[y, x + 1]
                gears += 1
                reset_numbers(plan[y], x, -1)
                reset_numbers(plan[y], x + 2, +1)

            if gears == 2:
                result += ratio
                print('Found', y + 1, x + 1, gears, ratio)
            else:
                print('Found', y + 1, x + 1, gears, 'no ratio')


print(plan)
print(result)


