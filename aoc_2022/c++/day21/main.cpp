#include "../day21/part1.h"
#include "../day21/part2.h"

using namespace std;
using namespace Day21;


int main(int argc, char* argv[]) {

    const auto start = chrono::high_resolution_clock::now();

    const string inputFilePath = argc > 1 ? argv[1] : "../day21/data.txt";

    // part 1
    const auto parsedPart1   = parse<long long>(inputFilePath);
    const auto resultPart1   = Part1::solve(parsedPart1);
    const auto afterPart1    = chrono::high_resolution_clock::now();
    const auto durationPart1 = duration_cast<chrono::milliseconds>(afterPart1 - start).count();
    cout << "Part 1 : " << resultPart1 << "  (" << durationPart1 << " ms)" << endl;

    // part 2
    // instanciate monkeys with complex values
    // all monkeys have integer values, except "humn" monkey that will have value i
    // this way, we can separate the value of "humn" monkey from all other monkeys in the calculation
    const auto parsedPart2   = parse<complex<long double>>(inputFilePath);
    const auto resultPart2   = Part2::solve(parsedPart2);
    const auto afterPart2    = chrono::high_resolution_clock::now();
    const auto durationPart2 = duration_cast<chrono::milliseconds>(afterPart2 - afterPart1).count();
    cout << "Part 2 : " << resultPart2 << "  (" << durationPart2 << " ms)" << endl;

    return 0;
}
