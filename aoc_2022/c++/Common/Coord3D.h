#pragma once

#include <compare>   // for <=> operator
#include <vector>

/**
 * Coordinates class for a 3D point
 */
struct Coord3D {

    // constructor
    Coord3D(int x, int y, int z): x(x), y(y), z(z) {}
    Coord3D() = default;

    // operator overload
    Coord3D operator+(const Coord3D& o) const;
    Coord3D& operator+=(const Coord3D& o);
    std::strong_ordering operator<=>(const Coord3D& o) const;
    bool operator==(const Coord3D& o) const = default;

    std::vector<Coord3D> neighbors() const;

    // member variables
    int x { 0 };
    int y { 0 };
    int z { 0 };
};
