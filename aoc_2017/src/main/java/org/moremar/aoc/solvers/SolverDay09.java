package org.moremar.aoc.solvers;

import java.util.List;

public class SolverDay09 implements ISolverEngine {

    public SolverDay09() {
        super();
    }

    @Override
    public String solvePart1(List<String> lines) {
        final String chars = parseInput(lines);
        int pos = 0, depth = 0, score = 0;
        boolean garbage = false;
        while (pos < chars.length()) {
            switch (chars.charAt(pos)) {
                case '{': if (!garbage) { ++depth; score += depth; }
                          break;
                case '}': if (!garbage) --depth;
                          break;
                case '!': ++pos; // only appears within garbage, skip the next char
                          break;
                case '<': garbage = true;
                          break;
                case '>': garbage = false;
                          break;
                default:  // ignore
            }
            ++pos;
        }
        return String.valueOf(score);
    }

    @Override
    public String solvePart2(List<String> lines) {
        final String chars = parseInput(lines);
        int pos = 0, garbageCount = 0;
        boolean garbage = false;
        while (pos < chars.length()) {
            switch (chars.charAt(pos)) {
                case '!': ++pos; // only appears within garbage, skip the next char
                          break;
                case '<': if (garbage) { ++garbageCount; } else { garbage = true; }
                          break;
                case '>': garbage = false;
                          break;
                default:  if (garbage) ++garbageCount;
            }
            ++pos;
        }
        return String.valueOf(garbageCount);
    }

    /**
     * Parse the input lines
     */
    private String parseInput(List<String> lines) {
        return lines.getFirst();
    }
}
