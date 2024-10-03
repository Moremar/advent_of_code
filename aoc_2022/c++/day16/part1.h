#pragma once
#include "../Common/Utils.h"


namespace Day16 {

    struct Valve {
        Valve(const string& name, const int rate) : name(name), rate(rate) {}
        Valve() = default;
        std::string name;
        int rate;
        std::map<std::string, int> tunnels {};
    };

    std::map<std::string, Valve> parse(const std::string& filename);


    namespace Part1 {

        int solve(const std::map<std::string, Valve>& valves);

    }
}
