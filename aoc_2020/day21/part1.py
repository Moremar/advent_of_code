import re


def reduce_allergens(recipes):
    allergens = {}
    for recipe in recipes:
        for allergen in recipe[1]:
            if allergen not in allergens:
                allergens[allergen] = set(recipe[0])
            else:
                allergens[allergen] = allergens[allergen].intersection(set(recipe[0]))
    return allergens


def solve(recipes):
    allergens = reduce_allergens(recipes)
    ingredients = set().union(*[recipe[0] for recipe in recipes])
    hazardous = set().union(*[allergens[allergen] for allergen in allergens])
    safe = ingredients.difference(hazardous)
    return sum([len(set(recipe[0]).intersection(safe)) for recipe in recipes])


def parse(file_name):
    recipes = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            ingredients, allergens = re.fullmatch(r'(.*) \(contains (.*)\)', line.strip()).groups()
            recipes.append((set(ingredients.split(' ')), set(allergens.split(', '))))
        return recipes


if __name__ == "__main__":
    print(solve(parse("data.txt")))
