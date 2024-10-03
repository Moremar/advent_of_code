#include "part2.h"

using namespace std;


namespace Day05 {
    namespace Part2 {
        string solve(const Parsed& parsed) {
            auto stacks = parsed.stacks;
            deque<char> tmpStack {};  // temporary stack to reverse the destacked elements
            for_each(parsed.instructions.begin(), parsed.instructions.end(), [&stacks, &tmpStack](const Instruction& instruction) {
                // destack items from the source stack into the temporary stack
                for (int k=0; k < instruction.count; ++k) {
                    tmpStack.push_back((stacks[instruction.src].back()));
                    stacks[instruction.src].pop_back();
                }
                // put the destacked chars in the original order into the destination stack
                for (int k=0; k < instruction.count; ++k) {
                    stacks[instruction.dest].push_back((tmpStack.back()));
                    tmpStack.pop_back();
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
