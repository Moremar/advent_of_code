package org.moremar.aoc;

import java.util.*;

public class SolverDay03 implements ISolverEngine {

    private record Position(int x, int y, int id) {}
    private record Coord(int x, int y) {}

    private static final Coord UP = new Coord(0, 1);
    private static final Coord DOWN = new Coord(0, -1);
    private static final Coord LEFT = new Coord(-1, 0);
    private static final Coord RIGHT = new Coord(1, 0);

    public SolverDay03() {
        super();
    }

    @Override
    public String solvePart1(List<String> lines) throws AocException {
        Position target = new Position(-1, -1, parseInput(lines));
        if (target.id < 9) {
            throw new AocException("The target square ID must be 10 or more.");
        }

        // move the curr position to the last square of the target's loop
        Position bottomRight = new Position(1, -1, 9);
        int loop = 1;
        int loopSize = 8;
        do {
            loop += 1;
            loopSize += 8;
            bottomRight = new Position(bottomRight.x + 1, bottomRight.y - 1, bottomRight.id + loopSize);
        } while (bottomRight.id < target.id);

        // the target square is in the last loop we processed, find it
        Position bottomLeft = new Position(bottomRight.x - 2 * loop, bottomRight.y, bottomRight.id - 2 * loop);
        Position topLeft = new Position(bottomLeft.x, bottomLeft.y + 2 * loop, bottomLeft.id - 2 * loop);
        Position topRight = new Position(topLeft.x + 2 * loop, topLeft.y, topLeft.id - 2 * loop);
        if (target.id >= bottomLeft.id) {
            // the target is in the bottom part of the loop
            target = new Position(bottomRight.x - (bottomRight.id - target.id), bottomRight.y, target.id);
        } else if (target.id >= topLeft.id) {
            // the target is in the left part of the loop
            target = new Position(bottomLeft.x, bottomLeft.y + (bottomLeft.id - target.id), target.id);
        } else if (target.id >= topRight.id) {
            // the target is in the top part of the loop
            target = new Position(topLeft.x + (topLeft.id - target.id), topLeft.y, target.id);
        } else {
            // the target is in the right part of the loop
            target = new Position(topRight.x, topRight.y - (topRight.id - target.id), target.id);
        }
        return String.valueOf(Math.abs(target.x) + Math.abs(target.y));
    }

    @Override
    public String solvePart2(List<String> lines) {

        // store all values of previously visited squares
        Map<Coord, Integer> world = new HashMap<>();
        world.put(new Coord(0, 0), 1);
        world.put(new Coord(1, 0), 1);

        int target = parseInput(lines);
        Coord curr = new Coord(1, 0);
        int value;
        Coord direction = UP;

        // calculate the value of each square in order until we find one bigger than the target
        do {
            curr = new Coord(curr.x + direction.x, curr.y + direction.y);
            // turn if we reached a corner of the current loop
            if (direction.equals(UP) && !world.containsKey(sum(curr, LEFT))) {
                direction = LEFT;
            } else if (direction.equals(LEFT) && !world.containsKey(sum(curr, DOWN))) {
                direction = DOWN;
            } else if (direction.equals(DOWN) && !world.containsKey(sum(curr, RIGHT))) {
                direction = RIGHT;
            } else if (direction.equals(RIGHT) && !world.containsKey(sum(curr, UP))) {
                direction = UP;
            }
            value = adjacent(curr).stream()
                                  .filter(world::containsKey)
                                  .mapToInt(world::get)
                                  .sum();
            world.put(curr, value);
        } while (value < target);

        return String.valueOf(value);
    }

    /**
     * Sum 2 pairs of coordinates
     */
    private Coord sum(Coord a, Coord b) {
        return new Coord(a.x + b.x, a.y + b.y);
    }

    /**
     * List adjacent coordinates (including diagonals)
     */
    private List<Coord> adjacent(Coord coord) {
        return Arrays.asList(
                sum(coord, UP),
                sum(coord, DOWN),
                sum(coord, LEFT),
                sum(coord, RIGHT),
                sum(coord, sum(LEFT, DOWN)),
                sum(coord, sum(RIGHT, DOWN)),
                sum(coord, sum(LEFT, UP)),
                sum(coord, sum(RIGHT, UP))
        );
    }

    /**
     * Parse the input lines
     */
    private int parseInput(List<String> lines) {
        return Integer.parseInt(lines.getFirst());
    }
}
