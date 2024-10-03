import re


def solve(rules):
    contained_colors = {}

    while len(contained_colors) < len(rules):
        for color in rules:
            # skip the rule if already processed
            if color in contained_colors:
                continue
            # process the rule if it is an empty bag
            if not len(rules[color]):
                contained_colors[color] = set()
                continue
            # skip the rule if all rules of the contained bags are not processed yet
            if not all([item_color in contained_colors for (_, item_color) in rules[color]]):
                continue
            # process the rule if all rules of contained bags are processed
            colors = set()
            for (_, item_color) in rules[color]:
                colors.add(item_color)
                colors = colors.union(contained_colors[item_color])
            contained_colors[color] = colors

    return len([x for x in contained_colors if 'shiny gold' in contained_colors[x]])


def parse(file_name):
    rules = {}
    with open(file_name, 'r') as f:
        for line in map(str.strip, f.readlines()):
            content = []
            color, items = re.match(r'([a-z ]+) bags contain ([0-9a-z ,]+)$', line[:-1]).groups()
            for item in items.split(', '):
                match = re.match(r'([0-9]+) ([a-z ]+) bag', item)
                if match:
                    quantity, item_color = match.groups()
                    content.append((int(quantity), item_color))
            rules[color] = content
        return rules


if __name__ == '__main__':
    print(solve(parse('data.txt')))
