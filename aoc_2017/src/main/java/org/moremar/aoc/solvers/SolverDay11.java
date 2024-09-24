package org.moremar.aoc.solvers;

import java.util.*;

public class SolverDay11 implements ISolverEngine {

    public SolverDay11() {
        super();
    }

    static final List<List<String>> OFFSET = List.of(
            List.of("n", "s"),
            List.of("nw", "se"),
            List.of("sw", "ne"));

    static final List<List<String>> SIMPLIFY = List.of(
            List.of("nw", "ne", "n"),
            List.of("n", "se", "ne"),
            List.of("ne", "s", "se"),
            List.of("se", "sw", "s"),
            List.of("s", "nw", "sw"),
            List.of("sw", "n", "nw"));

    @Override
    public String solvePart1(List<String> lines) {
        Map<String, Integer> moves = parseInput(lines);
        return String.valueOf(shortestPath(moves));
    }

    private int shortestPath(Map<String, Integer> moves) {
        boolean hasChanged;
        do {
            hasChanged = false;
            // eliminates pairs that offset
            for (var formula : OFFSET) {
                int dir0 = moves.get(formula.get(0));
                int dir1 = moves.get(formula.get(1));
                if (dir0 > 0 && dir1 > 0) {
                    moves.put(formula.get(0), dir0 - Integer.min(dir0, dir1));
                    moves.put(formula.get(1), dir1 - Integer.min(dir0, dir1));
                    hasChanged = true;
                }
            }
            // replace pairs that can be simplified
            for (var formula : SIMPLIFY) {
                int dir0 = moves.get(formula.get(0));
                int dir1 = moves.get(formula.get(1));
                int dir2 = moves.get(formula.get(2));
                if (dir0 > 0 && dir1 > 0) {
                    moves.put(formula.get(0), dir0 - Integer.min(dir0, dir1));
                    moves.put(formula.get(1), dir1 - Integer.min(dir0, dir1));
                    moves.put(formula.get(2), dir2 + Integer.min(dir0, dir1));
                    hasChanged = true;
                }
            }
        } while (hasChanged);
        return moves.values().stream().reduce(Integer::sum).orElseThrow();
    }

    @Override
    public String solvePart2(List<String> lines) {
        List<Map<String, Integer>> movesSuccessive = parseInputSuccessive(lines);
        return String.valueOf(movesSuccessive.stream().mapToInt(this::shortestPath).max().orElseThrow());
    }

    /**
     * Parse the input lines to get a map of the number of steps in each direction
     */
    private Map<String, Integer> parseInput(List<String> lines) {
        Map<String, Integer> moves = new HashMap<>(Map.of(
                "s", 0,
                "se", 0,
                "ne", 0,
                "n", 0,
                "nw", 0,
                "sw", 0
        ));
        for (String dir : lines.getFirst().split(",")) {
            moves.put(dir, moves.get(dir) + 1);
        }
        return moves;
    }

    /**
     * Parse the input lines to get a list of map of the number of steps in each directions
     * after every single move
     */
    private List<Map<String, Integer>> parseInputSuccessive(List<String> lines) {
        List<Map<String, Integer>> movesSequence = new ArrayList<>();
        Map<String, Integer> moves = new HashMap<>(Map.of(
                "s", 0,
                "se", 0,
                "ne", 0,
                "n", 0,
                "nw", 0,
                "sw", 0
        ));
        for (String dir : lines.getFirst().split(",")) {
            moves.put(dir, moves.get(dir) + 1);
            movesSequence.add(new HashMap<>(moves));
        }
        return movesSequence;
    }
}
