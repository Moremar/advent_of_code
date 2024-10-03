#pragma once
#include "Utils.hpp"


struct Instruction {
    Instruction(const string &type, size_t a, size_t b): type(type), a(a), b(b) {};
    string type;    // rect | row | column
    size_t a, b;
};


class Monitor {
public:
    Monitor();
    void execute(const Instruction &instruction);
    int countPixels() const;
    string screenDisplay() const;

private:
    vector<vector<char>> myScreen;
};


namespace Part1 {
    vector<Instruction> parse(const string &filePath);
    int solve(const vector<Instruction> &instructions);
}
