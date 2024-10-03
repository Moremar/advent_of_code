#include "part1.hpp"
#include "part2.hpp"

using namespace std;

/*
 * Solving this problem by optimization takes forever.
 * Instead we can solve it very easily by understanding the nodes configuration :
 * 
 *  0    0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . B @ 
 *  1    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
 *  2    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
 *  3    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
 *                   [ ... ]    
 *  20   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
 *  21   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
 *  22   . A # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
 *  23   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
 *  24   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
 *  25   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
 *  26   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
 *  27   . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
 *  28   . . . . . . . . _ . . . . . . . . . . . . . . . . . . . . . . . . . .
 * 
 *   The empty node is in (8, 28).
 *   All nodes from (2, 22) to (34, 22) have a "used" bigger than the size of the empty node.
 *   To bring the data from the target (34, 0) to the start node (0, 0), we must :
 *     - bring the empty node to A in Manhattan(empty node, A) swaps
 *     - then bring the empty node to B in Manhattan(A, B) swaps
 *     - move the target data from the target node to B in 1 swap
 *     - bring the target data from B to the start node.
 *       for the target data to move by 1 step left, it requires to move the empty node from
 *       the right of the target data to the left of the target data, which takes 5 steps.
 *       So the total move requires 5 * Manhattan(B, start node) swaps
 */

const Coordinates startNode(0, 0);
const Coordinates emptyNode(8, 28);
const Coordinates targetNode(34, 0);
const Coordinates nodeA(1, 22);
const Coordinates nodeB(33, 0);

void printNodes(const map<Coordinates, Node> &nodesMap) {
    cout << endl;
    for (int y = 0; y <= 28; ++y) {
        for (int x = 0; x <= 34; ++x) {
            char symbol = '.';
            if (Coordinates(x, y) == startNode) symbol = '0';
            if (Coordinates(x, y) == emptyNode) symbol = '_';
            if (Coordinates(x, y) == targetNode) symbol = '@';
            if (Coordinates(x, y) == nodeA) symbol = 'A';
            if (Coordinates(x, y) == nodeB) symbol = 'B';
            if (nodesMap.at(Coordinates(x, y)).used > nodesMap.at(emptyNode).size) symbol = '#';
            cout << symbol << " ";
        }
        cout << endl;
    }
}

int Part2::solve(const vector<Node> &nodes) {
    map<Coordinates, Node> nodesMap;
    for (const auto &node : nodes) {
        nodesMap.insert({ node.coords, node });
    }
    // printNodes(nodesMap);

    return manhattan(emptyNode, nodeA)        // bring the empty node to A
          + manhattan(nodeA, nodeB)           // bring the empty node to B
          + 1                                 // move the target data to B
          + 5 * manhattan(nodeB, startNode);  // move the target data from B to the start node
}
