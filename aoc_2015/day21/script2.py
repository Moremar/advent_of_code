from script1 import parse, possible_equipments, win_battle


def solve(boss):
    equipments = possible_equipments()
    equipments.reverse()  # from more expensive to cheapest
    for equipment in equipments:
        if not win_battle(boss, equipment):
            return equipment.cost


if __name__ == '__main__':
    print(solve(parse("data.txt")))
