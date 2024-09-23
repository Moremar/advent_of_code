package org.moremar.aoc.solvers;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.IntStream;

public class SolverDay02 implements ISolverEngine {

    public SolverDay02() {
        super();
    }

    @Override
    public String solvePart1(List<String> lines) {
        List<List<Integer>> parsed = parseInput(lines);
        List<Integer> maxList = parsed.stream().map(Collections::max).toList();
        List<Integer> minList = parsed.stream().map(Collections::min).toList();
        int sum = IntStream.range(0, maxList.size())
                           .map(i -> maxList.get(i) - minList.get(i))
                           .sum();
        return String.valueOf(sum);
    }

    @Override
    public String solvePart2(List<String> lines) {
        List<List<Integer>> parsed = parseInput(lines);
        int sum = parsed.stream().mapToInt(this::getDivisionResult).sum();
        return String.valueOf(sum);
    }

    private int getDivisionResult(List<Integer> values) {
        for (int i = 0; i < values.size(); ++i) {
            for (int j = 0; j < values.size(); ++j) {
                if (i == j) {
                    continue;
                }
                if (values.get(i) < values.get(j)) {
                    continue;
                }
                if (values.get(i) % values.get(j) != 0) {
                    continue;
                }
                return values.get(i) / values.get(j);
            }
        }
        return -1;
    }

    /**
     * Parse the input lines
     */
    private List<List<Integer>> parseInput(List<String> lines) {
        return lines.stream()
             .map(s -> Arrays.asList(s.split("[ \t]+")))
             .map(tokens -> tokens.stream().map(Integer::valueOf).toList())
             .toList();
    }
}
