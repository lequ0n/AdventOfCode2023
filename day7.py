with open('input.txt', 'r') as f:
    data = f.read().splitlines()

# 1
d = {'A': 50, 'K': 40, 'Q': 30, 'J': 20, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
hands_and_bids = [(tuple([d[y] for y in x.split()[0]]), int(x.split()[1])) for x in data]


def hand_score(hand):
    card_types = {}
    for card in hand[0]:
        card_types[card] = card_types.get(card, 0) + 1
    score = 1
    if max(t := card_types.values()) == 5: score = 7
    elif max(t) == 4: score = 6
    elif 3 in t and 2 in t: score = 5
    elif 3 in t: score = 4
    elif list(t).count(2) == 2: score = 3
    elif 2 in t: score = 2
    return (score, hand[0])


hands_and_bids.sort(key=hand_score)
print(sum([rank * bid[1] for rank, bid in enumerate(hands_and_bids, start=1)]))

# 2
d['J'] = 1
hands_and_bids = [(tuple([d[y] for y in x.split()[0]]), int(x.split()[1])) for x in data]


def hand_score2(hand):
    card_types = {}
    for card in hand[0]:
        card_types[card] = card_types.get(card, 0) + 1
    jokers = card_types.get(1, 0)
    card_types[1] = 0
    score = 1
    if max(t := card_types.values()) + jokers == 5: score = 7
    elif max(t) + jokers == 4: score = 6
    elif (3 in t and 2 in t) or (2 in t and jokers == 2) or (list(t).count(2) == 2 and jokers == 1): score = 5
    elif 3 in t or (2 in t and jokers == 1) or jokers == 2: score = 4
    elif list(t).count(2) == 2: score = 3
    elif 2 in t or jokers == 1: score = 2
    return (score, hand[0])


hands_and_bids.sort(key=hand_score2)
print(sum([rank * bid[1] for rank, bid in enumerate(hands_and_bids, start=1)]))
