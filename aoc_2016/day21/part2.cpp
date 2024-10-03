#include "part1.hpp"
#include "part2.hpp"

using namespace std;


Instruction oppositeInstruction(const Instruction &instr) {
    if (instr.type == "SwapPos")     return instr;
    if (instr.type == "SwapLetter")  return instr;
    if (instr.type == "Reverse")     return instr;
    if (instr.type == "RotateLeft")  return Instruction("RotateRight", instr.X, ' ');
    if (instr.type == "RotateRight") return Instruction("RotateLeft", instr.X, ' ');
    if (instr.type == "RotateBased") return Instruction("OppositeBased", instr.X, ' ');
    if (instr.type == "Move")        return Instruction("Move", instr.Y, instr.X);
    throw AdventException("Invalid instruction type : " + instr.type);
}

string Part2::solve(const pair<string, vector<Instruction>> &input) {
    vector<Instruction> reversed;
    transform(input.second.rbegin(), input.second.rend(), back_inserter(reversed), [](const Instruction &instr) {
        return oppositeInstruction(instr);
    });
    Scrambler scrambler(reversed);
    return scrambler.scramble("fbgdceah");
}
