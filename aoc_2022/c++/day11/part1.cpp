#include "part1.h"

using namespace std;


namespace Day11 {

    vector<Monkey> parse(const string& filename) {
        vector<Monkey> monkeys;
        const auto lines = getFileLines(filename);
        int curr = 0;
        while (curr < lines.size()) {
            ++curr;   // monkey declaration line
            const auto itemsVect  = split(split(lines[curr++], ": ")[1], ", ");
            const auto operation  = split(split(lines[curr++], "= old ")[1], " ");
            const auto test_val   = stoi(split(lines[curr++], " by ")[1]);
            const auto test_true  = stoi(split(lines[curr++], " monkey ")[1]);
            const auto test_false = stoi(split(lines[curr++], " monkey ")[1]);
            ++curr;   // empty line

            deque<long long> items {};
            transform(itemsVect.begin(), itemsVect.end(), back_inserter(items), [](const string& s) { return stoll(s); });

            monkeys.emplace_back(items,
                                array<string, 2> { operation[0], operation[1] },
                                array<int, 3>    { test_val, test_true, test_false });
        }
        return monkeys;
    }


    namespace Part1 {

        void playRound(vector<Monkey>& monkeys, vector<long long>& inspected, int multiplier) {
            for (int i = 0; i < monkeys.size(); ++i) {
                Monkey& monkey = monkeys[i];
                while (monkey.items.size() > 0) {

                    // inspect the object
                    ++inspected[i];
                    long long worry = monkey.items.front();
                    monkey.items.pop_front();
                    const long long val = monkey.operation[1] == "old" ? worry : stoll(monkey.operation[1]);
                    worry = (monkey.operation[0] == "*") ? worry * val : worry + val;

                    if (multiplier < 0) {
                        // part 1 : divide worry level by 3 after inspection
                        worry /= 3;
                    } else {
                        // part 2 : to avoid big numbers, use the remainder of the division by the multiplier
                        worry %= multiplier;
                    }

                    // throw the object to the next monkey
                    int target = (worry % monkey.test[0]) == 0LL ? monkey.test[1] : monkey.test[2];
                    monkeys[target].items.push_back(worry);
                }
            }
        }

        long long solve(const vector<Monkey>& monkeys) {
            vector<Monkey> monkeysCopy { monkeys };
            vector<long long> inspected(monkeys.size(), 0LL);
            for (int i = 0; i < 20; ++i) {
                playRound(monkeysCopy, inspected);
            }
            sort(inspected.begin(), inspected.end(), greater<long long>());
            return inspected[0] * inspected[1];
        }

    }
}
