package org.moremar.aoc.solvers;

import org.moremar.aoc.common.AocException;
import java.util.*;

public class SolverDay06 implements ISolverEngine {

    public SolverDay06() {
        super();
    }

    @Override
    public String solvePart1(List<String> lines) throws AocException {
        int[] banks = parseInput(lines);
        Set<String> seen = new HashSet<>();
        String currState = hash(banks);
        int cycles = 0;
        while (!seen.contains(currState)) {
            seen.add(currState);
            ++cycles;
            // find the bank with the most blocks
            int blocks = banks[0];
            int bank = 0;
            for (int i = 1; i < banks.length; ++i) {
                if (banks[i] > blocks) {
                    blocks = banks[i];
                    bank = i;
                }
            }
            // reallocate its blocks
            banks[bank] = 0;
            while (blocks > 0) {
                bank = (bank + 1) % banks.length;
                --blocks;
                ++banks[bank];
            }
            currState = hash(banks);
        }
        return String.valueOf(cycles);
    }

    @Override
    public String solvePart2(List<String> lines) {
        int[] banks = parseInput(lines);
        Set<String> seen = new HashSet<>();
        Map<String, Integer> stateCycles = new HashMap<>();
        String currState = hash(banks);
        int cycles = 0;
        while (!seen.contains(currState)) {
            seen.add(currState);
            stateCycles.put(currState, cycles);
            ++cycles;
            // find the bank with the most blocks
            int blocks = banks[0];
            int bank = 0;
            for (int i = 1; i < banks.length; ++i) {
                if (banks[i] > blocks) {
                    blocks = banks[i];
                    bank = i;
                }
            }
            // reallocate its blocks
            banks[bank] = 0;
            while (blocks > 0) {
                bank = (bank + 1) % banks.length;
                --blocks;
                ++banks[bank];
            }
            currState = hash(banks);
        }
        return String.valueOf(cycles - stateCycles.get(currState));
    }

    /**
     * Create a String that represents a memory state, so it can be used
     * as a key in the set tracking the memory states already seen
     */
    private String hash(int[] banks) {
        return String.join("_", Arrays.stream(banks)
                                              .boxed()
                                              .map(String::valueOf)
                                              .toList()
                                              .toArray(new String[0]));
    }

    /**
     * Parse the input lines
     */
    private int[] parseInput(List<String> lines) {
        return Arrays.stream(lines.getFirst().split("[ \t]+"))
                     .mapToInt(Integer::parseInt)
                     .toArray();
    }
}
