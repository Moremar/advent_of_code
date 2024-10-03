#include "part1.h"
#include "../Common/Utils.h"

#include <cassert>
#include <numeric>   // std::reduce
#include <iostream>

using namespace std;

namespace Day10 {
    namespace Part2 {
        string solve(const vector<pair<Operator_t, int>>& commands) {
            int cycle = 0, pixel = 0, regX = 1;
            string res = "\n";
            for (const auto& [op, val] : commands) {
                int duration = (op == Operator_t::addx) ? 2 : 1;
                for (int i = 1; i <= duration; ++i) {
                    ++cycle;
                    res += (pixel >= regX - 1 && pixel <= regX + 1) ? "#" : ".";
                    if (cycle % 40 == 0) res += "\n";
                    if (i == duration) regX += val;
                    pixel = (pixel + 1) % 40;
                }
            }
            return res;
        }
    }
}
