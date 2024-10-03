#include "part1.h"

using namespace std;

namespace Day20 {

    shared_ptr<Node> parse(const string& filename) {
        shared_ptr<Node> firstNode { nullptr };
        shared_ptr<Node> currNode  { nullptr };
        int nodeId { 0 };
        for (const auto line : getFileLines(filename)) {
            auto node = make_shared<Node>();
            node->val = stoll(line);
            node->nodeId = nodeId++;
            if (firstNode == nullptr) {
                firstNode = node;
                currNode = node;
            } else {
                node->prev = currNode;
                currNode->next = node;
                currNode = node;
            }
        }
        currNode->next = firstNode;
        firstNode->prev = currNode;
        return firstNode;
    }


    namespace Part1 {

        void mix(const shared_ptr<Node>& firstNode, const int maxNodeId) {
            auto curr = firstNode;
            for (int nodeId = 0; nodeId <= maxNodeId; ++nodeId) {
                // set the cursor to the node to move
                while (curr->nodeId != nodeId) {
                    curr = curr->next;
                }
                // get the number of elements to move the node forward
                const int shift = (curr->val % maxNodeId) + (curr-> val < 0 ? maxNodeId : 0);
                if (shift == 0) {
                    continue;
                }
                // find the node right before where this node should move
                auto target = curr;
                for (int i = 0; i < shift; ++i) {
                    target = target->next;
                }
                // insert the node to its target position
                curr->prev.lock()->next = curr->next;
                curr->next->prev = curr->prev;
                target->next->prev = curr;
                curr->next = target->next;
                target->next = curr;
                curr->prev = target;
            }
        }


        long long groveCoordinate(const shared_ptr<Node>& firstNode) {
            auto curr = firstNode;
            // move the current pointer to the node with value zero
            while (curr->val != 0LL) {
                curr = curr->next;
            }
            // calculate the sum of the 1000th, 2000th and 3000th elements
            long long result = 0;
            for (int i = 0; i < 3; ++i) {
                for (int k = 0; k < 1000; ++k) {
                    curr = curr->next;
                }
                result += curr->val;
            }
            return result;
        }


        long long solve(const shared_ptr<Node>& firstNode) {
            const int maxNodeId = firstNode->prev.lock()->nodeId;
            mix(firstNode, maxNodeId);
            return groveCoordinate(firstNode);
        }

    }
}
