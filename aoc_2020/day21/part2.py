from part1 import parse, reduce_allergens


def solve(recipes):
    allergens = reduce_allergens(recipes)
    solved = set()
    while len(solved) < len(allergens):
        for allergen in allergens:
            if len(allergens[allergen]) == 1:
                solved.add(list(allergens[allergen])[0])
            else:
                allergens[allergen] = allergens[allergen].difference(solved)
    return ','.join([list(allergens[allergen])[0] for allergen in sorted(allergens.keys())])


if __name__ == "__main__":
    print(solve(parse("data.txt")))
