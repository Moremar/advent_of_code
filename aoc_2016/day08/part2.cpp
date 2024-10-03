#include "part2.hpp"

using namespace std;


string Monitor::screenDisplay() const {
    ostringstream oss;
    oss << endl;
    for (const auto &row : myScreen) {
        for (const auto &val : row) {
            oss << val << " ";
        }
        oss << endl;
    }
    return oss.str();
}


string Part2::solve(const vector<Instruction> &instructions) {
    Monitor monitor;
    for (const auto &instruction : instructions) {
        monitor.execute(instruction);
    }
    return monitor.screenDisplay();
}
