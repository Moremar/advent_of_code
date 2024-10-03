import re
from math import inf

SPELL_COST = {1: 53, 2: 73, 3: 113, 4: 173, 5: 229}


class State:
    def __init__(self, hp, mana, boss_hp, boss_dmg, hard=False):
        self.hp = hp
        self.mana = mana
        self.boss_hp = boss_hp
        self.boss_dmg = boss_dmg
        self.shield = 0
        self.poison = 0
        self.recharge = 0
        self.mana_spent = 0
        self.hard = hard

    def pre_turn(self):
        if self.shield > 0:
            self.shield -= 1  # No effect at start of turn
        if self.poison > 0:
            self.poison -= 1
            self.boss_hp -= 3
        if self.recharge > 0:
            self.recharge -= 1
            self.mana += 101

    def castable(self):
        # can cast only if enough mana, and cannot cast an effect already active
        spells = [i for i in range(1, 6) if SPELL_COST[i] <= self.mana]
        if self.shield > 0 and 3 in spells:
            spells.remove(3)
        if self.poison > 0 and 4 in spells:
            spells.remove(4)
        if self.recharge > 0 and 5 in spells:
            spells.remove(5)
        return spells

    def cast(self, spell):
        self.mana -= SPELL_COST[spell]
        self.mana_spent += SPELL_COST[spell]
        if spell == 1:         # Magic Missile
            self.boss_hp -= 4
        elif spell == 2:       # Drain
            self.boss_hp -= 2
            self.hp += 2
        elif spell == 3:       # Shield
            self.shield = 6
        elif spell == 4:       # Poison
            self.poison = 6
        elif spell == 5:       # Recharge
            self.recharge = 5

    def boss_attack(self):
        self.hp -= self.boss_dmg - (7 if self.shield > 0 else 0)

    def play(self, spell):
        self.cast(spell)
        if self.boss_hp <= 0:
            return 1
        self.pre_turn()  # before the boss turn
        if self.hp <= 0:
            return -1
        elif self.boss_hp <= 0:
            return 1
        self.boss_attack()
        if self.hp <= 0:
            return -1
        if self.hard:
            self.hp -= 1
            if self.hp <= 0:
                return -1
        self.pre_turn()  # before the player turn
        if self.boss_hp <= 0:
            return 1
        return 0

    def copy(self):
        c = State(self.hp, self.mana, self.boss_hp, self.boss_dmg, self.hard)
        c.shield = self.shield
        c.poison = self.poison
        c.recharge = self.recharge
        c.mana_spent = self.mana_spent
        return c


def optimize_spells(state, spells_so_far):
    spells = state.castable()
    (best_mana, best_spells) = inf, spells_so_far
    for spell in spells:
        next_state = state.copy()
        res = next_state.play(spell)
        if res == 1:
            if next_state.mana_spent < best_mana:
                best_mana = next_state.mana_spent
                best_spells = spells_so_far + [spell]
        elif res == 0:
            (sub_best_mana, sub_best_spells) = optimize_spells(next_state, spells_so_far + [spell])
            if sub_best_mana < best_mana:
                best_mana = sub_best_mana
                best_spells = sub_best_spells
    return best_mana, best_spells


def solve(boss):
    (boss_hp, boss_dmg) = boss
    initial_state = State(50, 500, boss_hp, boss_dmg)
    return optimize_spells(initial_state, [])[0]


def parse(file_name):
    with open(file_name, "r") as f:
        _, hp, _ = re.split("Hit Points: ([0-9]+)", f.readline())
        _, dmg, _ = re.split("Damage: ([0-9]+)", f.readline())
        return int(hp), int(dmg)


if __name__ == '__main__':
    print(solve(parse("data.txt")))
