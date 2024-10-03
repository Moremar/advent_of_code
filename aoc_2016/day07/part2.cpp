#include "part2.hpp"

using namespace std;


bool IPv7::supportSSL(
) const {
    auto getABAs = [](const string &seq) {
        vector<string> abas;
        size_t pos = 0;
        while (pos + 2 < seq.size()) {
            if (seq.at(pos) == seq.at(pos+2)      // external pair
             && seq.at(pos) != seq.at(pos+1)) {   // the 2 pairs are different chars
                abas.push_back(seq.substr(pos, 3));
            }
            pos++;
        }
        return abas;
    };
    // get all ABAs in the supernet sequences
    vector<string> abas;
    for (const auto &seq : mySupernetSequences) {
        const vector<string> abasInSeq = getABAs(seq);
        abas.insert(abas.end(), abasInSeq.cbegin(), abasInSeq.cend());
    }
    // check if any ABA from the supernet has its corresponding BAB in the hypernet
    for (const auto &seq : myHypernetSequences) {
        for (const auto &aba : abas) {
            string bab = "";
            bab.push_back(aba.at(1));
            bab.push_back(aba.at(0));
            bab.push_back(aba.at(1));
            if (seq.find(bab) != string::npos) {
                return true;
            }
        }
    }
    return false;
}


int Part2::solve(const vector<IPv7> &ipv7s) {
    auto count = 0;
    for (const auto &ipv7 : ipv7s) {
        if (ipv7.supportSSL()) {
            count++;
        }
    }
    return count;
}
