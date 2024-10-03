#include "../day06/part1.h"
#include "../day06/part2.h"

using namespace std;
using namespace Day06;


int main(int argc, char* argv[]) {

    const auto start = chrono::high_resolution_clock::now();

    const string inputFilePath = argc > 1 ? argv[1] : "../day06/data.txt";
    const auto parsed = parse(inputFilePath);

    // part 1
    const auto resultPart1   = Part1::solve(parsed);
    const auto afterPart1    = chrono::high_resolution_clock::now();
    const auto durationPart1 = duration_cast<chrono::milliseconds>(afterPart1 - start).count();
    cout << "Part 1 : " << resultPart1 << "  (" << durationPart1 << " ms)" << endl;

    // part 2
    const auto resultPart2   = Part2::solve(parsed);
    const auto afterPart2    = chrono::high_resolution_clock::now();
    const auto durationPart2 = duration_cast<chrono::milliseconds>(afterPart2 - afterPart1).count();
    cout << "Part 2 : " << resultPart2 << "  (" << durationPart2 << " ms)" << endl;

    return 0;
}
