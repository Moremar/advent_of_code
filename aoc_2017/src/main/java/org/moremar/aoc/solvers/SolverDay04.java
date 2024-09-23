package org.moremar.aoc.solvers;

import org.moremar.aoc.common.AocException;
import java.util.Arrays;
import java.util.List;

public class SolverDay04 implements ISolverEngine {

    public SolverDay04() {
        super();
    }

    @Override
    public String solvePart1(List<String> lines) throws AocException {
        long valid = parseInput(lines)
                         .stream()
                         .filter(SolverDay04::hasDuplicates)
                         .count();
        return String.valueOf(valid);
    }

    @Override
    public String solvePart2(List<String> lines) {
        long valid = parseInput(lines)
                         .stream()
                         .filter(SolverDay04::hasAnagrams)
                         .count();
        return String.valueOf(valid);
    }

    private static boolean hasDuplicates(String[] tokens) {
        return tokens.length == Arrays.stream(tokens).distinct().count();
    }

    private static boolean hasAnagrams(String[] tokens) {
        String[] sortedTokens = Arrays.stream(tokens)
                                      .map(token -> {
                                          var chars = token.toCharArray();
                                          Arrays.sort(chars);
                                          return new String(chars);
                                      })
                                      .toList()
                                      .toArray(new String[0]);
        return hasDuplicates(sortedTokens);
    }

    /**
     * Parse the input lines
     */
    private List<String[]> parseInput(List<String> lines) {
        return lines.stream()
                    .map(s -> s.split(" "))
                    .toList();
    }
}
