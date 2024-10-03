#pragma once
#include "../Common/Utils.h"


namespace Day07 {

    struct Directory {
        Directory(const std::string& name): name(name) {};
        std::string name;
        std::map<std::string, int> files;
        std::map<std::string, std::shared_ptr<Directory>> folders;
        std::weak_ptr<Directory> parent {};  // weak pointer to avoid cycle dependency leading to memory leak
        int size { 0 };
    };

    std::shared_ptr<Directory> parse(const std::string& filename);

    namespace Part1 {
        int solve(const std::shared_ptr<Directory>& directory);
    }
}
