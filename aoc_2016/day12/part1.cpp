#include "part1.hpp"

using namespace std;


Assembunny::Assembunny(const vector<Instruction> &instructions): myInstructions(instructions) {
    myRegisters = vector<int>(4, 0);
};


size_t Assembunny::registerId(const string &registerName) {
    return static_cast<size_t>(registerName[0] - 'a');
}


void Assembunny::runInstruction(const Instruction &instr) {
    if (instr.cmd == "cpy") {
        const bool useRegistry = string("abcd").find(instr.x) != string::npos;
        const int val = useRegistry ? myRegisters[registerId(instr.x)] : stoi(instr.x);
        myRegisters[registerId(instr.y)] = val;
        myPos++;
        return;
    }
    if (instr.cmd == "inc") {
        myRegisters[registerId(instr.x)]++;
        myPos++;
        return;
    }
    if (instr.cmd == "dec") {
        myRegisters[registerId(instr.x)]--;
        myPos++;
        return;
    }
    if (instr.cmd == "jnz") {
        const bool useRegistry = string("abcd").find(instr.x) != string::npos;
        const int val = useRegistry ? myRegisters[registerId(instr.x)] : stoi(instr.x);
        myPos += (val != 0) ? stoul(instr.y) : 1;
        return;
    }
}


void Assembunny::run() {
    while (myPos < myInstructions.size()) {
        if (myPos < 0)
            throw AdventException("Negative position found in the assembunny.");
        runInstruction(myInstructions[myPos]);
    }
}


int Assembunny::getRegister(const string &registerName) const {
    return myRegisters[registerId(registerName)];
}


void Assembunny::setRegister(const string &registerName, int val) {
    myRegisters[registerId(registerName)] = val;
}


vector<Instruction> Part1::parse(const string &fileName) {
    vector<Instruction> instructions;
    for (const string &line : getFileLines(fileName)) {
        const auto tokens = split(line, " ");
        const string cmd = tokens[0];
        const string x = tokens[1];
        const string y = tokens.size() > 2 ? tokens[2] : "";
        instructions.emplace_back(cmd, x, y);
    }
    return instructions;
}

int Part1::solve(vector<Instruction> instructions) {
    Assembunny assembunny(instructions);
    assembunny.run();
    return assembunny.getRegister("a");
}
