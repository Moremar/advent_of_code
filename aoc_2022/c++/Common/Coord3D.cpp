#include "Coord3D.h"
#include <cmath>       // abs

using namespace std;


Coord3D Coord3D::operator+(const Coord3D& o) const {
    return { x + o.x, y  + o.y, z + o.z };
}

Coord3D& Coord3D::operator+=(const Coord3D& o) {
    x += o.x;
    y += o.y;
    z += o.z;
    return *this;
}

// spaceship operator
strong_ordering Coord3D::operator<=>(const Coord3D& o) const {
    if (x < o.x || (x == o.x && y < o.y) || (x == o.x && y == o.y && z < o.z)) {
        return strong_ordering::less;
    }
    if (x == o.x && y == o.y && z == o.z) {
        return strong_ordering::equal;
    }
    return strong_ordering::greater;
}

vector<Coord3D> Coord3D::neighbors() const {
    return { {x-1, y, z}, {x+1, y, z}, {x, y-1, z}, {x, y+1, z}, {x, y, z-1}, {x, y, z+1} };
}
