#include "part1.h"

using namespace std;


namespace Day15 {

    vector<Sensor> parse(const string& filename) {
        vector<Sensor> sensors;
        const regex pattern { "Sensor at x=(-?\\d+), y=(-?\\d+): closest beacon is at x=(-?\\d+), y=(-?\\d+)" };
        for (const auto line : getFileLines(filename)) {
            smatch match;
            regex_search(line.begin(), line.end(), match, pattern);
            Coord position { stoi(match[1]), stoi(match[2]) };
            Coord beacon   { stoi(match[3]), stoi(match[4]) };
            sensors.emplace_back(position, beacon);
        }
        return sensors;
    }

    namespace Part1 {

        vector<pair<int, int>> mergeIntervals(const vector<pair<int, int>>& intervals) {
            if (intervals.size() < 2) {
                return intervals;
            }
            vector<pair<int, int>> merged {};
            pair<int, int> currInterval = intervals[0];
            for (int i = 1; i < intervals.size(); ++i) {
                if (intervals[i].first <= currInterval.second) {
                    // intervals can be merged
                    currInterval.second = max(currInterval.second, intervals[i].second);
                } else {
                    // interval starts after the end of the previous one, create a new interval
                    merged.push_back(currInterval);
                    currInterval = intervals[i];
                }
            }
            merged.push_back(currInterval);
            return merged;
        }

        vector<pair<int, int>> findCoverageForY(const vector<Sensor>& sensors, const int targetY, const int maxBound) {
            vector<pair<int, int>> intervals {};
            for (const auto& sensor : sensors) {
                const int range = Coord::manhattan(sensor.pos, sensor.beacon);
                const int distanceToTargetY = abs(sensor.pos.y - targetY);
                if (range < distanceToTargetY) {
                    continue;
                } else {
                    int left  = sensor.pos.x - (range - distanceToTargetY);
                    int right = sensor.pos.x + (range - distanceToTargetY);
                    if (maxBound != -1) {
                        left  = max(left,  0);
                        right = min(right, maxBound);
                    }
                    intervals.emplace_back(left, right);
                }
            }
            sort(intervals.begin(), intervals.end());
            return mergeIntervals(intervals);
        }

        int solve(const vector<Sensor>& sensors, const int targetY) {
            // get the X of all cells covered by the sensors for that Y
            const auto intervals = findCoverageForY(sensors, targetY);

            // count the number of cells covered by the sensors on that Y
            int coveredCoords = 0;
            for_each (intervals.begin(), intervals.end(), [&](const auto& interval) {
                coveredCoords += interval.second - interval.first + 1;
            });

            // subtract from the covered area the known beacons
            set<int> processedBeaconsX {};
            for (const auto& sensor : sensors) {
                if (sensor.beacon.y != targetY) {
                    // beacon with a different value of Y
                    continue;
                }
                if (processedBeaconsX.find(sensor.beacon.x) != processedBeaconsX.end()) {
                    //beacon already subtracted for a previous sensor
                    continue;
                }
                processedBeaconsX.insert(sensor.beacon.x);
                if (any_of(intervals.begin(),
                           intervals.end(),
                           [&](const auto& interval) { return sensor.beacon.x >= interval.first && sensor.beacon.x <= interval.second; })) {
                    --coveredCoords;
                }
            }

            return coveredCoords;
        }

    }
}
