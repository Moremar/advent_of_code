#pragma once
#include "../Common/Utils.h"


namespace Day20 {

    struct Node {
        long long val;  // must be "long long" for part 2
        int nodeId;
        std::shared_ptr<Node> next { nullptr };
        std::weak_ptr<Node> prev {};
    };

    std::shared_ptr<Node> parse(const std::string& filename);


    namespace Part1 {

        void mix(const std::shared_ptr<Node>& firstNode, const int maxNodeId);

        long long groveCoordinate(const std::shared_ptr<Node>& firstNode);

        long long solve(const std::shared_ptr<Node>& firstNode);

    }
}
