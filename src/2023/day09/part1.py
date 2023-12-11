import re


def read_input(name):
    with open(name, 'r') as f:
        lines = f.read().splitlines()
    f.close()

    return lines


def parse_input(lines):
    return [list(map(lambda x: int(x), re.split('\s+', line))) for line in lines]


def create_history(line):
    history = [line]
    current_line = line
    while len([c for c in current_line if c != 0]) > 0:
        history_entry = []
        for i in range(len(current_line) - 1):
            history_entry.append(current_line[i + 1] - current_line[i])
        history.append(history_entry)
        current_line = history_entry
    return history


def extrapolate_history(history):
    history[len(history) - 1].append(0)
    for h in range(len(history) - 2, -1, -1):
        history[h].append(history[h][len(history[h]) - 1] + history[h + 1][len(history[h + 1]) - 1])
    return history


def history_value(history):
    return history[0][len(history[0]) - 1]


def main(filename):
    read_lines = read_input(filename)
    parsed_lines = parse_input(read_lines)
    result = 0
    for line in parsed_lines:
        history = create_history(line)
        extrapolated_history = extrapolate_history(history)
        result += history_value(extrapolated_history)
    return result


print('Result', main('sample.txt'))
print('Result', main('input.txt'))
