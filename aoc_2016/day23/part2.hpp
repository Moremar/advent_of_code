#pragma once
#include "part1.hpp"
#include "Utils.hpp"

using std::vector;


class Assembunny2 {
public:
    Assembunny2(const vector<Instruction> &instructions);
    void run();
    int getRegister(const string &registerName) const;
    void setRegister(const string &registerName, int val);
private:
    vector<Instruction> myInstructions;
    size_t myPos = 0;
    vector<int> myRegisters;

    // convert register name to ID ("a" -> 0)
    static size_t registerId(const string &registerName);
};

namespace Part2 {
    int solve(const vector<Instruction> &instructions);
}
