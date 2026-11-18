import functools

import numpy as np
import re

card_deck = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
hand_types = ['five of a kind', 'four of a kind', 'full house', 'three of a kind', 'two pair', 'one pair', 'high card']


def read_input(name):
    with open(name, 'r') as f:
        lines = f.read().splitlines()
    f.close()

    return lines


def parse_input(lines):
    return [re.split('\s', line) for line in lines]


def card_value(card):
    return len(card_deck) - card_deck.index(card)


def hand_type_value(hand_type):
    return len(hand_types) - hand_types.index(hand_type)


def analyze_hand(hand, bid):
    for card in card_deck:
        if hand.count(card) == 5 \
            or (card != 'J' and hand.count(card) + hand.count('J') == 5):
            return {'hand': hand, 'hand_type': 'five of a kind', 'cards': [card], 'value': hand_type_value('five of a kind'), 'bid': bid}
    for card in card_deck:
        if hand.count(card) == 4 \
            or (card != 'J' and hand.count(card) + hand.count('J') == 4):
            other_card = list(filter(lambda x: x != card, hand)).pop()
            return {'hand': hand, 'hand_type': 'four of a kind', 'cards': [card, other_card], 'value': hand_type_value('four of a kind'),
                    'bid': bid}
    for card1 in card_deck:
        for card2 in card_deck:
            if card1 == card2:
                continue
            if hand.count(card1) == 3 and hand.count(card2) == 2 \
                or (card1 != 'J' and card2 != 'J' and hand.count(card1) == 3 and hand.count(card2) + hand.count('J') == 2)\
                or (card1 != 'J' and card2 != 'J' and hand.count(card2) == 2 and hand.count(card1) + hand.count('J') == 3)\
                or (card1 != 'J' and card2 != 'J' and hand.count('J') == 2 and hand.count(card1) == 1 and hand.count(card2) == 2)\
                or (card1 != 'J' and card2 != 'J' and hand.count('J') == 1 and hand.count(card1) == 1 and hand.count(card2) == 3):
                return {'hand': hand, 'hand_type': 'full house', 'cards': [card1, card2], 'value': hand_type_value('full house'),
                        'bid': bid}
    for card in card_deck:
        if hand.count(card) == 3 \
            or (card != 'J' and hand.count(card) + hand.count('J') == 3):
            other_cards = list(filter(lambda x: x != card, hand))
            other_sorted_cards = list(filter(lambda x: x in other_cards, card_deck))
            return {'hand': hand, 'hand_type': 'three of a kind', 'cards': [card] + other_sorted_cards,
                    'value': hand_type_value('three of a kind'), 'bid': bid}
    for card1 in card_deck:
        for card2 in card_deck:
            if card1 == card2:
                continue
            if hand.count(card1) == 2 and hand.count(card2) == 2 \
                or (card1 != 'J' and card2 != 'J' and hand.count(card1) == 2 and hand.count(card2) + hand.count('J') == 2) \
                or (card1 != 'J' and card2 != 'J' and hand.count(card2) == 2 and hand.count(card1) + hand.count('J') == 2):
                other_card = list(filter(lambda x: x != card1 and x != card2, hand)).pop()
                higher_card = card1 if card_value(card1) > card_value(card2) else card2
                lower_card = card1 if card_value(card1) < card_value(card2) else card2
                return {'hand': hand, 'hand_type': 'two pair', 'cards': [higher_card, lower_card, other_card],
                        'value': hand_type_value('two pair'), 'bid': bid}
    for card in card_deck:
        if hand.count(card) == 2 or (card != 'J' and hand.count(card) + hand.count('J') == 2):
            other_cards = list(filter(lambda x: x != card, hand))
            other_sorted_cards = list(filter(lambda x: x in other_cards, card_deck))
            return {'hand': hand, 'hand_type': 'one pair', 'cards': [card] + other_sorted_cards, 'value': hand_type_value('one pair'),
                    'bid': bid}
    sorted_cards = list(filter(lambda x: x in hand, card_deck))
    return {'hand': hand, 'hand_type': 'high card', 'cards': sorted_cards, 'value': hand_type_value('high card'), 'bid': bid}


def compare_hands(analysed_hand1, analysed_hand2):
    if analysed_hand1['value'] != analysed_hand2['value']:
        return analysed_hand1['value'] - analysed_hand2['value']

    for i in range(max(len(analysed_hand1['cards']), len(analysed_hand2['cards']))):
        if i > len(analysed_hand1['cards']) - 1:
            return +1
        if i > len(analysed_hand2['cards']) - 1:
            return -1
        if card_value(analysed_hand1['cards'][i]) < card_value(analysed_hand2['cards'][i]):
            return -1
        if card_value(analysed_hand1['cards'][i]) > card_value(analysed_hand2['cards'][i]):
            return +1
    return 0


def compare_hands_with_cards(analysed_hand1, analysed_hand2):
    if analysed_hand1['value'] < analysed_hand2['value']:
        return -1
    if analysed_hand1['value'] > analysed_hand2['value']:
        return +1
    for i in range(len(analysed_hand1['hand'])):
        if card_value(analysed_hand1['hand'][i]) < card_value(analysed_hand2['hand'][i]):
            return -1
        if card_value(analysed_hand1['hand'][i]) > card_value(analysed_hand2['hand'][i]):
            return +1

    return 0


def main(filename):
    read_lines = read_input(filename)
    parsed_input = parse_input(read_lines)

    analysed_hands = [analyze_hand(line[0], int(line[1])) for line in parsed_input]
    sorted_analysed_hands = sorted(analysed_hands, reverse=False, key=functools.cmp_to_key(compare_hands_with_cards))
    print(np.array(sorted_analysed_hands))

    result = 0
    for i, analysed_hand in enumerate(sorted_analysed_hands):
        result += (i + 1) * analysed_hand['bid']

    return result


# filename = 'sample.txt'
filename = 'input.txt'
print('Result', main(filename))
