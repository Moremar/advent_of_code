#pragma once
#include "Utils.hpp"


struct Instruction {
    Instruction(const string &lowDest, const string &highDest)
        : lowDest(lowDest), highDest(highDest) {};
    string lowDest, highDest;
};


struct FactoryRules {
    map<string, set<int>> initialChips; 
    map<string, Instruction> instructions;
};


class Factory {
public:
    Factory(const FactoryRules &rules);
    string run(int targetLow, int targetHigh);
    int getChip(const string &loc) const;
private:
    map<string, set<int>> myChips;
    map<string, Instruction> myInstructions;
};


namespace Part1 {
    FactoryRules parse(const string &filePath);
    string solve(const FactoryRules &rules);
}
