#include "part1.hpp"
#include "part2.hpp"

using namespace std;


int Part2::solve(int elves) {
    // circular linked list of all players
    map<int, int> circle;
    for (int i = 1; i < elves; ++i) {
        circle.insert({ i, i+1 });
    }
    circle.insert({ elves, 1 });
    int curr = 1;

    // keep a pointer on the elf before the elf facing the current player
    int beforeFacingElf = elves/2;
    bool stepForward = elves % 2 == 1;

    // remove the player facing the current player, and move the pointer right
    // one time out of 2
    while (circle.at(curr) != curr) {
        circle[beforeFacingElf] = circle.at(circle.at(beforeFacingElf));
        if (stepForward){
            beforeFacingElf = circle.at(beforeFacingElf);
        }
        stepForward = !stepForward;

        curr = circle.at(curr);
    }
    return curr;
}
