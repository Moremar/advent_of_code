"""Solution for AOC 2024 day 23"""


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        links = {}
        for (c1, c2) in [tuple(line.strip().split('-')) for line in file.readlines()]:
            if c1 not in links:
                links[c1] = set()
            if c2 not in links:
                links[c2] = set()
            links[c1].add(c2)
            links[c2].add(c1)
        return links


def get_tri_lans(links):
    """Return all groups of 3 interconnected machines"""
    tri_lans = set()
    for c1 in links:
        for c2 in links[c1]:
            for c3 in links[c1]:
                if c2 != c3 and c2 in links[c3]:
                    tri_lans.add(tuple(sorted([c1, c2, c3])))
    return tri_lans


def solve1(links):
    """Solve part 1"""
    return len([1 for (c1, c2, c3) in get_tri_lans(links) if 't' in [c1[0], c2[0], c3[0]]])


def solve2(links):
    """Solve part 2"""
    groups = [(tri_lan, links[tri_lan[0]]) for tri_lan in get_tri_lans(links)]
    changed = True
    while changed:
        changed = False
        next_groups = []
        seen_keys = set()
        for (group, candidates) in groups:
            next_candidates = []
            for c in candidates:
                if all(c in links[c2] for c2 in group):
                    next_candidates.append(c)
            for (i, c) in enumerate(next_candidates):
                next_group = set(group)
                next_group.add(c)
                next_group_key = ','.join(next_group)
                if next_group_key in seen_keys:
                    continue
                seen_keys.add(next_group_key)
                next_groups.append((next_group, next_candidates[:i] + next_candidates[i+1:]))
                changed = True
        if changed:
            groups = next_groups
    return ','.join(sorted(list(groups[0][0])))


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 23:', solve1(parsed), solve2(parsed))
