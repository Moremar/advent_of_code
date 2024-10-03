#include "part1.hpp"

using namespace std;


Factory::Factory(const FactoryRules &rules)
  : myChips(rules.initialChips), myInstructions(rules.instructions) {};


string Factory::run(int targetLow, int targetHigh) {
    // a bot proceeds only if it has 2 chips, so we keep a list of bots to check
    list<string> toCheck; 
    for (const auto &chips : myChips) {
        if (chips.second.size() == 2) {
            toCheck.push_back(chips.first);
        }
    }
    // check the potential bots with 2 chips one by one
    while (!toCheck.empty()) {
        const string item = toCheck.front();
        toCheck.pop_front();

        // outputs or bots with less than 2 chips are not eligible
        if (item.find("output") != string::npos || myChips.at(item).size() != 2) {
            continue;
        }

        const Instruction &instr = myInstructions.at(item);
        set<int> &chips = myChips.find(item)->second;
        const int lowChip = *chips.begin();
        const int highChip = *chips.rbegin();

        // if both target chips are owned by that bot, return it
        if (lowChip == targetLow && highChip == targetHigh) {
            return item;
        }

        // move the chips to their destination and flag the 2 destinations to be checked
        chips.erase(chips.find(lowChip));
        chips.erase(chips.find(highChip));
        myChips[instr.lowDest].insert(lowChip);
        myChips[instr.highDest].insert(highChip);
        toCheck.push_back(instr.lowDest);
        toCheck.push_back(instr.highDest);
    }
    return "";
}


FactoryRules Part1::parse(const string &filePath) {
    FactoryRules factoryRules;
    regex chip_rgx("value ([0-9]+) goes to ([a-z 0-9]+)");
    regex instr_rgx("([a-z 0-9]+) gives low to ([a-z 0-9]+) and high to ([a-z 0-9]+)");
    for (const string &line : getFileLines(filePath)) {
        smatch match;
        if (line.find("value") != string::npos) {
            // chip initialization line
            regex_search(line.begin(), line.end(), match, chip_rgx);
            const int chipId = stoi(match[1]);
            const string dest = match[2];
            if (factoryRules.initialChips.find(dest) == factoryRules.initialChips.end()) {
                factoryRules.initialChips.insert({ dest, set<int>() });
            }
            factoryRules.initialChips[dest].insert(chipId);
        } else {
            // instruction line
            regex_search(line.begin(), line.end(), match, instr_rgx);
            const string src = match[1];
            const string lowDest = match[2];
            const string highDest = match[3];
            if (factoryRules.initialChips.find(lowDest) == factoryRules.initialChips.end()) {
                factoryRules.initialChips.insert({ lowDest, set<int>() });
            }
            if (factoryRules.initialChips.find(highDest) == factoryRules.initialChips.end()) {
                factoryRules.initialChips.insert({ highDest, set<int>() });
            }
            factoryRules.instructions.insert({ src, Instruction(lowDest, highDest) });
        }
    }
    return factoryRules;
}


string Part1::solve(const FactoryRules &rules) {
    Factory factory(rules);
    return factory.run(17, 61);
}
