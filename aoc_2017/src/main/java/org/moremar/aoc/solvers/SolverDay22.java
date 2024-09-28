package org.moremar.aoc.solvers;

import org.moremar.aoc.common.AocException;
import org.moremar.aoc.common.Coord;
import java.util.*;

public class SolverDay22 implements ISolverEngine {

    private static class World {
        public Coord virusPosition;
        public Coord virusDirection = Coord.UP;
        public Set<Coord> infected = new HashSet<>();
        public Set<Coord> flagged = new HashSet<>();
        public Set<Coord> weakened = new HashSet<>();

        public World(Coord virusPosition) {
            this.virusPosition = virusPosition;
        }
    }

    public SolverDay22() {
        super();
    }

    @Override
    public String solvePart1(List<String> lines) throws AocException {
        final World world = parseInput(lines);
        int infected = 0;
        for (int steps = 0; steps < 10000; ++steps) {
            if (nextStep(world)) {
                ++infected;
            }
        }
        return String.valueOf(infected);
    }

    private boolean nextStep(World world) throws AocException {
        boolean infected = false;
        if (world.infected.contains(world.virusPosition)) {
            world.virusDirection = world.virusDirection.turnRight();
            world.infected.remove(world.virusPosition);
        } else {
            world.virusDirection = world.virusDirection.turnLeft();
            world.infected.add(world.virusPosition);
            infected = true;
        }
        world.virusPosition = world.virusPosition.add(world.virusDirection);
        return infected;
    }

    @Override
    public String solvePart2(List<String> lines) throws AocException {
        final World world = parseInput(lines);
        int infected = 0;
        for (int steps = 0; steps < 10000000; ++steps) {
            if (nextStepEvolved(world)) {
                ++infected;
            }
        }
        return String.valueOf(infected);
    }

    private boolean nextStepEvolved(World world) throws AocException {
        boolean infected = false;
        if (world.infected.contains(world.virusPosition)) {
            world.virusDirection = world.virusDirection.turnRight();
            world.infected.remove(world.virusPosition);
            world.flagged.add(world.virusPosition);
        } else if (world.flagged.contains(world.virusPosition)) {
            world.virusDirection = world.virusDirection.turnLeft().turnLeft();
            world.flagged.remove(world.virusPosition);
        } else if (world.weakened.contains(world.virusPosition)) {
            world.weakened.remove(world.virusPosition);
            world.infected.add(world.virusPosition);
            infected = true;
        } else {
            world.virusDirection = world.virusDirection.turnLeft();
            world.weakened.add(world.virusPosition);
        }
        world.virusPosition = world.virusPosition.add(world.virusDirection);
        return infected;
    }

    /**
     * Parse the input lines
     */
    private World parseInput(List<String> lines) throws AocException {
        final Coord origin = new Coord((lines.getFirst().length() - 1) / 2, - (lines.size() - 1) / 2);
        final World world = new World(origin);
        for (int j = 0; j < lines.size(); ++j) {
            for (int i = 0; i < lines.get(j).length(); ++i) {
                if (lines.get(j).charAt(i) == '#') {
                    world.infected.add(new Coord(i, -j));
                }
            }
        }
        return world;
    }
}