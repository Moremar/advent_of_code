#include "part1.hpp"

using namespace std;


string getPattern(char c) {
    ostringstream oss;
    oss << c << c << c << c << c;
    return oss.str();
}


KeyGenerator::KeyGenerator(const string &salt)
  : mySalt(salt) {
    const string hexa = "0123456789abcdef";
    for (const auto &c : hexa) {
        myPendingKeys.insert({ getPattern(c), {} });
    }
}


void KeyGenerator::updatePending() {
    for (auto &pendingKey: myPendingKeys) {
        std::erase_if(pendingKey.second, [this](const auto &elem) {
            return elem + 1000 < myCurrIdx;
        });
    }
}


string getHash(const string &str, int iters) {
    return iters == 0 ? md5(str) : getHash(md5(str), iters -1);
}


int KeyGenerator::findIthKey(int targetKey, int stretchLevel) {
    int stopIdx = -1;
    while (myCurrIdx != stopIdx) {
        // regular cleanup
        if (myCurrIdx % 100 == 0) updatePending();
            
        const string hash = getHash(mySalt + to_string(myCurrIdx), stretchLevel);
        bool hasTriple = false;
        char repeatedChar;
        for (size_t i = 0; i < hash.size() - 2; ++i) {
            if (hash.at(i) == hash.at(i+1) && hash.at(i) == hash.at(i+2)) {
                hasTriple = true;
                repeatedChar = hash.at(i);
                break;
            }
        }
        // only check for 5 consecutive letters if a triplet was found
        if (hasTriple) {
            updatePending();
            for (auto &pendingKey: myPendingKeys) {
                if (!pendingKey.second.empty() && hash.find(pendingKey.first) != string::npos) {
                    // add all pending keys with that searchPattern to the keys
                    for (const auto &key : pendingKey.second) {
                        myFoundKeys.insert(key);
                    }
                    pendingKey.second.clear();

                    // we cannot stop immediately when we get the target number of keys, as there
                    // may be valid smaller keys not revealed yet, so we need to check another 1000
                    // keys to validate all potential smaller keys
                    if (stopIdx == -1 && (int)myFoundKeys.size() >= targetKey) {
                        stopIdx = myCurrIdx + 1001;
                    }
                }
            }
            // insert the new pending key after validation so it does not validate itself
            // in case of 5 consecutive chars
            myPendingKeys[getPattern(repeatedChar)].insert(myCurrIdx);
        }
        myCurrIdx++;
    }

    vector<int> res(myFoundKeys.begin(), myFoundKeys.end());
    return res[63];
}


string Part1::parse(const string &fileName) {
    return getFileLines(fileName)[0];
}


int Part1::solve(const string &salt) {
    KeyGenerator generator(salt);
    return generator.findIthKey(64, 0);
}
