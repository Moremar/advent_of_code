#pragma once
#include "Utils.hpp"


struct Room {
    string encryptedName;
    size_t sectorId;
    string checksum;

    Room(const string &encryptedName, size_t sectorId, const string &checksum):
        encryptedName(encryptedName), sectorId(sectorId), checksum(checksum) {}
    
    bool isReal() const;
};


namespace Part1 {
    vector<Room> parse(const string &filePath);
    int solve(vector<Room> data);
}