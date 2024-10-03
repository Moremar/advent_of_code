#include "part1.h"

using namespace std;


namespace Day14 {

    vector<Coord> getLine(const Coord& p1, const Coord& p2) {
        // only support horizontal or vertical lines
        assert (p1.x == p2.x || p1.y == p2.y);

        // get the smallest point first
        if ( (p1.x == p2.x && p1.y > p2.y) || (p1.y == p2.y && p1.x > p2.x)) {
            return getLine(p2, p1);
        }
        vector<Coord> line {};
        for (int i = 0; i <= p2.x - p1.x + p2.y - p1.y; ++i) {
            line.emplace_back(p1.x + (p1.x != p2.x ? i : 0), p1.y + (p1.y != p2.y ? i : 0));
        }
        return line;
    }

    World parse(const string& filename) {
        World world;
        for (const auto line : getFileLines(filename)) {
            vector<Coord> vertices {};
            for (const auto coords : split(line, " -> ")) {
                const auto tokens = split(coords, ",");
                vertices.emplace_back(stoi(tokens[0]), stoi(tokens[1]));
            }
            for (int i = 1; i < vertices.size(); ++i) {
                for (const auto p : getLine(vertices[i-1], vertices[i])) {
                    world[p] = '#';
                }
            }
        }
        return world;
    }

    namespace Part1 {

        bool dropSand(World& world, int deepestPath, bool hasFloor) {
            Coord sand { 500, 0 };
            if (world.find(sand) != world.end()) {
                // can no longer drop sand
                return false;
            }
            bool atRest = false;
            while (!atRest) {
                if (!hasFloor && sand.y >= deepestPath) {
                    // the sand flows into the abyss, it will never come to rest
                    return false;
                }
                if (hasFloor && sand.y == deepestPath + 1) {
                    // the sand reached the floor
                    atRest = true;
                    world[sand] = 'o';
                    return true;
                }
                Coord below { sand.x, sand.y+1 };
                if (world.find(below) == world.end()) {
                    sand = move(below);
                    continue;
                }
                Coord belowLeft { sand.x-1, sand.y+1 };
                if (world.find(belowLeft) == world.end()) {
                    sand = move(belowLeft);
                    continue;
                }
                Coord belowRight { sand.x+1, sand.y+1 };
                if (world.find(belowRight) == world.end()) {
                    sand = move(belowRight);
                    continue;
                }
                atRest = true;
                world[sand] = 'o';
                return true;
            }
            return false;
        }

        void print(const World& world) {
            int minX = 500, maxX = 500, minY = 0, maxY = 0;
            for (const auto& [coord, _] : world) {
                minX = min(minX, coord.x);
                maxX = max(maxX, coord.x);
                minY = min(minY, coord.y);
                maxY = max(maxY, coord.y);
            }
            ostringstream oss;
            oss << endl;
            for (int y = minY; y <= maxY + 1; ++y) {
                for (int x = minX-1; x <= maxX+1; ++x) {
                    oss << (world.find({ x, y }) == world.end() ? '.' : world.at({ x, y }));
                }
                oss << endl;
            }
            cout << oss.str();
        }

        int solve(const World& world) {
            World worldCopy { world };
            int deepestPath = 0;
            for (const auto& [coord, _] : worldCopy) {
                deepestPath = max(deepestPath, coord.y);
            }
            // flow sand until it flows into the abyss
            bool atRest = true;
            int droppedSand = 0;
            while (atRest) {
                atRest = dropSand(worldCopy, deepestPath);
                ++droppedSand;
            }
            // print(worldCopy);
            return droppedSand - 1;
        }

    }
}
