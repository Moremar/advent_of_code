import re


class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories


def cookie_score(ingredients, ratios):
    capacity, durability, flavor, texture = (0, 0, 0, 0)
    for ingredient in ingredients:
        capacity += ingredients[ingredient].capacity * ratios[ingredient]
        durability += ingredients[ingredient].durability * ratios[ingredient]
        flavor += ingredients[ingredient].flavor * ratios[ingredient]
        texture += ingredients[ingredient].texture * ratios[ingredient]
    return max(0, capacity) * max(0, durability) * max(0, flavor) * max(0, texture)


def best_cookie(ingredients, so_far, to_use, space, score_func):
    if len(to_use) == 1:
        so_far = dict(so_far)  # take a copy
        so_far[to_use[0]] = space
        return score_func(ingredients, so_far)
    max_cookie_score = 0
    for i in range(0, space + 1):
        so_far[to_use[0]] = i
        max_local = best_cookie(ingredients, so_far, to_use[1:], space - i, score_func)
        if max_local > max_cookie_score:
            max_cookie_score = max_local
    return max_cookie_score


def solve(ingredients):
    return best_cookie(ingredients, {}, [ingredient for ingredient in ingredients], 100, cookie_score)


def parse(file_name):
    with open(file_name, "r") as f:
        ingredients = {}
        for line in f.readlines():
            _, ingredient, capacity, durability, flavor, texture, calories, _ = re.split(
                r"([A-Za-z]+): .* ([-0-9]+), .* ([-0-9]+), .* ([-0-9]+), .* ([-0-9]+), .* ([-0-9]+)", line)
            ingredients[ingredient] = Ingredient(ingredient, int(capacity), int(durability),
                                                 int(flavor), int(texture), int(calories))
        return ingredients


if __name__ == '__main__':
    print(solve(parse("data.txt")))
