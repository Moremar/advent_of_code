#pragma once
#include "../Common/Utils.h"


namespace Day14 {

    using World = std::map<Coord, char>;

    World parse(const std::string& filename);


    namespace Part1 {

        bool dropSand(World& world, int deepestPath, bool hasFloor = false);

        // print the sand flow in the terminal
        // not required to solve the puzzle, but it looks pretty cool
        void print(const World& world);

        int solve(const World& world);

    }
}
