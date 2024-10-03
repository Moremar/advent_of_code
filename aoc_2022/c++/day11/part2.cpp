#include "part2.h"

using namespace std;

/**
 * When we do not divide the worry level by 3 at every inspection, the worry level gets very big quickly.
 * This worry level is only used to decide what monkey an item is thrown to, which is decided by the 
 * remainder of the division by the test value.
 * This means we do not need to keep the original worry level, we can use any value that would produce
 * the same remainder for that dision.
 * The easiest option is to divide the worry level by the product of all test values and keep only the remainder.
 */

namespace Day11 {
    namespace Part2 {

        long long solve(const vector<Monkey>& monkeys) {
            vector<Monkey> monkeysCopy { monkeys };
            vector<long long> inspected(monkeys.size(), 0LL);

            int multiplier = 1;
            for_each(monkeys.begin(), monkeys.end(), [&](const Monkey& monkey) {
                multiplier *= monkey.test[0];
            });

            for (int i = 0; i < 10'000; ++i) {
                Part1::playRound(monkeysCopy, inspected, multiplier);
            }
            sort(inspected.begin(), inspected.end(), greater<long long>());
            return inspected[0] * inspected[1];
        }

    }
}
