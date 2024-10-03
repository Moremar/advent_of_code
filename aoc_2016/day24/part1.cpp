#include "part1.hpp"

using namespace std;


World::World(const map<Coordinates, char> &worldMap): worldMap(worldMap) {
    buildGraph();
    simplifyGraph();
}

size_t World::getKeysCount() const {
    return keys.size();
}

bool World::hasKey(const Coordinates &node) const {
    return keys.find(node) != keys.end();
}

char World::getKey(const Coordinates &node) const {
    return keys.at(node);
}

map<Coordinates, map<Coordinates, int>> World::getGraph() const {
    return graph;
}

Coordinates World::getStartPoint() const {
    for (const auto node: keys) {
        if (node.second == '0') return node.first;
    }
    throw AdventException("No start point found.");
}

void World::buildGraph() {
    for (const auto &point : worldMap) {
        const auto coord = point.first;
        if (worldMap.at(coord) == '#') continue;
        if (worldMap.at(coord) != '.') keys.insert({coord, worldMap.at(coord)});

        graph.insert({coord, {}});
        set<Coordinates> neighbors = {
            {coord.first - 1, coord.second},
            {coord.first + 1, coord.second},
            {coord.first, coord.second + 1},
            {coord.first, coord.second - 1},
        };
        for (const auto &neighbor : neighbors) {
            if (worldMap.find(neighbor) == worldMap.end()) continue;
            if (worldMap.at(neighbor) == '#') continue;
            graph.at(coord).insert({neighbor, 1});
        }
    }
}

void World::simplifyGraph() {
    bool reduced = false;
    while (!reduced) {
        reduced = true;
        for (auto nodePtr = graph.begin(); nodePtr != graph.end(); ++nodePtr) {
            auto node = *nodePtr;
            if (keys.find(node.first) != keys.end()) {
                // key nodes cannot be reduced
                continue;
            }
            // remove circular paths
            if (node.second.find(node.first) != node.second.end()) {
                node.second.erase(node.first);                
                reduced = false;
            }
            // trim excluded node
            if (node.second.size() == 0) {
                graph.erase(nodePtr);
                reduced = false;
                break;
            }
            // trim node with a single neighbor
            if (node.second.size() == 1) {
                // remove current node from its neighbor's list
                auto neighbor = node.second.begin()->first;
                graph.at(neighbor).erase(node.first);
                // remove current node
                graph.erase(nodePtr);
                reduced = false;
                break;
            }
            // simplify when a node has 2 neighbors
            if (node.second.size() == 2) {
                auto neighbor1 = node.second.begin()->first;
                auto neighbor2 = (++node.second.begin())->first;
                const auto dist = node.second.at(neighbor1) + node.second.at(neighbor2);
                // link the 2 neigbhors to each other
                if (graph.at(neighbor1).find(neighbor2) == graph.at(neighbor1).end()) {
                    graph.at(neighbor1).insert({ neighbor2, dist });
                    graph.at(neighbor2).insert({ neighbor1, dist });
                } else {
                    graph.at(neighbor1).at(neighbor2) = min(dist, graph.at(neighbor1).at(neighbor2));
                    graph.at(neighbor2).at(neighbor1) = min(dist, graph.at(neighbor2).at(neighbor1));
                }
                // remove current node from its neighbor's list
                graph.at(neighbor1).erase(node.first);
                graph.at(neighbor2).erase(node.first);
                // remove current node
                graph.erase(nodePtr);
                reduced = false;
                break;
            }
        }
    }
}

bool State::operator<(const State other) const {
    if (dist < other.dist) return true;
    if (dist > other.dist) return false;
    if (keys.size() > other.keys.size()) return true;
    if (keys.size() < other.keys.size()) return false;
    if (keys < other.keys) return true;
    if (keys > other.keys) return false;
    return pos < other.pos;
}

string getKeysStr(const set<char> &keys) {
    ostringstream oss;
    for (const auto &key : keys) oss << key;
    return oss.str();
}

int Part1::findSmallestRoute(const World &world, bool goBackHome) {
    const auto targetKeys = world.getKeysCount() + (goBackHome ? 1 : 0);
    const auto startCoord = world.getStartPoint();
    const auto graph = world.getGraph();

    State initialState(startCoord, { '0' }, 0);
    set<State> toCheck = { initialState };
    map<string, map<Coordinates, int>> seen;  // keys -> (pos -> best dist)

    while (!toCheck.empty()) {
        // pop the smallest state to check
        auto currState = *toCheck.begin();
        toCheck.erase(toCheck.begin());

        // discard if already seen, else add it in seen
        const auto keysStr = getKeysStr(currState.keys);
        if (seen.find(keysStr) == seen.end()) {
            seen.insert({ keysStr, {}});
        }
        if (seen.at(keysStr).find(currState.pos) == seen.at(keysStr).end()) {
            seen.at(keysStr).insert({currState.pos, currState.dist});
        } else {
            if (seen.at(keysStr).at(currState.pos) <= currState.dist) {
                // no need to process this path, a better one was already processed
                continue;
            }
            seen.at(keysStr).at(currState.pos) = currState.dist;
        }

        // found the shortest path with all keys
        if (currState.keys.size() == targetKeys) {
            return currState.dist;
        }

        for (const auto &neighbor : graph.at(currState.pos)) {
            set<char> nextKeys = currState.keys;
            if (world.hasKey(neighbor.first)) {
                nextKeys.insert(world.getKey(neighbor.first));
            }
            if (goBackHome && neighbor.first == startCoord && nextKeys.size() == world.getKeysCount()) {
                // got all keys and came back to the original point, receive the final key
                nextKeys.insert('X');
            }
            State nextState(neighbor.first, nextKeys, currState.dist + neighbor.second);
            const auto nextKeysStr = getKeysStr(nextKeys);
            if (seen.find(nextKeysStr) != seen.end()
                && seen.at(nextKeysStr).find(neighbor.first) != seen.at(nextKeysStr).end()
                && seen.at(nextKeysStr).at(neighbor.first) <= nextState.dist) {
                    // a better path was already seen
                    continue;
                }
            toCheck.insert(nextState);
        }
    }
    throw AdventException("No route found to gather all keys");
}

map<Coordinates, char> Part1::parse(const string &fileName) {
    map<Coordinates, char> worldMap;
    auto lines = getFileLines(fileName);
    for (size_t y=0; y < lines.size(); ++y) {
        for (size_t x=0; x < lines[y].size(); ++x) {
            Coordinates coord(x, y);
            worldMap[coord] = lines[y][x];
        }
    }
    return worldMap;
}

int Part1::solve(const map<Coordinates, char> &worldMap) {
    World world(worldMap);
    return findSmallestRoute(world, false);
}
