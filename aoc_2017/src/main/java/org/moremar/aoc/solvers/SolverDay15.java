package org.moremar.aoc.solvers;

import org.moremar.aoc.common.AocException;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class SolverDay15 implements ISolverEngine {

    static final long FACTOR_A = 16807;
    static final long FACTOR_B = 48271;
    static final long DIVIDE_BY = 2147483647;
    static final long KEEP_SIZE = 65536;  // 2^16

    public SolverDay15() {
        super();
    }

    @Override
    public String solvePart1(List<String> lines) throws AocException {
        final List<Long> starts = parseInput(lines);
        long a = starts.get(0), b = starts.get(1);
        int matchesCount = 0;
        for (int i = 0; i < 40000000; ++i) {
            a = (FACTOR_A * a) % DIVIDE_BY;
            b = (FACTOR_B * b) % DIVIDE_BY;
            // we compare the remainder modulo 2^16 to only use the last 16 bits
            if (a % KEEP_SIZE == b % KEEP_SIZE) {
                ++matchesCount;
            }
        }
        return String.valueOf(matchesCount);
    }

    @Override
    public String solvePart2(List<String> lines) throws AocException {
        final List<Long> starts = parseInput(lines);
        long a = starts.get(0), b = starts.get(1);
        int[] numbersA = new int[5000000];
        int[] numbersB = new int[5000000];
        int countA = 0, countB = 0;
        boolean doneA = false, doneB = false;
        while (!doneA || !doneB) {
            if (!doneA) {
                a = (FACTOR_A * a) % DIVIDE_BY;
                int shortA = (int) (a % KEEP_SIZE);
                if (shortA % 4 == 0) {
                    numbersA[countA++] = shortA;
                    if (countA == 5000000) {
                        doneA = true;
                    }
                }
            }
            if (!doneB) {
                b = (FACTOR_B * b) % DIVIDE_BY;
                int shortB = (int) (b % KEEP_SIZE);
                if (shortB % 8 == 0) {
                    numbersB[countB++] = shortB;
                    if (countB == 5000000) {
                        doneB = true;
                    }
                }
            }
        }
        int matchesCount = 0;
        for (int i = 0; i < 5000000; ++i) {
            if (numbersA[i] == numbersB[i]) {
                ++matchesCount;
            }
        }
        return String.valueOf(matchesCount);
    }

    /**
     * Parse the input lines
     */
    private List<Long> parseInput(List<String> lines) throws AocException {
        final Pattern pattern = Pattern.compile("[a-zA-Z ]+(\\d+)$");
        Matcher matcherA = pattern.matcher(lines.getFirst());
        if (!matcherA.matches()) {
            throw new AocException("Cannot find start value for generator A");
        }
        final long startA = Long.parseLong(matcherA.group(1));
        Matcher matcherB = pattern.matcher(lines.get(1));
        if (!matcherB.matches()) {
            throw new AocException("Cannot find start value for generator B");
        }
        final long startB = Long.parseLong(matcherB.group(1));
        return List.of(startA, startB);
    }
}
