#include "part1.hpp"

using namespace std;


bool Room::isReal() const {
    // get the frequence of each letter in the encrypted name
    map<char, int> freq;
    for (const char &c : encryptedName) {
        if (c == '-') {
            continue;
        } else if (freq.find(c) != freq.end())
        {
            freq[c]++;
        } else {
            freq.insert({c, 1});
        }
    }
    // sort the letters by frequence and alphabetical order
    vector<pair<char, int>> toSort(freq.begin(), freq.end());
    sort(toSort.begin(), toSort.end(), [](const pair<char, int> v1, pair<char, int> v2) {
        return (v1.second > v2.second) || (v1.second ==  v2.second && v1.first < v2.first);
    });
    // ensure the first 5 letters are the checksum
    string top5;
    for (size_t i = 0; i < 5; i++) {
        top5 += toSort[i].first;
    }
    return top5 == checksum;
}


vector<Room> Part1::parse(const string &filePath) {
    vector<Room> res;
    regex rgx("([a-z-]+)-([0-9]+)\\[([a-z]+)\\]");
    for (const string &line : getFileLines(filePath)) {
        smatch match;
        if (regex_search(line.begin(), line.end(), match, rgx)) {
            res.emplace_back(match[1], stoi(match[2]), match[3]);
        }
    }
    return res;
}


int Part1::solve(vector<Room> data) {
    auto sum = 0;
    for (const Room &room : data) {
        if (room.isReal()) {
            sum += room.sectorId;
        }
    }
    return sum;
}