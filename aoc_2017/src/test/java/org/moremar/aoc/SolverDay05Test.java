package org.moremar.aoc;

import org.junit.jupiter.api.Test;
import org.moremar.aoc.common.AocException;
import org.moremar.aoc.solvers.ISolverEngine;
import org.moremar.aoc.solvers.SolverDay05;
import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SolverDay05Test {

    @Test
    void solvePart1() throws AocException {
        AocScenario scenario = new AocScenario(
                Arrays.asList("0", "3", "0", "1", "-3"),
                "5");
        ISolverEngine engine = new SolverDay05();
        assertEquals(scenario.expectedOutput(), engine.solvePart1(scenario.input()));
    }

    @Test
    void solvePart2() throws AocException {
        AocScenario scenario = new AocScenario(
                Arrays.asList("0", "3", "0", "1", "-3"),
                "10");
        ISolverEngine engine = new SolverDay05();
        assertEquals(scenario.expectedOutput(), engine.solvePart2(scenario.input()));
    }
}