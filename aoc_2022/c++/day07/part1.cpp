#include "part1.h"

using namespace std;


namespace Day07 {

    void compute_size(shared_ptr<Directory> directory) {
        if (directory->size == 0) {
            for (const auto& [name, size] : directory->files) {
                directory->size += size;
            }
            for (auto& [name, folder] : directory->folders) {
                compute_size(folder);
                directory->size += folder->size;
            }
        }
    }

    shared_ptr<Directory> parse(const string& filename) {
        const auto lines = getFileLines(filename);
        const shared_ptr<Directory> directory = make_shared<Directory>("/");
        shared_ptr<Directory> curr_dir { directory };

        int curr_line = 1;
        while (curr_line < lines.size()) {
            auto tokens = split(lines[curr_line], " ");
            if (tokens[1] == "cd") {
                curr_dir = tokens[2] == ".." ? curr_dir->parent.lock() : curr_dir->folders.at(tokens[2]);
                ++curr_line;
                continue;
            } 

            // ls
            ++curr_line;
            while (curr_line < lines.size() && *lines[curr_line].begin() != '$') {
                tokens = split(lines[curr_line], " ");
                if (tokens[0] == "dir" && curr_dir->folders.find(tokens[1]) == curr_dir->folders.end()) {
                    curr_dir->folders.insert({ tokens[1], make_shared<Directory>(tokens[1]) });
                    curr_dir->folders.at(tokens[1])->parent = curr_dir;
                } else if (curr_dir->files.find(tokens[1]) == curr_dir->files.end()) {
                    curr_dir->files.insert({ tokens[1], stoi(tokens[0]) });
                }
                ++curr_line;
            }
        }

        compute_size(directory);

        return directory;
    }


    namespace Part1 {

        void calculate(const shared_ptr<Directory>& directory, int& result) {
            if (directory->size <= 100'000) {
                result += directory->size;
            }
            for (const auto& [_, folder] : directory->folders) {
                calculate(folder, result);
            }
        }

        int solve(const shared_ptr<Directory>& directory) {
            int result = 0;
            calculate(directory, result);
            return result;
        }
    }
}
