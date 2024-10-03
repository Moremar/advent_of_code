#include "part2.h"

using namespace std;


namespace Day07 {
    namespace Part2 {

        void findDirectorySizeToRemove(const shared_ptr<Directory>& directory, int target, int& result) {
            if (directory->size < target) {
                return;
            }
            if (directory->size < result) {
                result = directory->size;
            }
            for (const auto& [_, folder] : directory->folders) {
                findDirectorySizeToRemove(folder, target, result);
            }
        }

        int solve(const shared_ptr<Directory>& directory) {
            const int available = 70'000'000 - directory->size;
            const int target = 30'000'000 - available;

            int result = directory->size;
            findDirectorySizeToRemove(directory, target, result);
            return result;
        }
    }
}
