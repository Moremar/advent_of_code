#include "part2.h"

using namespace std;

/**
 * With 32 time intervals instead of 24, the computation in part 1 takes too much time.
 * To improve it, we refactor the code to optimize it :
 *  - use a cache that remembers for a given combination of resources, bots and remaining time what is the
 *    max amount of geodes that can be open
 *  - cap the number of resources to the maximum number usable during the remaining time, to hit the cache more often
 */

const int ORE      = 0;
const int CLAY     = 1;
const int OBSIDIAN = 2;
const int GEODE    = 3;


namespace Day19 {
    namespace Part2 {

        using CacheKey = tuple<int, int, int, int, int, int, int, int, int>;  // resources + bots + remaining time

        int calculate(
                const Blueprint&      blueprint,
                array<int, 4>         resources,
                const array<int, 4>&  bots,
                const int             remainingTime,
                const array<int, 3>&  maxBots,
                map<CacheKey, int>&   cache) {

            // cap resources to max usable resources to improve cache usage
            for (int i = 0; i < 3; ++i) {
                resources[i] = min(resources[i], remainingTime * maxBots[i]);
            }

            // return the result from the cache if already calculated
            CacheKey cacheKey { resources[ORE], resources[CLAY], resources[OBSIDIAN], resources[GEODE],
                                bots[ORE], bots[CLAY], bots[OBSIDIAN], bots[GEODE], remainingTime };
            if (cache.find(cacheKey) != cache.end()) {
                return cache.at(cacheKey);
            }

            // score if we stop producing anything for the remaining time
            int currScore = resources[GEODE] + bots[GEODE] * remainingTime;

            // get the score if we build next a bot of each type
            for (int resource = 0; resource < 4; ++resource) {
                // skip that bot type if we already have enough bots of that type
                if (resource != GEODE && bots[resource] >= maxBots[resource]) {
                    continue;
                }
                // skip that bot if we cannot produce it yet
                if ((resource == OBSIDIAN && bots[CLAY] == 0) || (resource == GEODE && bots[OBSIDIAN] == 0)) {
                    continue;
                }
                int timeToGetResources = 0;
                for (int i = 0; i < 3; ++i) {
                    const int missingResources = blueprint[resource][i] - resources[i];
                    int time = 0;
                    if (missingResources > 0) {
                        time = missingResources / bots[i] + (missingResources % bots[i] == 0 ? 0 : 1);
                    }
                    timeToGetResources = max(timeToGetResources, time);
                }
                ++timeToGetResources;  // +1 for the time to build the bot
                if (remainingTime - timeToGetResources > 0) {
                    const int childScore = calculate(
                        blueprint,
                        {
                            resources[ORE] + timeToGetResources * bots[ORE] - blueprint[resource][ORE],
                            resources[CLAY] + timeToGetResources * bots[CLAY] - blueprint[resource][CLAY],
                            resources[OBSIDIAN] + timeToGetResources * bots[OBSIDIAN] - blueprint[resource][OBSIDIAN],
                            resources[GEODE] + timeToGetResources * bots[GEODE],
                        },
                        {
                            bots[ORE] + (resource == ORE ? 1 : 0),
                            bots[CLAY] + (resource == CLAY ? 1 : 0),
                            bots[OBSIDIAN] + (resource == OBSIDIAN ? 1 : 0),
                            bots[GEODE] + (resource == GEODE ? 1 : 0),
                        },
                        remainingTime - timeToGetResources,
                        maxBots,
                        cache
                    );
                    currScore = max(currScore, childScore);
                }
            }
            cache[cacheKey] = currScore;
            return currScore;
        }


        int calculateMaxGeodesWithCache(const Blueprint& blueprint, const int maxTime) {
            map<CacheKey, int> cache {};
            // we can build only 1 bot at a time, so it is useless to have more bots of a resource
            // than the maximum required of that resource for a bot construction
            array<int, 3> maxBots;
            for (int i = 0; i < 3; ++i) {
                for (int j = 0; j < 4; ++j) {
                    maxBots[i] = max(maxBots[i], blueprint[j][i]);
                }
            }
            return calculate(blueprint, { 0, 0, 0, 0 }, { 1, 0, 0, 0 }, maxTime, maxBots, cache);
        }


        int solve(const vector<Blueprint>& blueprints) {
            int result = 1;
            for (int i = 0; i < 3; ++i) {
                 result *= calculateMaxGeodesWithCache(blueprints[i], 32);
            }
            return result;
        }

    }
}
