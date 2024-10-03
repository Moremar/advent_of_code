#include "part1.hpp"

using namespace std;


Assembunny::Assembunny(const vector<Instruction> &instructions, const string &logFile)
    : myInstructions(instructions), myLogFile(logFile) {
    myRegisters = vector<int>(4, 0);
};


size_t Assembunny::registerId(const string &registerName) {
    return static_cast<size_t>(registerName[0] - 'a');
}


void Assembunny::run() {
    ofstream myfile;
    myfile.open(myLogFile, ios::trunc);
    myfile << myRegisters[0] << " " << myRegisters[1] << " " << myRegisters[2] << " " << myRegisters[3] << endl; 

    while (myPos < myInstructions.size()) {
        if (myPos < 0)
            throw AdventException("Negative position found in the assembunny.");

        const auto &instr = myInstructions[myPos];
        myfile << "[" << myRegisters[0] << " " << myRegisters[1] << " " << myRegisters[2] << " " << myRegisters[3] << "]  "; 
        myfile << instr.str() << endl;

        if (instr.cmd == "cpy") {
            if ("abcd"s.find(instr.y) == string::npos) {
                // invalid command (possibly due to a tgl)
                myPos++;
                continue;
            }
            const bool useRegistry = "abcd"s.find(instr.x) != string::npos;
            const int val = useRegistry ? myRegisters[registerId(instr.x)] : stoi(instr.x);
            myRegisters[registerId(instr.y)] = val;
            myPos++;
            continue;
        }
        if (instr.cmd == "inc") {
            myRegisters[registerId(instr.x)]++;
            myPos++;
            continue;
        }
        if (instr.cmd == "dec") {
            myRegisters[registerId(instr.x)]--;
            myPos++;
            continue;
        }
        if (instr.cmd == "mul") {
            // Added for part 2
            const bool useRegistryX = string("abcd").find(instr.x) != string::npos;
            const int valX = useRegistryX ? myRegisters[registerId(instr.x)] : stoi(instr.x);
            myRegisters[registerId(instr.y)] *= valX;
            myPos++;
            continue;
        }
        if (instr.cmd == "add") {
            // Added for part 2
            const bool useRegistryX = string("abcd").find(instr.x) != string::npos;
            const int valX = useRegistryX ? myRegisters[registerId(instr.x)] : stoi(instr.x);
            myRegisters[registerId(instr.y)] += valX;
            myPos++;
            continue;
        }
        if (instr.cmd == "jnz") {
            const bool useRegistryX = string("abcd").find(instr.x) != string::npos;
            const int valX = useRegistryX ? myRegisters[registerId(instr.x)] : stoi(instr.x);
            const bool useRegistryY = string("abcd").find(instr.y) != string::npos;
            const size_t valY = useRegistryY ? (size_t) myRegisters[registerId(instr.y)] : stoul(instr.y);
            myPos += (valX != 0) ? valY : 1;
            continue;
        }
        if (instr.cmd == "tgl") {
            const bool useRegistry = string("abcd").find(instr.x) != string::npos;
            const int val = useRegistry ? myRegisters[registerId(instr.x)] : stoi(instr.x);
            if ((int)myPos + val < 0) {
                // out of scope, ignore it
                myPos++;
                continue;
            }
            const size_t toggledPos = static_cast<size_t>((int)myPos + val);
            if (toggledPos >= myInstructions.size()) {
                // out of scope, ignore it
                myPos++;
                continue;
            }
            if (myInstructions[toggledPos].cmd == "inc")      myInstructions[toggledPos].cmd = "dec";
            else if (myInstructions[toggledPos].cmd == "dec") myInstructions[toggledPos].cmd = "inc";
            else if (myInstructions[toggledPos].cmd == "tgl") myInstructions[toggledPos].cmd = "inc";
            else if (myInstructions[toggledPos].cmd == "jnz") myInstructions[toggledPos].cmd = "cpy";
            else if (myInstructions[toggledPos].cmd == "cpy") myInstructions[toggledPos].cmd = "jnz";
            else if (myInstructions[toggledPos].cmd == "mul") throw AdventException("UNEXPECTED");
            else if (myInstructions[toggledPos].cmd == "add") throw AdventException("UNEXPECTED");
            myPos++;
            continue;
        }
    }
    myfile.close();
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
    Assembunny assembunny(instructions, "./day23/history_part1.log");
    assembunny.setRegister("a", 7);
    assembunny.run();
    return assembunny.getRegister("a");
}
