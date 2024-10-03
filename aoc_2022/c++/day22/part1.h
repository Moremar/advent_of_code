#pragma once
#include "../Common/Utils.h"


namespace Day22 {

    struct Instruction {
        int  distance;
        char turn;
    };

    using World = std::map<Coord, char>;

    /**
     * Interface specifying how to wrap around when we go past a border of the world
     */
    class IWrapper {
    public:
        virtual std::pair<Coord, int> wrap(const World& world, const Coord& pos, const int facing) const = 0;
    };

    std::tuple<Coord, World, std::vector<Instruction>> parse(const std::string& filename);

    namespace Part1 {

        // Wrapper for part 1
        class Wrapper : public IWrapper {
        public:
            std::pair<Coord, int> wrap(const World& world, const Coord& pos, const int facing) const override;
        };

        int getFinalPassword(
                const Coord& start,
                const World& world,
                const std::vector<Instruction>& instructions,
                const IWrapper& wrapper);

        int solve(const std::tuple<Coord, World, std::vector<Instruction>>& input);

    }
}
