#include "part2.h"

using namespace std;

const long long DECRYPTION_KEY = 811'589'153LL;

namespace Day20 {
    namespace Part2 {

        long long solve(const shared_ptr<Node>& firstNode) {
            const int maxNodeId = firstNode->prev.lock()->nodeId;
            // multiply all values by the decryption key
            auto curr = firstNode;
            for (int i = 0; i <= maxNodeId; ++i) {
                curr->val *= DECRYPTION_KEY;
                curr = curr->next;
            }
            // mix the nodes 10 times
            for (int i = 0; i < 10; ++i) {
                Part1::mix(firstNode, maxNodeId);
            }
            return Part1::groveCoordinate(firstNode);
        }

    }
}
