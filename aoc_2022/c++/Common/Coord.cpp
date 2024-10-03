#include "Coord.h"
#include <cmath>       // abs

using namespace std;


// initialize static members
const Coord Coord::WEST  = { -1,  0 };
const Coord Coord::EAST  = {  1,  0 };
const Coord Coord::NORTH = {  0, -1 };
const Coord Coord::SOUTH = {  0,  1 };


Coord Coord::operator+(const Coord& o) const {
    return { x + o.x, y  + o.y };
}

Coord& Coord::operator+=(const Coord& o) {
    x += o.x;
    y += o.y;
    return *this;
}

// spaceship operator
strong_ordering Coord::operator<=>(const Coord& o) const {
    if (x < o.x || (x == o.x && y < o.y)) {
        return strong_ordering::less;
    }
    if (x == o.x && y == o.y) {
        return strong_ordering::equal;
    }
    return strong_ordering::greater;
}

int Coord::manhattan(const Coord& c1, const Coord& c2) {
    return abs(c1.x - c2.x) + abs(c1.y - c2.y);
}

vector<Coord> Coord::neighbors() const {
    return { {x-1, y}, {x+1, y}, {x, y-1}, {x, y+1} };
}
