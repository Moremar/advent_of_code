package org.moremar.aoc.solvers;

import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;

public class SolverDay10 implements ISolverEngine {

    public SolverDay10() {
        super();
    }

    public record State(int position, int skipSize) {}

    @Override
    public String solvePart1(List<String> lines) {
        final int[] lengths = parseInput(lines);
        int nodeCount = 256;
        int[] nodes = IntStream.range(0, nodeCount).toArray();
        applyRound(nodes, lengths, new State(0, 0));
        return String.valueOf(nodes[0] * nodes[1]);
    }

    public static State applyRound(int[] nodes, int[] lengths, State state) {
        int nodeCount = nodes.length;
        int pos = state.position;
        int skipSize = state.skipSize;

        for (int length : lengths) {
            int left = pos;
            int right = pos + length - 1;
            while (right > left) {
                int tmp = nodes[left % nodeCount];
                nodes[left % nodeCount] = nodes[right % nodeCount];
                nodes[right % nodeCount] = tmp;
                ++left;
                --right;
            }
            pos = (pos + length + skipSize) % nodeCount;
            ++skipSize;
        }
        return new State(pos, skipSize);
    }

    @Override
    public String solvePart2(List<String> lines) {
        return getKnotHash(lines.getFirst());
    }

    public static String getKnotHash(String line) {
        final int[] lengths = parseInputAscii(line);
        // run 64 rounds
        int nodeCount = 256;
        int[] nodes = IntStream.range(0, nodeCount).toArray();
        int position = 0, skipSize = 0;
        for (int i = 0; i < 64; ++i) {
            State state = applyRound(nodes, lengths, new State(position, skipSize));
            position = state.position;
            skipSize = state.skipSize;
        }
        // reduce the nodes by groups of 16 nodes
        StringBuilder hash = new StringBuilder();
        for (int i = 0; i < 16; ++i) {
            int xor = Arrays.stream(nodes, i * 16, i * 16 + 16)
                            .reduce((x, y) -> x ^ y)
                            .orElse(0);
            hash.append(String.format("%02x", xor));
        }
        return hash.toString();
    }

    /**
     * Parse the input lines as comma-separated integers
     */
    private int[] parseInput(List<String> lines) {
        return Arrays.stream(lines.getFirst().split(","))
                     .mapToInt(Integer::parseInt)
                     .toArray();
    }

    /**
     * Parse the input lines as ASCII codes
     */
    private static int[] parseInputAscii(String line) {
        int[] result = new int[line.length() + 5];
        int position = 0;
        while (position < line.length()) {
            result[position] = line.charAt(position);
            ++position;
        }
        // add hard-coded values in the lengths
        result[position++] = 17;
        result[position++] = 31;
        result[position++] = 73;
        result[position++] = 47;
        result[position] = 23;
        return result;
    }
}
