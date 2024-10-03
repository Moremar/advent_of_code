#include "part2.hpp"

using namespace std;


string Part2::solve(const string &doorId) {
    int index = 0;
    int resolved = 0;
    string password = "        ";
    const string validIndexVals = "01234567";

    while (resolved < 8) {
        const auto hash = md5(doorId + to_string(index));
        if (hash.substr(0, 5) == "00000") {
            if (validIndexVals.find(hash[5]) != string::npos) {
                size_t pos = static_cast<size_t>(hash[5] - '0');
                if (password[pos] == ' ') {
                    password[pos] = hash[6];
                    resolved++;
                }
            }
        }
        index++;
    }
    return password;
}
