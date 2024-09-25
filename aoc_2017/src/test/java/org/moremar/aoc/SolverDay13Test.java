package org.moremar.aoc;

import org.junit.jupiter.api.Test;
import org.moremar.aoc.common.AocException;
import org.moremar.aoc.solvers.ISolverEngine;
import org.moremar.aoc.solvers.SolverDay13;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SolverDay13Test {

    static final String INPUT = """
            0: 3
            1: 2
            4: 4
            6: 4
            """;

    @Test
    void solvePart1() throws AocException {
        AocScenario scenario = new AocScenario(List.of(INPUT.split("\n")), "24");
        ISolverEngine engine = new SolverDay13();
        assertEquals(scenario.expectedOutput(), engine.solvePart1(scenario.input()));
    }

    @Test
    void solvePart2() throws AocException {
        AocScenario scenario = new AocScenario(List.of(INPUT.split("\n")), "10");
        ISolverEngine engine = new SolverDay13();
        assertEquals(scenario.expectedOutput(), engine.solvePart2(scenario.input()));
    }
}