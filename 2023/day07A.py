from utils import getInput

inputs = getInput(7)
hands = [x.split()[0] for x in inputs]
bids = [x.split()[1] for x in inputs]

types = {
    'high': [],
    'pair': [],
    'two': [],
    'three': [],
    'full_house': [],
    'four': [],
    'five': [],
}

for hand, bid in zip(hands, bids):
    cards = {}
    for card in hand:
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1
    
    if len(cards) == 5:
        types['high'].append((hand, bid))
    elif len(cards) == 4:
        types['pair'].append((hand, bid))
    elif len(cards) == 3:
        if 3 in cards.values():
            types['three'].append((hand, bid))
        else:
            types['two'].append((hand, bid))
    elif len(cards) == 2:
        if 4 in cards.values():
            types['four'].append((hand, bid))
        else:
            types['full_house'].append((hand, bid))
    else:
        types['five'].append((hand, bid))
    
def sort_func(tup):
    x = tup[0]
    positions = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14,
    }
    # print((12**4)*positions[x[0]] + (12**3)*positions[x[1]] + (12**2)*positions[x[2]] + 12*positions[x[3]] + positions[x[4]])
    return (13**4)*positions[x[0]] + (13**3)*positions[x[1]] + (13**2)*positions[x[2]] + 13*positions[x[3]] + positions[x[4]]

for x in types:
    types[x].sort(key=sort_func)

winnings = 0
rank = 1
for win in types.values():
    for hand in win:
        winnings += rank * int(hand[1])
        rank += 1

print(winnings)
        