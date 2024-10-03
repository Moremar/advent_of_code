from part1 import parse, valid
import math


def valid_ticket(ticket, rules):
    for val in ticket:
        if not any([valid(val, rule) for rule in rules]):
            return False
    return True


def solve(data):
    rules, my_ticket, tickets = data
    tickets = [ticket for ticket in tickets if valid_ticket(ticket, rules)]

    # mapping[i] is the list of possible positions of the ith field in the tickets
    # once resolved, there should be just 1 position left in each mapping[i]
    mapping = [list(range(len(rules))) for _ in range(len(rules))]

    # step 1 : remove the positions of invalid fields in the mapping
    for ticket in tickets:
        for (pos, val) in enumerate(ticket):
            for field_id in range(len(mapping)):
                if pos in mapping[field_id] and not valid(val, rules[field_id]):
                    mapping[field_id].remove(pos)

    # step 2 : resolve the unique combination of fields verifying these constraints
    processed = []
    while len(processed) < len(rules):
        for i in range(len(rules)):
            if i not in processed and len(mapping[i]) == 1:
                # only one possible position for this field_id so we remove it from the list of other fields
                pos = mapping[i][0]
                for k in range(len(rules)):
                    if k != i and pos in mapping[k]:
                        mapping[k].remove(pos)
                processed.append(i)

    return math.prod([my_ticket[mapping[i][0]] for i in range(len(rules)) if 'departure' in rules[i][0]])


if __name__ == "__main__":
    print(solve(parse("data.txt")))
