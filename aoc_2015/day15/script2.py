from script1 import parse, best_cookie


def cookie_score(ingredients, ratios):
    """Cookie score function giving a 0 score if the calories are not 500"""
    capacity, durability, flavor, texture, calories = (0, 0, 0, 0, 0)
    for ingredient in ingredients:
        capacity += ingredients[ingredient].capacity * ratios[ingredient]
        durability += ingredients[ingredient].durability * ratios[ingredient]
        flavor += ingredients[ingredient].flavor * ratios[ingredient]
        texture += ingredients[ingredient].texture * ratios[ingredient]
        calories += ingredients[ingredient].calories * ratios[ingredient]
    if calories != 500:
        return 0
    else:
        return max(0, capacity) * max(0, durability) * max(0, flavor) * max(0, texture)


def solve(ingredients):
    return best_cookie(ingredients, {}, [ingredient for ingredient in ingredients], 100, cookie_score)


if __name__ == '__main__':
    print(solve(parse("data.txt")))
