"""Solution for AOC 2024 day 16"""

from collections import deque

UP, RIGHT, DOWN, LEFT = (-1, 0), (0, 1), (1, 0), (0, -1)
DIRECTIONS = [UP, RIGHT, DOWN, LEFT]


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        walls = set()
        start, target = None, None
        for (i, line) in enumerate(file.readlines()):
            for (j, c) in enumerate(line.strip()):
                if c == 'S':
                    start = (i, j)
                elif c == 'E':
                    target = (i, j)
                elif c == '#':
                    walls.add((i, j))
        return start, target, walls


def traverse(start, target, walls):
    """Find the best paths through the maze"""
    forward_queue = deque([(start, RIGHT, 0, {start})])
    turn_queue = deque()
    seen = {}
    best_score = -1
    best_path_sets = set()
    while True:
        # turning is very expensive, so we first try all moves forward
        if len(forward_queue) > 0:
            pos, direction, score, path = forward_queue.popleft()
            if (pos, direction) in seen and score > seen[(pos, direction)]:
                continue
            seen[(pos, direction)] = score
            if pos == target:
                if score < best_score:
                    best_path_sets = set()
                best_path_sets = best_path_sets.union(path)
                best_score = score if best_score == -1 else min(score, best_score)
                continue
            # go forward if possible
            front = (pos[0] + direction[0], pos[1] + direction[1])
            if front not in walls:
                forward_queue.append((front, direction, score + 1, path.union({front})))
            # turn left if possible
            left_dir = DIRECTIONS[(DIRECTIONS.index(direction) - 1) % 4]
            left_pos = (pos[0] + left_dir[0], pos[1] + left_dir[1])
            if left_pos not in walls:
                turn_queue.append((pos, left_dir, score + 1000, path))
            # turn right if possible
            right_dir = DIRECTIONS[(DIRECTIONS.index(direction) + 1) % 4]
            right_pos = (pos[0] + right_dir[0], pos[1] + right_dir[1])
            if right_pos not in walls:
                turn_queue.append((pos, right_dir, score + 1000, path))
        else:
            # when we can no longer move forward, try to turn
            if best_score != -1:
                return best_score, len(best_path_sets)
            forward_queue = turn_queue
            turn_queue = deque()


def solve1(data):
    """Solve part 1"""
    return traverse(*data)[0]


def solve2(data):
    """Solve part 2"""
    return traverse(*data)[1]


if __name__ == '__main__':
    parsed = parse('data.txt')
    print('Day 16:', solve1(parsed), solve2(parsed))
