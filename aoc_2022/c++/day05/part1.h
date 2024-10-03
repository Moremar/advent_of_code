#pragma once
#include "../Common/Utils.h"

struct Instruction {
    int count;
    int src;
    int dest;
};

struct Parsed {
    std::vector<std::deque<char>> stacks;
    std::vector<Instruction> instructions;
};

namespace Day05 {
    Parsed parse(const std::string& filename);

    namespace Part1 {
        string solve(const Parsed& input);
    }
}
