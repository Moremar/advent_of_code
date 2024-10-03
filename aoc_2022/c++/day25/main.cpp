#include "../day25/part1.h"

using namespace std;
using namespace Day25;


int main(int argc, char* argv[]) {

    const auto start = chrono::high_resolution_clock::now();

    const string inputFilePath = argc > 1 ? argv[1] : "../day25/data.txt";
    const auto parsed = parse(inputFilePath);

    // part 1
    const auto resultPart1   = Part1::solve(parsed);
    const auto afterPart1    = chrono::high_resolution_clock::now();
    const auto durationPart1 = duration_cast<chrono::milliseconds>(afterPart1 - start).count();
    cout << "Part 1 : " << resultPart1 << "  (" << durationPart1 << " ms)" << endl;

    // no part 2 for day 25

    return 0;
}
