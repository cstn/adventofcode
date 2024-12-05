import re

# filename = 'sample.txt'
filename = 'input.txt'


with open(filename, 'r') as f:
    read_data = list(map(lambda x: re.split(': | \| ', x), f.read().splitlines()))
f.close()


def play_game(game_data, offset):
    score = 0
    for y, game in enumerate(game_data):
        score += 1
        [card_number, winning, scratched] = game
        winning_numbers = list(filter(lambda x: x.strip() != '', re.split('\s+', winning)))
        scratched_numbers = list(filter(lambda x: x.strip() != '', re.split('\s+', scratched)))
        intersection_numbers = list(set(winning_numbers) & set(scratched_numbers))
        win = len(intersection_numbers)
        win_cards = read_data[y + offset + 1: y + offset + win + 1]
        if len(win_cards) > 0:
            # print(card_number, ' wins ', list(map(lambda c: c[0], win_cards)))
            score += play_game(win_cards, y + offset + 1)

    return score


print('Result', play_game(read_data, 0))
