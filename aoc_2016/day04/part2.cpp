#include "part2.hpp"

using namespace std;


const string ALPHABET = "abcdefghijklmnopqrstuvwxyz";


string decryptName(const Room &room) {
    string res;
    for (const char &c : room.encryptedName) {
        if (c == '-') {
            res += ' ';
        } else {
            res += ALPHABET[(ALPHABET.find(c) + room.sectorId) % 26];
        }
    }
    return res;
}


int Part2::solve(vector<Room> data) {
    for (const Room &room : data) {
        if (room.isReal()) {
            const auto decrypted = decryptName(room);
            if (decrypted.find("northpole") != string::npos) {
                return room.sectorId;
            }
        }
    }
    throw AdventException("No room found containing 'northpole'.");
}