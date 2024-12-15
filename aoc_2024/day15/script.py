"""Solution for AOC 2024 day 15"""

from collections import deque

UP, RIGHT, DOWN, LEFT = (-1, 0), (0, 1), (1, 0), (0, -1)
DIRECTIONS = {'^': UP, '>': RIGHT, 'v': DOWN, '<': LEFT}


def parse(file_name):
    """Parse the input file"""
    with open(file_name, 'r', encoding='utf-8') as file:
        world_str, moves_str = file.read().split('\n\n')
        start, walls, boxes = None, set(), set()
        for (i, line) in enumerate(world_str.split('\n')):
            for (j, c) in enumerate(line.strip()):
                if c == '@':
                    start = (i, j)
                elif c == '#':
                    walls.add((i, j))
                elif c == 'O':
                    boxes.add((i, j))
        moves = [DIRECTIONS[c] for c in moves_str.replace('\n', '')]
        return start, walls, boxes, moves


def expand_map(start, walls, boxes, moves):
    """Generate the map of part 2 from the parsed map of part 1"""
    expanded_walls, expanded_boxes = set(), set()
    for (i, j) in walls:
        expanded_walls.add((i, 2 * j))
        expanded_walls.add((i, 2 * j + 1))
    expanded_boxes = set()
    for (i, j) in boxes:
        expanded_boxes.add((i, 2 * j))
    return (start[0], 2 * start[1]), expanded_walls, expanded_boxes, moves


def can_move(position, move, walls, boxes):
    """Return true if the robot can move in a given direction"""
    next_pos = position[0] + move[0], position[1] + move[1]
    if next_pos in boxes:
        return can_move(next_pos, move, walls, boxes)
    return next_pos not in walls


def solve1(parsed):
    """Solve part 1"""
    position, walls, boxes, moves = parsed
    for move in moves:
        if can_move(position, move, walls, boxes):
            position = position[0] + move[0], position[1] + move[1]
            if position in boxes:
                # move the boxes
                new_box_position = position[0] + move[0], position[1] + move[1]
                while new_box_position in boxes:
                    new_box_position = new_box_position[0] + move[0], new_box_position[1] + move[1]
                boxes.remove(position)
                boxes.add(new_box_position)
    return sum(100 * i + j for (i, j) in boxes)


def can_move_double(pos, move, walls, boxes):
    """Return true if a box (2-cells wide) can move in a given direction"""
    if move in [UP, DOWN]:
        return can_move_single(pos, move, walls, boxes) \
            and can_move_single((pos[0], pos[1] + 1), move, walls, boxes)
    if move == LEFT:
        return can_move_single(pos, move, walls, boxes)
    return can_move_single((pos[0], pos[1] + 1), move, walls, boxes)


def can_move_single(pos, move, walls, boxes):
    """Return true if the robot (1-cell wide) can move in a given direction"""
    next_pos = pos[0] + move[0], pos[1] + move[1]
    if next_pos in boxes:
        return can_move_double(next_pos, move, walls, boxes)
    if move in [LEFT, UP, DOWN] and (next_pos[0], next_pos[1] - 1) in boxes:
        return can_move_double((next_pos[0], next_pos[1] - 1), move, walls, boxes)
    return next_pos not in walls


def solve2(parsed):
    """Solve part 2"""
    position, walls, boxes, moves = expand_map(*parsed)
    for move in moves:
        if can_move_single(position, move, walls, boxes):
            position = position[0] + move[0], position[1] + move[1]
            boxes_to_remove, boxes_to_add = set(), set()
            boxes_to_move = deque()
            if position in boxes:
                boxes_to_move.append(position)
            if move in [UP, DOWN, LEFT] and (position[0], position[1] - 1) in boxes:
                boxes_to_move.append((position[0], position[1] - 1))
            while len(boxes_to_move):
                box = boxes_to_move.popleft()
                boxes_to_remove.add(box)
                next_pos = (box[0] + move[0], box[1] + move[1])
                boxes_to_add.add(next_pos)
                if next_pos in boxes:
                    boxes_to_move.append(next_pos)
                if move == RIGHT and (next_pos[0], next_pos[1] + 1) in boxes:
                    boxes_to_move.append((next_pos[0], next_pos[1] + 1))
                if move in [UP, DOWN, LEFT] and (next_pos[0], next_pos[1] - 1) in boxes:
                    boxes_to_move.append((next_pos[0], next_pos[1] - 1))
                if move in [UP, DOWN] and (next_pos[0], next_pos[1] + 1) in boxes:
                    boxes_to_move.append((next_pos[0], next_pos[1] + 1))
            boxes = boxes.difference(boxes_to_remove).union(boxes_to_add)
    return sum(100 * i + j for (i, j) in boxes)


if __name__ == '__main__':
    # we do not share the parsed input between part 1 and part 2 because part 1 modifies it
    print('Day 15:', solve1(parse('data.txt')), solve2(parse('data.txt')))
