from script1 import parse, optimize_spells, State


def solve(boss):
    (boss_hp, boss_dmg) = boss
    initial_state = State(50 - 1, 500, boss_hp, boss_dmg, True)  # -1 for the first HP lost
    return optimize_spells(initial_state, [])[0]


if __name__ == '__main__':
    print(solve(parse("data.txt")))
