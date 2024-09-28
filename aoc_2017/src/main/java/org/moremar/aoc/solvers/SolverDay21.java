package org.moremar.aoc.solvers;

import org.moremar.aoc.common.AocException;
import java.util.*;

public class SolverDay21 implements ISolverEngine {

    public SolverDay21() {
        super();
    }

    @Override
    public String solvePart1(List<String> lines) throws AocException {
        final List<String[]> rules = parseInput(lines);
        final String[] world = { ".#.", "..#", "###" };
        return String.valueOf(transform(world, rules, 5));
    }

    public int transform(String[] world, List<String[]> rules, int times) throws AocException {
        for (int t = 0; t < times; ++t) {
            world = transformOnce(world, rules);
        }
        // return the number of lights that are on
        return Arrays.stream(world)
                     .mapToInt(s -> s.chars().map(c -> c == '#' ? 1 : 0).sum())
                     .sum();
    }

    private String[] transformOnce(String[] world, List<String[]> rules) throws AocException {
        final int squareSize = (world.length % 2 == 0) ? 2 : 3;
        final String[] transformed = new String[world.length * (squareSize + 1) / squareSize];
        for (int i = 0; i < world.length / squareSize; ++i) {
            StringBuilder[] gridRowBuilders = new StringBuilder[squareSize+1];
            for (int k = 0; k < gridRowBuilders.length; ++k) {
                gridRowBuilders[k] = new StringBuilder();
            }
            for (int j = 0; j < world.length / squareSize; ++j) {
                // process the square in position (i, j) in the input grid
                StringBuilder squareKey = new StringBuilder();
                squareKey.append(world[i * squareSize], j * squareSize, (j+1) * squareSize);
                for (int k = 1; k < squareSize; ++k) {
                    squareKey.append("/")
                             .append(world[i * squareSize + k], j * squareSize, (j+1) * squareSize);
                }
                String convertedKey = convertKey(squareKey.toString(), rules);
                var convertedKeyArr = convertedKey.split("/");
                for (int k = 0; k < gridRowBuilders.length; ++k) {
                    gridRowBuilders[k].append(convertedKeyArr[k]);
                }
            }
            for (int k = 0; k < gridRowBuilders.length; ++k) {
                transformed[i * (squareSize + 1) + k] = gridRowBuilders[k].toString();
            }
        }
        return transformed;
    }

    private String convertKey(String squareKey, List<String[]> rules) throws AocException {
        // find the corresponding rule, by applying to the square key
        // any flip and rotation
        String flippedKey = flip(squareKey);
        List<String> rotatedKeys = rotate(squareKey);
        List<String> flippedRotatedKeys = rotate(flippedKey);
        List<String> candidates = new ArrayList<>();
        candidates.add(squareKey);
        candidates.add(flippedKey);
        candidates.addAll(rotatedKeys);
        candidates.addAll(flippedRotatedKeys);
        for (String candidate : candidates) {
            for (String[] rule : rules) {
                if (candidate.equals(rule[0])) {
                    return rule[1];
                }
            }
        }
        throw new AocException("Did not find a matching rule for square key: " + squareKey);
    }

    private String flip(String squareKey) {
        List<String> flipped = Arrays.stream(squareKey.split("/"))
                                     .map(s->new StringBuilder(s).reverse().toString())
                                     .toList();
        return String.join("/", flipped);
    }

    private List<String> rotate(String squareKey) {
        final List<String> rotatedKeys = new ArrayList<>();
        // apply 3 rotations to include all possible rotated keys
        String currKey = squareKey;
        for (int k = 0; k < 3; ++k) {
            String[] keyRows = currKey.split("/");
           StringBuilder builder = new StringBuilder();
           for (int j = 0; j < keyRows.length; ++j) {
                for (int i = keyRows.length - 1; i >= 0; --i) {
                    builder.append(keyRows[i].charAt(j));
                }
                builder.append("/");
            }
            currKey = builder.deleteCharAt(builder.length()-1).toString();
            rotatedKeys.add(currKey);
        }
        return rotatedKeys;
    }

    @Override
    public String solvePart2(List<String> lines) throws AocException {
        final List<String[]> rules = parseInput(lines);
        final String[] world = { ".#.", "..#", "###" };
        return String.valueOf(transform(world, rules, 18));
    }

    /**
     * Parse the input lines
     */
    public List<String[]> parseInput(List<String> lines) throws AocException {
        return lines.stream()
                    .map(s -> s.split(" => "))
                    .toList();
    }
}