#include "part2.hpp"

using namespace std;

/**
 * When checking the instructions, we notice that the following block is a double loop
 * doing  a += b * d  then setting c and d to 0 :
 * 
 *    cpy b c
 *    inc a
 *    dec c
 *    jnz c -2
 *    dec d
 *    jnz d -5
 * 
 *  We create the mul and add instructions, and replace the below block by :
 * 
 *    mul b d
 *    add d a
 *    cpy 0 c
 *    cpy 0 d
 *    cpy 0 d           // "do nothing" isntruction just to keep the size
 *    cpy 0 d           // "do nothing" isntruction just to keep the size
 */


int Part2::solve(const vector<Instruction> &instructions) {

    // replace the double loop by a multiplication
    auto optimized = instructions;
    optimized[4] = Instruction("mul", "b", "d");
    optimized[5] = Instruction("add", "d", "a");
    optimized[6] = Instruction("cpy", "0", "c");
    optimized[7] = Instruction("cpy", "0", "d");
    optimized[8] = Instruction("cpy", "0", "d");  // filler
    optimized[9] = Instruction("cpy", "0", "d");  // filler

    Assembunny assembunny(optimized, "./day23/history_part2.log");
    assembunny.setRegister("a", 12);
    assembunny.run();
    return assembunny.getRegister("a");
}
