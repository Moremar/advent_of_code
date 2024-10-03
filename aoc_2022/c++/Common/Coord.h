#pragma once

#include <compare>   // for <=> operator
#include <vector>

/**
 * Coordinates class for a 2D point
 */
struct Coord {

    // constructor
    Coord(int x, int y): x(x), y(y) {}
    Coord() = default;

    // operator overload
    Coord operator+(const Coord& o) const;
    Coord& operator+=(const Coord& o);
    std::strong_ordering operator<=>(const Coord& o) const;
    bool operator==(const Coord& o) const = default;

    // manhattan distance between 2 coordinates
    static int manhattan(const Coord& c1, const Coord& c2);

    std::vector<Coord> neighbors() const;

    // member variables
    int x { 0 };
    int y { 0 };

    // unit vectors
    static const Coord WEST, EAST, NORTH, SOUTH;
};
