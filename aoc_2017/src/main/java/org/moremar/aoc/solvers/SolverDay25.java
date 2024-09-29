package org.moremar.aoc.solvers;

import org.moremar.aoc.common.AocException;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class SolverDay25 implements ISolverEngine {

    private record TuringAction(int valueToWrite, int shift, String nextState) {}

    private record TuringState(TuringAction action0, TuringAction action1) {
        public TuringAction getAction(int value) {
            return value == 0 ? action0 : action1;
        }
    }

    private static class TuringMachine {

        private final Map<String, TuringState> myStates;
        private final Map<Integer, Integer> myTape = new HashMap<>();
        private int myCursor = 0;
        private String myCurrentState;
        private int myStepsLeft;

        public TuringMachine(Map<String, TuringState> states, String initialState, int steps){
            myStates = states;
            myCurrentState = initialState;
            myStepsLeft = steps;
        }

        private void run() {
            while (myStepsLeft > 0) {
                TuringAction action = myStates.get(myCurrentState)
                                              .getAction(myTape.getOrDefault(myCursor, 0));
                myTape.put(myCursor, action.valueToWrite);
                myCursor += action.shift;
                myCurrentState = action.nextState;
                --myStepsLeft;
            }
        }

        public int getCheckSum() {
            return myTape.values().stream().reduce(0, Integer::sum);
        }
    }

    public SolverDay25() {
        super();
    }

    @Override
    public String solvePart1(List<String> lines) throws AocException {
        TuringMachine turingMachine = parseInput(lines);
        turingMachine.run();
        return String.valueOf(turingMachine.getCheckSum());
    }

    @Override
    public String solvePart2(List<String> lines) throws AocException {
        // no part 2 on the last day
        return "COMPLETE";
    }

    /**
     * Parse the input lines
     */
    private TuringMachine parseInput(List<String> lines) throws AocException {
        Map<String, TuringState> states = new HashMap<>();

        Pattern initialStatePattern = Pattern.compile("Begin in state ([A-Z]).");
        Pattern stepsPattern = Pattern.compile("Perform a diagnostic checksum after (\\d+) steps.");
        Pattern currStatePattern = Pattern.compile("In state ([A-Z]):");
        Pattern valuePattern = Pattern.compile(" {4}- Write the value ([01])\\.");
        Pattern shiftPattern = Pattern.compile(" {4}- Move one slot to the (\\w+)\\.");
        Pattern statePattern = Pattern.compile(" {4}- Continue with state ([A-Z])\\.");

        int lineNumber = 0;

        // initial state
        Matcher matcher = initialStatePattern.matcher(lines.get(lineNumber));
        if (!matcher.matches()) {
            throw new AocException("Failed to parse initial state line : " + lines.get(lineNumber));
        }
        String initialStateName = matcher.group(1);
        ++lineNumber;
        // number of steps required
        matcher = stepsPattern.matcher(lines.get(lineNumber));
        if (!matcher.matches()) {
            throw new AocException("Failed to parse steps line : " + lines.get(lineNumber));
        }
        int steps = Integer.parseInt(matcher.group(1));
        lineNumber += 2;

        while (lineNumber < lines.size()) {
            // state name
            matcher = currStatePattern.matcher(lines.get(lineNumber));
            if (!matcher.matches()) {
                throw new AocException("Failed to parse current state line : " + lines.get(lineNumber));
            }
            String stateName = matcher.group(1);
            lineNumber += 2;

            // value to write if the current value is 0
            matcher = valuePattern.matcher(lines.get(lineNumber));
            if (!matcher.matches()) {
                throw new AocException("Failed to parse value line : " + lines.get(lineNumber));
            }
            int valueToWrite0 = Integer.parseInt(matcher.group(1));
            ++lineNumber;

            // shift to apply to the tape if the current value is 0
            matcher = shiftPattern.matcher(lines.get(lineNumber));
            if (!matcher.matches()) {
                throw new AocException("Failed to parse shift line : " + lines.get(lineNumber));
            }
            int shift0 = Objects.equals(matcher.group(1), "left") ? -1 : 1;
            ++lineNumber;

            // next state if the current value is 0
            matcher = statePattern.matcher(lines.get(lineNumber));
            if (!matcher.matches()) {
                throw new AocException("Failed to parse next state line : " + lines.get(lineNumber));
            }
            String nextState0 = matcher.group(1);
            lineNumber += 2;

            // value to write if the current value is 1
            matcher = valuePattern.matcher(lines.get(lineNumber));
            if (!matcher.matches()) {
                throw new AocException("Failed to parse value line : " + lines.get(lineNumber));
            }
            int valueToWrite1 = Integer.parseInt(matcher.group(1));
            ++lineNumber;

            // shift to apply to the tape if the current value is 1
            matcher = shiftPattern.matcher(lines.get(lineNumber));
            if (!matcher.matches()) {
                throw new AocException("Failed to parse shift line : " + lines.get(lineNumber));
            }
            int shift1 = Objects.equals(matcher.group(1), "left") ? -1 : 1;
            ++lineNumber;

            // next state if the current value is 1
            matcher = statePattern.matcher(lines.get(lineNumber));
            if (!matcher.matches()) {
                throw new AocException("Failed to parse next state line : " + lines.get(lineNumber));
            }
            String nextState1 = matcher.group(1);
            lineNumber += 2;

            // add a state for the Turing machine
            states.put(stateName, new TuringState(
                    new TuringAction(valueToWrite0, shift0, nextState0),
                    new TuringAction(valueToWrite1, shift1, nextState1)
            ));
        }
        return new TuringMachine(states, initialStateName, steps);
    }
}