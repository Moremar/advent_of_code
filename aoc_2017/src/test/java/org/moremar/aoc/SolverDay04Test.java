package org.moremar.aoc;

import org.junit.jupiter.api.Test;
import org.moremar.aoc.common.AocException;
import org.moremar.aoc.solvers.ISolverEngine;
import org.moremar.aoc.solvers.SolverDay03;
import org.moremar.aoc.solvers.SolverDay04;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SolverDay04Test {

    @Test
    void solvePart1() throws AocException {
        List<AocScenario> scenarios = Arrays.asList(
                new AocScenario(List.of("aa bb cc dd ee"), "1"),
                new AocScenario(List.of("aa bb cc dd aa"), "0"),
                new AocScenario(List.of("aa bb cc dd aaa"), "1")
        );
        for (AocScenario scenario : scenarios) {
            ISolverEngine engine = new SolverDay04();
            assertEquals(scenario.expectedOutput(), engine.solvePart1(scenario.input()));
        }
    }

    @Test
    void solvePart2() throws AocException {
        List<AocScenario> scenarios = Arrays.asList(
                new AocScenario(List.of("abcde fghij"), "1"),
                new AocScenario(List.of("abcde xyz ecdab"), "0"),
                new AocScenario(List.of("a ab abc abd abf abj"), "1"),
                new AocScenario(List.of("iiii oiii ooii oooi oooo"), "1"),
                new AocScenario(List.of("oiii ioii iioi iiio"), "0")
        );
        for (AocScenario scenario : scenarios) {
            ISolverEngine engine = new SolverDay04();
            assertEquals(scenario.expectedOutput(), engine.solvePart2(scenario.input()));
        }
    }
}