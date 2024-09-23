package org.moremar.aoc.solvers;

import org.moremar.aoc.common.AocException;
import org.moremar.aoc.common.Coord;
import java.util.*;

public class SolverDay03 implements ISolverEngine {

    private record Position(int x, int y, int id) {}

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
        Coord direction = Coord.UP;

        // calculate the value of each square in order until we find one bigger than the target
        do {
            curr = new Coord(curr.x() + direction.x(), curr.y() + direction.y());
            // turn if we reached a corner of the current loop
            if (direction.equals(Coord.UP) && !world.containsKey(curr.add(Coord.LEFT))) {
                direction = Coord.LEFT;
            } else if (direction.equals(Coord.LEFT) && !world.containsKey(curr.add(Coord.DOWN))) {
                direction = Coord.DOWN;
            } else if (direction.equals(Coord.DOWN) && !world.containsKey(curr.add(Coord.RIGHT))) {
                direction = Coord.RIGHT;
            } else if (direction.equals(Coord.RIGHT) && !world.containsKey(curr.add(Coord.UP))) {
                direction = Coord.UP;
            }
            value = curr.adjacent8().stream()
                                    .filter(world::containsKey)
                                    .mapToInt(world::get)
                                    .sum();
            world.put(curr, value);
        } while (value < target);

        return String.valueOf(value);
    }

    /**
     * Parse the input lines
     */
    private int parseInput(List<String> lines) {
        return Integer.parseInt(lines.getFirst());
    }
}
