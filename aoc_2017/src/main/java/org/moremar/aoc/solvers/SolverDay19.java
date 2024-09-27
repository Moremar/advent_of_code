package org.moremar.aoc.solvers;

import org.moremar.aoc.common.AocException;
import org.moremar.aoc.common.Coord;
import java.util.*;

public class SolverDay19 implements ISolverEngine {

    public SolverDay19() {
        super();
    }


    @Override
    public String solvePart1(List<String> lines) throws AocException {
        StringBuilder stringBuilder = new StringBuilder();
        traverse(parseInput(lines), stringBuilder);
        return stringBuilder.toString();
    }

    @Override
    public String solvePart2(List<String> lines) throws AocException {
        return String.valueOf(traverse(parseInput(lines), new StringBuilder()));
    }

    public int traverse(Map<Coord, Character> router, StringBuilder stringBuilder) {
        Coord curr = router.keySet().stream().filter(k -> k.y() == 0).toList().getFirst();
        Coord prev;
        Coord direction = Coord.DOWN;
        int steps = 1;
        while (true) {
            ++steps;
            prev = curr;
            curr = curr.add(direction);
            if (router.get(curr) >= 'A' && router.get(curr) <= 'Z') {
                stringBuilder.append(router.get(curr));
            }
            final List<Coord> adjacentNodes = curr.adjacent4().stream().filter(router::containsKey).toList();
            if (adjacentNodes.size() == 1) {
                break;
            }
            // change direction if we reached a corner
            if (router.get(curr) == '+') {
                for (Coord node : adjacentNodes) {
                    if (!node.equals(prev) && router.containsKey(node)) {
                        direction = node.subtract(curr);
                    }
                }
            }
        }
        return steps;
    }

    /**
     * Parse the input lines
     */
    public Map<Coord, Character> parseInput(List<String> lines) throws AocException {
        final Map<Coord, Character> router = new HashMap<>();
        for (int j = 0; j < lines.size(); ++j) {
            String line = lines.get(j);
            for (int i = 0; i < line.length(); ++i) {
                if (line.charAt(i) != ' ') {
                    router.put(new Coord(i, -j), line.charAt(i));
                }
            }
        }
        return router;
    }
}