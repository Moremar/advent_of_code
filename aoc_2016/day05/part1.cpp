#include "part1.hpp"

using namespace std;


string Part1::parse(const string &filePath) {
    return getFileLines(filePath)[0];
}


string Part1::solve(const string &doorId) {
    int index = 0;
    int resolved = 0;
    string password = "";
    while (resolved < 8) {
        const auto hash = md5(doorId + to_string(index));
        if (hash.substr(0, 5) == "00000") {
            password += hash[5];
            resolved++;
        }
        index++;
    }
    return password;
}
