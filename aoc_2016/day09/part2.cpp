#include "part1.hpp"
#include "part2.hpp"

using namespace std;


/**
 * In part 2, the decompressed word has above 10 billion characters, so trying to generate
 * it takes forever.
 * Instead, we go through the letters of the compressed file and calculate how many times
 * each one will appear in the decompressed file.
 * Each letter starts with a score of 1, and this score is multiplied every time a marker 
 * including that letter is found.
 */

size_t countLetters(const string &compressed) {
    auto occurences = vector<size_t>(compressed.size(), 1);
    size_t pos = 0;
    regex rgx("\\(([0-9]+)x([0-9]+)\\)");
    while(pos < compressed.size()) {
        if (compressed.at(pos) != '(') {
            pos++;
            continue;
        }
        // found a marker
        const auto markerSize = compressed.substr(pos).find(")") + 1;
        const string marker = compressed.substr(pos, markerSize);
        smatch match;
        regex_search(marker.begin(), marker.end(), match, rgx);
        const size_t repeatChars = stoul(match[1]);
        const size_t repeatTimes = stoul(match[2]);
        // multiply occurences of all letters in the repeated block
        for (size_t i = 0; i < repeatChars; ++i) {
            occurences[pos + markerSize + i] *= repeatTimes;
        }
        // set the occurence of the marker to 0
        for (size_t i = 0; i < markerSize; ++i) {
           occurences[pos + i] = 0;
        }
        pos += markerSize;
    }
    return accumulate(occurences.begin(), occurences.end(), (size_t)0);
}


size_t Part2::solve(const string &compressed) {
    return countLetters(compressed);
}
