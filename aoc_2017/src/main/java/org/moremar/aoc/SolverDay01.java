package org.moremar.aoc;

import java.util.List;
import java.util.stream.IntStream;

public class SolverDay01 implements ISolverEngine {

    public SolverDay01() {
        super();
    }

    @Override
    public String solvePart1(List<String> lines) {
        int[] parsed = parseInput(lines);
        int sum = IntStream.range(0, parsed.length)
                 .filter(i -> parsed[i] == parsed[(i+1) % parsed.length])
                 .map(i -> parsed[i])
                 .reduce(0, Integer::sum);
        return String.valueOf(sum);
    }

    @Override
    public String solvePart2(List<String> lines) {
        int[] parsed = parseInput(lines);
        int sum = IntStream.range(0, parsed.length)
                 .filter(i -> parsed[i] == parsed[(i + parsed.length/2) % parsed.length])
                 .map(i -> parsed[i])
                 .reduce(0, Integer::sum);
        return String.valueOf(sum);
    }

    /**
     * Parse the input lines
     */
    private int[] parseInput(List<String> lines) {
        return  lines.getFirst().trim().chars().map(Character::getNumericValue).toArray();
    }
}
