package org.moremar.aoc.solvers;

import org.moremar.aoc.common.AocException;
import java.util.List;

public class SolverDay05 implements ISolverEngine {

    public SolverDay05() {
        super();
    }

    @Override
    public String solvePart1(List<String> lines) throws AocException {
        final int[] trampolines = parseInput(lines);
        int position = 0;
        int steps = 0;
        while (position >= 0 && position < trampolines.length) {
            ++steps;
            int prevPosition = position;
            position += trampolines[position];
            ++trampolines[prevPosition];  // increment the trampoline after the jump
        }
        return String.valueOf(steps);
    }

    @Override
    public String solvePart2(List<String> lines) {
        final int[] trampolines = parseInput(lines);
        int position = 0;
        int steps = 0;
        while (position >= 0 && position < trampolines.length) {
            ++steps;
            int prevPosition = position;
            position += trampolines[position];
            if (trampolines[prevPosition] >= 3) {
                --trampolines[prevPosition];  // decrement the trampoline after the jump if its offset is 3 or more
            } else {
                ++trampolines[prevPosition];  // otherwise increment it
            }
        }
        return String.valueOf(steps);
    }

    /**
     * Parse the input lines
     */
    private int[] parseInput(List<String> lines) {
        return lines.stream()
                    .mapToInt(Integer::parseInt)
                    .toArray();
    }
}
