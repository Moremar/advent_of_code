#include "part1.hpp"
#include "part2.hpp"

using namespace std;


int main() {
    const auto data = Part1::parse("./day11/data.txt");
    cout << "Part 1: " << Part1::solve(data) << endl;
    const auto data2 = Part1::parse("./day11/data2.txt");
    cout << "Part 2: " << Part1::solve(data2) << endl;
    return 0;
}
