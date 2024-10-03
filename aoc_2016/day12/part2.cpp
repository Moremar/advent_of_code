#include "part2.hpp"

using namespace std;


int Part2::solve(vector<Instruction> instructions) {
    Assembunny assembunny(instructions);
    assembunny.setRegister("c", 1);
    assembunny.run();
    return assembunny.getRegister("a");
}
