package org.moremar.aoc;

import org.junit.jupiter.api.Test;
import org.moremar.aoc.common.AocException;
import org.moremar.aoc.solvers.ISolverEngine;
import org.moremar.aoc.solvers.SolverDay02;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SolverDay02Test {

    @Test
    void solvePart1() throws AocException {
        AocScenario scenario = new AocScenario(
                Arrays.asList("5 9 2 8", "9 4 7 3",  "3 8 6 5"),
                "18");
        ISolverEngine engine = new SolverDay02();
        assertEquals(scenario.expectedOutput(), engine.solvePart1(scenario.input()));
    }

    @Test
    void solvePart2() throws AocException {
        AocScenario scenario = new AocScenario(
                Arrays.asList("5 9 2 8", "9 4 7 3",  "3 8 6 5"),
                "9");
        ISolverEngine engine = new SolverDay02();
        assertEquals(scenario.expectedOutput(), engine.solvePart2(scenario.input()));
    }
}