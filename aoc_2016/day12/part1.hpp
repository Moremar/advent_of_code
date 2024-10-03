#pragma once
#include "Utils.hpp"


struct Instruction {
    Instruction(const string &cmd, const string &x, const string &y) : cmd(cmd), x(x), y(y) {}
    string cmd, x, y;
};


class Assembunny {
public:
    Assembunny(const vector<Instruction> &instructions);
    void runInstruction(const Instruction &instruction);
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


namespace Part1 {  
    vector<Instruction> parse(const string &fileName);
    int solve(vector<Instruction> instructions);
}
