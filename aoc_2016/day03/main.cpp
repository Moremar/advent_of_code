#include "part1.hpp"
#include "part2.hpp"

using namespace std;


int main() {
    const auto data1 = Part1::parse("./day03/data.txt");
    cout << "Part 1: " << Part1::solve(data1) << endl;

    // Same solve() but different parse()
    const auto data2 = Part2::parse("./day03/data.txt");
    cout << "Part 2: " << Part1::solve(data2) << endl;

    return 0;
}
