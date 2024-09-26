package org.moremar.aoc.solvers;

import org.moremar.aoc.common.AocException;
import java.util.List;

public class SolverDay17 implements ISolverEngine {

    private static class VortexNode {
        // private members
        private final int value;
        private VortexNode next = null;

        // constructor
        public VortexNode(int val) { value = val; }

        // getters / setters
        public VortexNode getNext() { return next; }
        public void setNext(VortexNode next) { this.next = next; }
        public int getValue() { return value; }
    }

    public SolverDay17() {
        super();
    }

    @Override
    public String solvePart1(List<String> lines) throws AocException {
        int steps = parseInput(lines);
        // initialize circular vortex
        int nextVal = 0;
        VortexNode vortex = new VortexNode(nextVal++);
        vortex.setNext(vortex);
        // build the vortex
        while (nextVal <= 2017) {
            for (int i = 0; i < (steps % nextVal); ++i) {
                vortex = vortex.next;
            }
            VortexNode inserted = new VortexNode(nextVal++);
            inserted.setNext(vortex.getNext());
            vortex.setNext(inserted);
            vortex = inserted;
        }
        return String.valueOf(vortex.getNext().getValue());
    }

    @Override
    public String solvePart2(List<String> lines) throws AocException {
        /*
         * There are too many steps to build the full vortex
         * Since we only care about the value just after the 0, we only check
         * at each insertion if the new element would be after the 0 or not
         */
        int steps = parseInput(lines);
        int currPosition = 0;
        int after0 = 0;
        for (int i = 1; i <= 50000000; ++i) {
            currPosition = (currPosition + steps) % i;
            if (currPosition == 0) { after0 = i; }
            ++currPosition;
        }
        return String.valueOf(after0);
    }

    /**
     * Parse the input lines
     */
    public int parseInput(List<String> lines) throws AocException {
        return Integer.parseInt(lines.getFirst());
    }
}