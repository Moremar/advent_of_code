#!/usr/bin/env python3
import time


class Folder:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.files = []
        self.folders = []
        self.size = None


def parse(input_path):
    with open(input_path, 'r') as f:
        return [[row.split(' ') for row in command.strip().split('\n')] for command in f.read().split('$')[1:]]


def compute_folder_sizes(folder):
    if folder.size is None:
        folder.size = sum([f[0] for f in folder.files]) + sum([compute_folder_sizes(f) for f in folder.folders])
    return folder.size


def build_tree(commands):
    root = Folder('/')
    curr = root
    for command in commands:
        if command[0][0] == 'ls':
            if len(curr.folders) == 0 and len(curr.files) == 0:
                for result in command[1:]:
                    if result[0] == 'dir':
                        curr.folders.append(Folder(result[1], curr))
                    else:
                        curr.files.append((int(result[0]), result[1]))
        elif command[0][0] == 'cd':
            if command[0][1] == '/':
                curr = root
            elif command[0][1] == '..':
                curr = curr.parent
            else:
                for folder in curr.folders:
                    if folder.name == command[0][1]:
                        curr = folder
                        break
    compute_folder_sizes(root)
    return root


def get_sum(folder):
    return (folder.size if folder.size <= 100000 else 0) + sum([get_sum(f) for f in folder.folders])


def solve_part1(commands):
    return get_sum(build_tree(commands))


if __name__ == "__main__":
    start = time.time()
    parsed = parse("data.txt")
    result = solve_part1(parsed)
    print(f'Part 1 : {result}  ({round(1000 * (time.time() - start))} ms)')
