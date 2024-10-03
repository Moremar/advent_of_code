
def solve(decks):
    deck1, deck2 = decks
    while len(deck1) and len(deck2):
        card1, card2 = deck1.pop(0), deck2.pop(0)
        if card1 > card2:
            deck1 += [card1, card2]
        else:
            deck2 += [card2, card1]
    winner = deck1 if len(deck1) else deck2
    return sum([i * winner[len(winner)-i] for i in range(1, len(winner)+1)])


def parse(file_name):
    decks = []
    with open(file_name, 'r') as f:
        for block in f.read().split('\n\n'):
            decks.append([int(line) for line in block.split('\n')[1:]])
    return decks


if __name__ == "__main__":
    print(solve(parse("sample.txt")))
