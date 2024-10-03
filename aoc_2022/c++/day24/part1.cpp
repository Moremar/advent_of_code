#include "part1.h"

using namespace std;

static const Coord NORTH { -1, 0 };
static const Coord EAST {  0, 1 };
static const Coord SOUTH { 1, 0 };
static const Coord WEST { 0, -1 };


namespace Day24 {

    tuple<Winds, Coord, Coord> parse(const string& filename) {
        map<Coord, set<Coord>> winds {};
        map<char, Coord> windMapping { { '>', EAST }, { '<', WEST }, { '^', NORTH }, { 'v', SOUTH } };
        const auto lines = getFileLines(filename);
        for (int i = 1; i < lines.size()-1; ++i) {
            for (int j = 1; j < lines[0].size()-1; ++j) {
                if (windMapping.find(lines[i][j]) != windMapping.end()) {
                    winds[Coord{ i, j }].insert(windMapping.at(lines[i][j]));
                }
            }
        }
        return {
            winds,
            Coord{ 0, 1 },
            Coord{ static_cast<int>(lines.size())-1, static_cast<int>(lines[0].size())-2 }
        };
    }


    namespace Part1 {

        void computeWinds(map<int, Winds>& winds, int step, int maxX, int maxY) {
            if (winds.find(step) == winds.end()) {
                for (const auto& [windPosition, windDirections] : winds.at(step-1)) {
                    for (const auto& windDirection : windDirections) {
                        Coord nextWindPosition { windPosition + windDirection };
                        if (nextWindPosition.x > maxX)      { nextWindPosition.x = 1;    }
                        else if (nextWindPosition.x < 1)    { nextWindPosition.x = maxX; }
                        else if (nextWindPosition.y > maxY) { nextWindPosition.y = 1;    }
                        else if (nextWindPosition.y < 1)    { nextWindPosition.y = maxY; }
                        winds[step][nextWindPosition].insert(windDirection);
                    }
                }
            }
        }

        int crossValley(map<int, Winds>& winds, int initialStep, const Coord& start, const Coord& target, int maxX, int maxY) {
            set<pair<int, Coord>> seen {};
            deque<pair<int, Coord>> toCheck { { initialStep, start } };
            while (toCheck.size() > 0) {
                const auto& [step, position] = toCheck.front();
                if (seen.find(toCheck.front()) != seen.end()) {
                    // this position has already been checked
                    toCheck.pop_front();
                    continue;
                }
                seen.insert(toCheck.front());
                computeWinds(winds, step+1, maxX, maxY);
                // add to the list to process all valid next positions
                vector<Coord> nextPositions { position.neighbors() };
                nextPositions.push_back(position);
                for (const auto& neighbor : nextPositions) {
                    if (neighbor == target) {
                        return step + 1;
                    }
                    if ( (neighbor != start) 
                      && (neighbor.x < 1 || neighbor.x > maxX || neighbor.y < 1 || neighbor.y > maxY) ) {
                        // we can't move to that position
                        continue;
                    }
                    if (winds[step+1].find(neighbor) == winds[step+1].end()) {
                        // no wind on this position, we can walk there
                        toCheck.emplace_back(step+1, neighbor);
                    }
                }
                toCheck.pop_front();
            }
            return -1;
        }


        int solve(const tuple<Winds, Coord, Coord>& input) {
            const auto [initialWinds, start, target] = input;
            const int maxX = target.x - 1;
            const int maxY = target.y;
            map<int, Winds> winds;
            winds[0] = initialWinds;
            return crossValley(winds, 0, start, target, maxX, maxY);
        }

    }
}
