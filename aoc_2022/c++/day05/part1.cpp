#include "part1.h"

using namespace std;


namespace Day05 {

    Parsed parse(const string& filename) {

        vector<deque<char>> stacks;
        vector<Instruction> instructions;

        const regex pattern { "move (\\d+) from (\\d+) to (\\d+)" };
        const auto lines = getFileLines(filename);

        // initialize the stacks
        for (int k = 0; k < (lines[0].size() + 1) / 4; ++k){
            stacks.push_back(deque<char>{});
        }

        int i = 0;
        while (contains(lines[i], "[")) {
            for (int k = 0; k < stacks.size(); ++k) {
                char c = lines[i][1 + k*4];
                if (c != ' ') {
                    stacks[k].push_front(c);
                }
            }
            ++i;
        }

        for (auto line = lines.cbegin() + i + 2; line != lines.cend(); ++line) {
            smatch match;
            regex_search(line->begin(), line->end(), match, pattern);
            instructions.push_back(Instruction{ stoi(match[1]),  stoi(match[2])-1, stoi(match[3])-1 });
        }
        return Parsed{ stacks, instructions };
    }

    namespace Part1 {
        string solve(const Parsed& parsed) {
            auto stacks = parsed.stacks;
            for_each(parsed.instructions.begin(), parsed.instructions.end(), [&stacks](const Instruction& instruction) {
                for (int k=0; k < instruction.count; ++k) {
                    stacks[instruction.dest].push_back((stacks[instruction.src].back()));
                    stacks[instruction.src].pop_back();
                }
            });

            string result = "";
            for_each(stacks.begin(), stacks.end(), [&result](const deque<char>& stack) {
                result += stack.back();
            }) ;

            return result;
        }
    }
}
