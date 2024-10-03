from part1 import parse


def serialize_config(deck1, deck2):
    return '.'.join(map(str, deck1)) + '|' + '.'.join(map(str, deck2))


def play_game(deck1, deck2):
    seen_configs = set()
    while len(deck1) and len(deck2):
        config = serialize_config(deck1, deck2)
        if config in seen_configs:
            return (1, deck1, deck2)
        seen_configs.add(config)
        card1, card2 = deck1.pop(0), deck2.pop(0)
        if len(deck1) < card1 or len(deck2) < card2:
            # not enough cards to recurse
            if card1 > card2:
                deck1 += [card1, card2]
            else:
                deck2 += [card2, card1]
        else:
            # determine round winner by recursion
            player, _, _ = play_game(list(deck1[:card1]), list(deck2[:card2]))
            if player == 1:
                deck1 += [card1, card2]
            else:
                deck2 += [card2, card1]
    return (1 if len(deck1) else 2, deck1, deck2)


def solve(decks):
    player, deck1, deck2 = play_game(*decks)
    winner = deck1 if player == 1 else deck2
    return sum([i * winner[len(winner)-i] for i in range(1, len(winner)+1)])


if __name__ == "__main__":
    print(solve(parse("data.txt")))
