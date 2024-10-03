#include "part1.h"
#include "../Common/Utils.h"

using namespace std;

namespace Day10 {

    vector<pair<Operator_t, int>> parse(const string& filename) {
        vector<pair<Operator_t, int>> parsed;
        for (const string& line : getFileLines(filename)) {
            const auto splitted = split(line, " ");
            if (splitted[0] == "addx") {
                parsed.emplace_back(Operator_t::addx, stoi(splitted[1]));
            } else {
                parsed.emplace_back(Operator_t::noop, 0 /* unused */);
            }
        }
        return parsed;
    }

    namespace Part1 {
        int solve(const vector<pair<Operator_t, int>>& commands) {
            int cycle = 0, res = 0, regX = 1;
            for (const auto& [op, val] : commands) {
                int duration = (op == Operator_t::addx) ? 2 : 1;
                for (int i = 1; i <= duration; ++i) {
                    ++cycle;
                    if (cycle % 40 == 20) { res  += cycle * regX; }
                    if (i == duration)    { regX += val; }
                }
            }
            return res;
        }
    }
}
