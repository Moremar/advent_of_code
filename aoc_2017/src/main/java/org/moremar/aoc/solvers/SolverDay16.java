package org.moremar.aoc.solvers;

import org.moremar.aoc.common.AocException;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class SolverDay16 implements ISolverEngine {

    static final String SPIN = "s";
    static final String EXCHANGE = "x";
    static final String PARTNER = "p";

    public record DanceMove(String danceType, String param1, String param2) {}

    public SolverDay16() {
        super();
    }

    @Override
    public String solvePart1(List<String> lines) throws AocException {
        List<DanceMove> danceMoves = parseInput(lines);
        return getStateAfterOneDance(danceMoves, 16);
    }

    public String getStateAfterOneDance(List<DanceMove> danceMoves, int programCount) {
        // initialize the programs list
        String[] programs = new String[programCount];
        for (int i = 0; i < programCount; ++i) {
            programs[i] = String.valueOf((char) ('a' + i));
        }
        // run a single dance
        runOneDance(danceMoves, programs);
        return String.join("", programs);
    }

    public void runOneDance(List<DanceMove> danceMoves, String[] programs) {
        // perform the dances
        for (DanceMove danceMove : danceMoves) {
            if (Objects.equals(danceMove.danceType, SPIN)) {
                int spinSize = Integer.parseInt(danceMove.param1);
                String[] tmp = programs.clone();
                if (spinSize >= 0) {
                    System.arraycopy(tmp, programs.length - spinSize, programs, 0, spinSize);
                }
                if (programs.length - spinSize >= 0) {
                    System.arraycopy(tmp, 0, programs, spinSize, programs.length - spinSize);
                }
            } else if (Objects.equals(danceMove.danceType, EXCHANGE)) {
                int pos1 = Integer.parseInt(danceMove.param1);
                int pos2 = Integer.parseInt(danceMove.param2);
                String tmp = programs[pos1];
                programs[pos1] = programs[pos2];
                programs[pos2] = tmp;
            } else {
                int pos1 = -1, pos2 = -1;
                String name1 = danceMove.param1;
                String name2 = danceMove.param2;
                for (int i = 0; i < programs.length; ++i) {
                    if (Objects.equals(programs[i], name1)) {
                        pos1 = i;
                    }
                    if (Objects.equals(programs[i], name2)) {
                        pos2 = i;
                    }
                }
                String tmp = programs[pos1];
                programs[pos1] = programs[pos2];
                programs[pos2] = tmp;
            }
        }
    }

    @Override
    public String solvePart2(List<String> lines) throws AocException {
        List<DanceMove> danceMoves = parseInput(lines);
        return getStateAfterMultipleDances(danceMoves, 16, 1000000000);
    }

    public String getStateAfterMultipleDances(List<DanceMove> danceMoves, int programCount, long danceCount) {
        // initialize the programs list
        String[] programs = new String[programCount];
        for (int i = 0; i < programCount; ++i) {
            programs[i] = String.valueOf((char) ('a' + i));
        }
        String initialState = String.join("", programs);

        // find the cycle in the dance results
        List<String> states = new ArrayList<>();
        states.add(initialState);
        int danceId = 0;
        String danceResult = "";
        while (!danceResult.equals(initialState)) {
            runOneDance(danceMoves, programs);
            ++danceId;
            danceResult = String.join("", programs);
            states.add(danceResult);
        }

        // deduce the state after the target number of dances
        return states.get((int) (danceCount % danceId));
    }

    /**
     * Parse the input lines
     */
    public List<DanceMove> parseInput(List<String> lines) throws AocException {
        final List<DanceMove> danceMoves = new LinkedList<>();

        final Pattern spinPattern = Pattern.compile(SPIN + "(\\d+)");
        final Pattern exchangePattern = Pattern.compile(EXCHANGE + "(\\d+)/(\\d+)");
        final Pattern partnerPattern = Pattern.compile(PARTNER + "(\\w)/(\\w)");

        for (String danceStr : lines.getFirst().split(",")) {
            if (danceStr.startsWith(SPIN)) {
                Matcher matcher = spinPattern.matcher(danceStr);
                if (!matcher.matches()) {
                    throw new AocException("Failed to parse spin : " + danceStr);
                }
                danceMoves.add(new DanceMove(SPIN, matcher.group(1), ""));
            } else if (danceStr.startsWith(EXCHANGE)) {
                Matcher matcher = exchangePattern.matcher(danceStr);
                if (!matcher.matches()) {
                    throw new AocException("Failed to parse exchange : " + danceStr);
                }
                danceMoves.add(new DanceMove(EXCHANGE, matcher.group(1), matcher.group(2)));
            } else if (danceStr.startsWith(PARTNER)) {
                Matcher matcher = partnerPattern.matcher(danceStr);
                if (!matcher.matches()) {
                    throw new AocException("Failed to parse partner : " + danceStr);
                }
                danceMoves.add(new DanceMove(PARTNER, matcher.group(1), matcher.group(2)));
            } else {
                throw new AocException("Unknown dance type");
            }
        }
        return danceMoves;
    }
}