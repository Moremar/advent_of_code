from script1 import parse
import re

# There are too many combinations to generate all possible molecules of the target size
# Even starting from the target molecule and trying all possible reductions is not feasible
# We try the heuristic to always apply the reduction with the longest right part (so the molecule shrinks quickly)
# Depending on the input, there may have cases where this solution leads to a non-shrinkable molecule.
# For my input file I was lucky, it reduced back to "e"


def solve(data):
    (reactions, molecule) = data
    reactions.sort(key=lambda x: len(x[1]), reverse=True)
    count = 0
    while len(molecule) > 1:
        found = False
        for reaction in reactions:
            if re.search(r"({0})".format(reaction[1]), molecule):
                index = molecule.index(reaction[1])
                molecule = molecule[:index] + reaction[0] + molecule[index + len(reaction[1]):]
                count += 1
                found = True
                break
        if not found:
            print("WARN - Could not reduce more the molecule")
            break
    return molecule + " reached in " + str(count) + " steps"


if __name__ == '__main__':
    print(solve(parse("data.txt")))
