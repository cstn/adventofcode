import re

# filename = 'sample.txt'
filename = 'input.txt'

allowed = dict({
    'red': 12,
    'green': 13,
    'blue': 14
})


def parse_line(text):
    [game_text, hands_text] = re.split(': ', text)

    return dict({
        'game': int(game_text.replace('Game ', '')),
        'hands': list(map(lambda h: re.split(', ', h), re.split('; ', hands_text))),
    })


with open(filename, 'r') as f:
    read_data = f.read().splitlines()
f.close()

parsed_data = list(map(lambda line: parse_line(line), read_data))

result = 0
for game in parsed_data:
    possible = True
    for hands in game['hands']:
        for hand in hands:
            if hand.endswith('blue') and int(hand.replace(' blue', '')) > allowed['blue']:
                possible = False
            elif hand.endswith('red') and int(hand.replace(' red', '')) > allowed['red']:
                possible = False
            elif hand.endswith('green') and int(hand.replace(' green', '')) > allowed['green']:
                possible = False
    if possible:
        result += game['game']


print(result)
