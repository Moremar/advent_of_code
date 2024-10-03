#include "part1.hpp"
#include "part2.hpp"

using namespace std;


string Part2::solve(const vector<string> &signals) {
    vector<map<char, int>> freqs = Part1::getFreqs(signals);
    // pick the least popular letter for each position
    string corrected = "";
    for (const auto freq : freqs) {
        vector<pair<char, int>> toSort(freq.cbegin(), freq.cend());
        // sort in the opposite order from part 1
        sort(toSort.begin(), toSort.end(), [](pair<char, int> v1, pair<char, int> v2) {
            return (v1.second < v2.second) || (v1.second == v2.second && v1.first > v2.first);
        });
        corrected += toSort[0].first;
    }
    return corrected;
}
