import re


class Item:
    def __init__(self, name, cost, damage, defense):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.defense = defense


class Equipment:
    def __init__(self, weapon, armor, ring1, ring2):
        self.weapon = weapon
        self.armor = armor
        self.ring1 = ring1
        self.ring2 = ring2
        self.damage = weapon.damage + ring1.damage + ring2.damage
        self.defense = armor.defense + ring1.defense + ring2.defense
        self.cost = weapon.cost + armor.cost + ring1.cost + ring2.cost


WEAPONS = [Item("Dagger", 8, 4, 0), Item("Shortsword", 10, 5, 0), Item("Warhammer", 25, 6, 0),
           Item("Longsword", 40, 7, 0), Item("Greataxe", 74, 8, 0)]

ARMORS = [Item("No Armor", 0, 0, 0), Item("Leather", 13, 0, 1), Item("Chainmail", 31, 0, 2),
          Item("Splintmail", 53, 0, 3), Item("Bandedmail", 75, 0, 4), Item("Platemail", 102, 0, 5)]

RINGS = [Item("Dmg+1", 25, 1, 0), Item("Dmg+2", 50, 2, 0), Item("Dmg+3", 100, 3, 0),
         Item("Def+1", 20, 0, 1), Item("Def+2", 40, 0, 2), Item("Def+3", 80, 0, 3),
         Item("No ring", 0, 0, 0)]


def possible_equipments():
    equipments = []
    for weapon in WEAPONS:
        for armor in ARMORS:
            for ring1 in RINGS:
                for ring2 in RINGS:
                    if ring1.cost >= ring2.cost:
                        continue  # to avoid (r1, r2) and (r2, r1), we say r1 is the cheapest ring
                    equipments.append(Equipment(weapon, armor, ring1, ring2))
            equipments.append(Equipment(weapon, armor, Item("No ring", 0, 0, 0), Item("No ring", 0, 0, 0)))
    equipments.sort(key=lambda x: x.cost)
    return equipments


def win_battle(boss, equipment):
    (boss_hp, boss_damage, boss_defense) = boss
    hp = 100
    while True:
        boss_hp -= max(1, (equipment.damage - boss_defense))
        if boss_hp <= 0:
            return True
        hp -= max(1, (boss_damage - equipment.defense))
        if hp <= 0:
            return False


def solve(boss):
    for equipment in possible_equipments():
        if win_battle(boss, equipment):
            return equipment.cost


def parse(file_name):
    with open(file_name, "r") as f:
        _, hp, _ = re.split(r"Hit Points: ([0-9]+)", f.readline())
        _, damage, _ = re.split(r"Damage: ([0-9]+)", f.readline())
        _, defense, _ = re.split(r"Armor: ([0-9]+)", f.readline())
        return int(hp), int(damage), int(defense)


if __name__ == '__main__':
    print(solve(parse("data.txt")))
