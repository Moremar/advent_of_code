package org.moremar.aoc.solvers;

import org.moremar.aoc.common.AocException;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class SolverDay07 implements ISolverEngine {

    public SolverDay07() {
        super();
    }

    @Override
    public String solvePart1(List<String> lines) throws AocException {
        Map<String, Program> programs = parseInput(lines);
        for (Map.Entry<String, Program> entry : programs.entrySet()) {
            if (entry.getValue().getParentName() == null) {
                return entry.getKey();
            }
        }
        throw new AocException("Failed to find the root program");
    }

    @Override
    public String solvePart2(List<String> lines) throws AocException {
        Map<String, Program> programs = parseInput(lines);
        // find the unbalanced program that has only balanced children
        // this means that the weight of one of its direct children must be adjusted
        for (Program program : programs.values()) {
            if (!program.isBalanced() && program.getChildren().stream().allMatch(Program::isBalanced)) {
                Map<Integer, List<Program>> totalWeights = new HashMap<>();
                for (Program child : program.getChildren()) {
                    if (!totalWeights.containsKey(child.getTotalWeight())) {
                        totalWeights.put(child.getTotalWeight(), new ArrayList<>());
                    }
                    totalWeights.get(child.getTotalWeight()).add(child);
                }
                assert totalWeights.size() == 2;
                int targetTotalWeight = -1;
                Program programToAdjust = null;
                for (Map.Entry<Integer, List<Program>> weightEntry : totalWeights.entrySet()) {
                    if (weightEntry.getValue().size() == 1) {
                        programToAdjust = weightEntry.getValue().getFirst();
                    } else {
                        targetTotalWeight = weightEntry.getKey();
                    }
                }
                // the weight of the program must be adjusted so its total weight is equal to its siblings
                assert programToAdjust != null;
                final int adjustedWeight = programToAdjust.getWeight() - (programToAdjust.getTotalWeight() - targetTotalWeight);
                return String.valueOf(adjustedWeight);
            }
        }
        throw new AocException("Failed to find the program to adjust");
    }

    /**
     * Class representing one program in the hierarchy
     */
    private static class Program {

        private int weight;
        private List<Program> children = new ArrayList<>();
        private String parentName;
        private int totalWeight = -1;

        boolean isBalanced() {
            return children.stream().mapToInt(Program::getTotalWeight).distinct().toArray().length < 2;
        }

        int getTotalWeight() {
            if (totalWeight < 0) {
                totalWeight = weight + children.stream().mapToInt(Program::getTotalWeight).sum();
            }
            return totalWeight;
        }

        public List<Program> getChildren() {
            return children;
        }

        public void setChildren(List<Program> children) {
            this.children = children;
        }

        public String getParentName() {
            return parentName;
        }

        public void setParentName(String parentName) {
            this.parentName = parentName;
        }

        public int getWeight() {
            return weight;
        }

        public void setWeight(int weight) {
            this.weight = weight;
        }
    }

    /**
     * Parse the input lines
     */
    private Map<String, Program> parseInput(List<String> lines) throws AocException {
        Map<String, Program> programs = new HashMap<>();
        final Pattern pattern = Pattern.compile("^(\\w+) \\((\\d+)\\)( -> )?([\\w ,]*)");
        for (String line : lines) {
            Matcher matcher = pattern.matcher(line);
            if (!matcher.find()) {
                throw new AocException("Could not parse line : " + line);
            }
            final String name = matcher.group(1);
            final int weight = Integer.parseInt(matcher.group(2));
            final String[] childrenNames = matcher.group(4).split(", ");
            // add info about this program to the map
            if (!programs.containsKey(name)) {
                programs.put(name, new Program());
            }
            programs.get(name).setWeight(weight);
            List<Program> children = new LinkedList<>();
            programs.get(name).setChildren(children);
            // add info about children programs
            for (String childName : childrenNames) {
                if (!programs.containsKey(childName)) {
                    programs.put(childName, new Program());
                }
                programs.get(childName).setParentName(name);
                children.add(programs.get(childName));
            }
            programs.get(name).setChildren(children);
        }
        return programs;
    }
}
