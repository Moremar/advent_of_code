#pragma once
#include "Utils.hpp"


class State {
public:
    State(const Coordinates &coords, const string &password, const string &path);
    vector<State> getNextStates() const;
    Coordinates getCoordinates() const { return myCoords; };
    string getPath() const { return myPath; };
private:
    Coordinates myCoords;
    string myPassword;
    string myPath;
};


namespace Part1 {  
    string parse(const string &fileName);
    string solve(const string &password);
}
