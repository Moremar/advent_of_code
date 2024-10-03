#include "part1.hpp"
#include "part2.hpp"

using namespace std;


map<Coordinates, string> KEYPAD {
    { {2, 0}, "1" }, { {1, 1}, "2" }, { {2, 1}, "3" },
    { {3, 1}, "4" }, { {0, 2}, "5" }, { {1, 2}, "6" },
    { {2, 2}, "7" }, { {3, 2}, "8" }, { {4, 2}, "9" },
    { {1, 3}, "A" }, { {2, 3}, "B" }, { {3, 3}, "C" },
    { {2, 4}, "D" }
};

bool in_keypad(const Coordinates &position) {
    return KEYPAD.find(position) != KEYPAD.end();
}

void Part2::next_position(const char& c, Coordinates &coords) {
    switch (c) {
        case 'U':
            if (in_keypad(make_pair(coords.first, coords.second - 1))) coords.second--;
            break;
        case 'R':
            if (in_keypad(make_pair(coords.first + 1, coords.second))) coords.first++;
            break;
        case 'D':
            if (in_keypad(make_pair(coords.first, coords.second + 1))) coords.second++;
            break;
        case 'L':
            if (in_keypad(make_pair(coords.first - 1, coords.second))) coords.first--;
            break;
        default:
            throw AdventException(string("Undefined direction: ") + c);
    }
}

string Part2::solve(vector<vector<char>> directions) {
    Coordinates coords(0, 2);
    string code;
    for(const vector<char> &dirLine : directions) {
        for (const char &c: dirLine) {
            next_position(c, coords);
        }
        code += KEYPAD[coords];
    }
    return code;
}
