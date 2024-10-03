#include "part1.hpp"

using namespace std;


vector<string> Part1::parse(const string &filePath) {
    return getFileLines(filePath);
}


vector<map<char, int>> Part1::getFreqs(const vector<string> &signals) {
    vector<map<char, int>> freqs;
    // count the number of occurences of each letter at each position
    for (const string &signal : signals) {        
        for (size_t i = 0; i < signal.size(); i++) {
            if (freqs.size() <= i) {
                freqs.push_back(map<char, int>());
            }
            const char c = signal[i];
            if (freqs[i].find(c) == freqs[i].end()) {
                freqs[i].insert({c, 1});
            } else {
                freqs[i][c]++;
            }
        }
    }
    return freqs;
}

string Part1::solve(const vector<string> &signals) {
    const auto freqs = getFreqs(signals);
    // pick the most popular letter for each position
    string corrected = "";
    for (const auto freq : freqs) {
        vector<pair<char, int>> toSort(freq.cbegin(), freq.cend());
        sort(toSort.begin(), toSort.end(), [](pair<char, int> v1, pair<char, int> v2) {
            return (v1.second > v2.second) || (v1.second == v2.second && v1.first < v2.first);
        });
        corrected += toSort[0].first;
    }
    return corrected;
}
