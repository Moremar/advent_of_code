"""Solution for AOC 2024 day 24"""


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        init_str, links_str = file.read().split('\n\n')
        initial_state = {}
        links = {}
        for line in init_str.split('\n'):
            k, v = line.strip().split(': ')
            initial_state[k] = int(v)
        for line in links_str.split('\n'):
            w1, op, w2, _, res = line.strip().split()
            links[res] = (w1, op, w2)
        return initial_state, links


def resolve(wire, initial_state, links):
    """Get the value for a given wire"""
    if wire in initial_state:
        return initial_state[wire]
    (w1, op, w2) = links[wire]
    w1_val = resolve(w1, initial_state, links)
    w2_val = resolve(w2, initial_state, links)
    if op == 'XOR':
        return 1 if w1_val != w2_val else 0
    if op == 'AND':
        return 1 if w1_val == w2_val == 1 else 0
    return 1 if w1_val == 1 or w2_val == 1 else 0


def solve1(initial_state, links):
    """Solve part 1"""
    idx = 0
    res = ''
    while f'z{idx:02}' in links:
        res = f'{resolve(f'z{idx:02}', initial_state, links)}' + res
        idx += 1
    return int(res, 2)


def solve2(_, links):
    """Solve part 2"""

    # There are too many combinations of 4 pairs of wires to brute-force the solution.
    # Instead, we need to understand the logic of the adder program.
    # it follows a regular pattern for each bit, so we can identify anomalies.
    to_swap = set()
    for wire in links:
        # all z wires result from a XOR rule
        if wire[0] == 'z' and links[wire][1] != 'XOR' and wire != 'z45':
            to_swap.add(wire)
            continue
        # all (x, y) bit pair have a XOR and a AND rule
        (w1, op, w2) = links[wire]
        bit_id = int(w1[1:]) if w1[0] == 'x' else int(w2[1:]) if w2[0] == 'x' else -1
        next_wires = [w for w in links if wire in [links[w][0], links[w][2]]]
        if bit_id != -1 and op == 'XOR':
            # The resulting wire of the XOR rule should have a XOR and an AND rule
            # (except the first one z00)
            if wire != 'z00' and len(next_wires) != 2:
                to_swap.add(wire)
                continue
            for next_wire in next_wires:
                if links[next_wire][1] == 'XOR' and next_wire != f'z{bit_id:02}':
                    to_swap.add(next_wire)
                    continue
        elif bit_id != -1 and op == 'AND':
            # the resulting wire of the AND rule should have a OR rule
            if len(next_wires) != 1 and 'z01' not in next_wires:
                to_swap.add(wire)

    return ','.join(sorted(to_swap))


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 24:', solve1(*parsed), solve2(*parsed))
