#include "part1.hpp"

using namespace std;


IPv7::IPv7(const string &str) {
    string remaining = str;
    while (remaining.size() > 0) {
        auto hypernetIdx = remaining.find("[");
        if (hypernetIdx == string::npos) {
            // no hypernet sequence left
            mySupernetSequences.push_back(remaining);
            remaining = "";
        } else {
            mySupernetSequences.push_back(remaining.substr(0, hypernetIdx));
            auto hypernetEndIdx = remaining.find("]");  // we are sure it exists
            auto hypernetSize = hypernetEndIdx - hypernetIdx - 1; 
            myHypernetSequences.push_back(remaining.substr(hypernetIdx+1, hypernetSize));
            if (hypernetEndIdx == remaining.size()-1) {
                remaining = "";  // no sequence left after the hypernet
            } else {
                remaining = remaining.substr(hypernetEndIdx+1);
            }                
        }
    }
}

bool IPv7::supportTLS() const {
    auto hasABBA = [](const string &seq) {
        size_t pos = 0;
        while (pos + 3 < seq.size()) {
            if (seq.at(pos) == seq.at(pos+3)      // external pair
             && seq.at(pos+1) == seq.at(pos+2)    // internal pair
             && seq.at(pos) != seq.at(pos+1)) {   // the 2 pairs are different chars
                return true;
            }
            pos++;
        }
        return false;
    };
    // ensure hypernet sequences have no ABBA
    for (const auto &seq : myHypernetSequences) {
        if (hasABBA(seq)) {
            return false;
        }
    }
    // ensure normal sequences have a ABBA
    for (const auto &seq : mySupernetSequences) {
        if (hasABBA(seq)) {
            return true;
        }
    }
    return false;
}


vector<IPv7> Part1::parse(const string &filePath) {
    vector<IPv7> res;
    for (const auto &line : getFileLines(filePath)) {
        res.emplace_back(line);
    }
    return res;
}


int Part1::solve(const vector<IPv7> &ipv7s) {
    auto count = 0;
    for (const auto &ipv7 : ipv7s) {
        if (ipv7.supportTLS()) {
            count++;
        }
    }
    return count;
}
