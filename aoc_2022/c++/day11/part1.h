#pragma once
#include "../Common/Utils.h"


namespace Day11 {

    struct Monkey {
        Monkey(const std::deque<long long>& items, const std::array<std::string, 2>& op, const std::array<int, 3>& test)
          : items(items), operation(op), test(test) {}
        std::deque<long long> items;
        std::array<std::string, 2> operation;
        std::array<int, 3> test;
    };

    std::vector<Monkey> parse(const std::string& filename);

    namespace Part1 {

        void playRound(std::vector<Monkey>& monkeys, std::vector<long long>& inspected, int multiplier = -1);

        long long solve(const std::vector<Monkey>& monkeys);

    }
}
