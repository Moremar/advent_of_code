#pragma once
#include "Utils.hpp"


struct Instruction {
    Instruction(const string &type, const char &X, const char &Y): type(type), X(X), Y(Y) {}
    string type;
    char X;
    char Y;
};


class Scrambler {
public:
    Scrambler(const vector<Instruction> &instructions) : myInstructions(instructions) {}
    string scramble(const string &clearPwd);
private:
    vector<Instruction> myInstructions;
};


namespace Part1 {  
    pair<string, vector<Instruction>> parse(const string &fileName);
    string solve(const pair<string, vector<Instruction>> &input);

    string processInstruction(const Instruction &instr, const string &pwd);
}
