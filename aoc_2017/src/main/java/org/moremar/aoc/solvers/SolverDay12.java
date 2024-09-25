package org.moremar.aoc.solvers;

import org.moremar.aoc.common.AocException;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class SolverDay12 implements ISolverEngine {

    public SolverDay12() {
        super();
    }

    @Override
    public String solvePart1(List<String> lines) throws AocException {
        final List<int[]> nodes = parseInput(lines);
        return String.valueOf(findGroup(nodes, 0).size());
    }

    private Set<Integer> findGroup(List<int[]> nodes, int rootNodeId) {
        final Set<Integer> inGroup = new HashSet<>();
        final Deque<Integer> toCheck = new LinkedList<>();
        toCheck.add(rootNodeId);
        while (!toCheck.isEmpty()) {
            int nodeId = toCheck.pollFirst();
            if (inGroup.contains(nodeId)) {
                continue;
            }
            inGroup.add(nodeId);
            for (int connectedNodeId : nodes.get(nodeId)) {
                toCheck.add(connectedNodeId);
            }
        }
        return inGroup;
    }

    @Override
    public String solvePart2(List<String> lines) throws AocException {
        final List<int[]> nodes = parseInput(lines);
        final Set<Integer> seen = new HashSet<>();
        int groupCount = 0;
        for (int i = 0; i < nodes.size(); ++i) {
            if (!seen.contains(i)) {
                ++groupCount;
                seen.addAll(findGroup(nodes, i));
            }
        }
        return String.valueOf(groupCount);
    }

    /**
     * Parse the input lines to get a list of the connected node IDs for each node
     */
    private List<int[]> parseInput(List<String> lines) throws AocException {
        final List<int[]> nodes = new ArrayList<>();
        final Pattern pattern = Pattern.compile("\\d+ <-> ([\\d ,]+)");
        for (String line : lines) {
            Matcher matcher = pattern.matcher(line);
            if (!matcher.matches()) {
                throw new AocException("Failed to parse line : " + line);
            }
            nodes.add(Arrays.stream(matcher.group(1).split(", ")).mapToInt(Integer::parseInt).toArray());
        }
        return nodes;
    }
}
