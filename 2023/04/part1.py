import re

# filename = 'sample.txt'
filename = 'input.txt'


with open(filename, 'r') as f:
    read_data = list(map(lambda x: re.split(': | \| ', x), f.read().splitlines()))
f.close()

result = 0
for y, game in enumerate(read_data):
    [card_number, winning, scratched] = game
    winning_numbers = list(filter(lambda x: x.strip() != '', re.split('\s+', winning)))
    scratched_numbers = list(filter(lambda x: x.strip() != '', re.split('\s+', scratched)))
    intersection_numbers = list(set(winning_numbers) & set(scratched_numbers))
    points = 1 * 2 ** (len(intersection_numbers) - 1) if len(intersection_numbers) > 0 else 0
    result += points

    print(card_number, winning_numbers, scratched_numbers, intersection_numbers, points, result)

print('Result', result)
