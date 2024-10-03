#include "part2.h"

using namespace std;

namespace Day21 {
    namespace Part2 {

        void updateMonkey(
                const std::shared_ptr<Monkey<complex<long double>>>& monkey,
                const string& name,
                const complex<long double> val) {
            if (monkey != nullptr) {
                if (monkey->name == name) {
                    monkey->val = val;
                }
                updateMonkey(monkey->left, name, val);
                updateMonkey(monkey->right, name, val);
            }
        }

        long long solve(const std::shared_ptr<Monkey<complex<long double>>>& rootMonkey) {
            updateMonkey(rootMonkey, "humn", complex<long double>{ 0, 1 });
            const auto left  = rootMonkey->left->getVal();
            const auto right = rootMonkey->right->getVal();
            // the value shouted by the "humn" monkey is on the left side
            return static_cast<long long>(round((right.real() - left.real()) / left.imag()));
        }
    }
}
