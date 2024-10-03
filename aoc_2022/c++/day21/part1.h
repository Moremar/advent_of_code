#pragma once
#include "../Common/Utils.h"


namespace Day21 {

    /**
     * Templated struct for Monkeys so we can use it for part 1 (with "long long" values)
     * and for part 2 (with complex values)
     */
    template <class T>
    struct Monkey {
        Monkey(const std::string& name) : name(name) {}

        std::string name;
        std::optional<T> val {};
        std::string op {};
        std::shared_ptr<Monkey> left { nullptr };
        std::shared_ptr<Monkey> right { nullptr };

        T getVal() {
            if (!val.has_value()) {
                const T leftVal = left->getVal();
                const T rightVal = right->getVal();
                if (op == "+") val = leftVal + rightVal;
                else if (op == "-") val = leftVal - rightVal;
                else if (op == "*") val = leftVal * rightVal;
                else val = static_cast<T>(leftVal / rightVal);
            }
            return val.value();
        }
    };


    template <class T>
    std::shared_ptr<Monkey<T>> parse(const std::string& filename) {
        std::map<std::string, std::shared_ptr<Monkey<T>>> monkeys;
        for (const auto line : getFileLines(filename)) {
            const auto tokens = split(line, " ");
            const auto name   = tokens[0].substr(0, tokens[0].size()-1);
            if (monkeys.find(name) == monkeys.end()) {
                monkeys.insert({ name, std::make_shared<Monkey<T>>(name) });
            }
            if (tokens.size() == 2) {
                // number yelling monkey
                monkeys.at(name)->val = static_cast<T>(stoi(tokens[1]));
            } else {
                const auto leftName  = tokens[1];
                const auto op        = tokens[2];
                const auto rightName = tokens[3];
                if (monkeys.find(leftName) == monkeys.end()) {
                    monkeys.insert({ leftName, std::make_shared<Monkey<T>>(leftName) });
                }
                if (monkeys.find(rightName) == monkeys.end()) {
                    monkeys.insert({ rightName, std::make_shared<Monkey<T>>(rightName) });
                }
                monkeys.at(name)->left  = monkeys.at(leftName);
                monkeys.at(name)->op    = op;
                monkeys.at(name)->right = monkeys.at(rightName);
            }
        }
        return monkeys.at("root");
    }


    namespace Part1 {

        long long solve(const std::shared_ptr<Monkey<long long>>& rootMonkey);

    }
}
