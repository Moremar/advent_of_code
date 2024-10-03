#include "part1.hpp"
#include "part2.hpp"

using namespace std;


int main() {
    const auto data = Part1::parse("./day25/data.txt");
    cout << "Part 1: " << Part1::solve(data) << endl;
    cout << "(No part 2)" << endl;
    return 0;
}
