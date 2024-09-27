package org.moremar.aoc;

import org.junit.jupiter.api.Test;
import org.moremar.aoc.common.AocException;
import org.moremar.aoc.solvers.ISolverEngine;
import org.moremar.aoc.solvers.SolverDay19;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SolverDay19Test {

    static final String INPUT = """
                 |
                 |  +--+
                 A  |  C
             F---|----E|--+
                 |  |  |  D
                 +B-+  +--+
            """;

    @Test
    void solvePart1() throws AocException {
        AocScenario scenario = new AocScenario(List.of(INPUT.split("\n")), "ABCDEF");
        ISolverEngine engine = new SolverDay19();
        assertEquals(scenario.expectedOutput(), engine.solvePart1(scenario.input()));
    }

    @Test
    void solvePart2() throws AocException {
        AocScenario scenario = new AocScenario(List.of(INPUT.split("\n")), "38");
        ISolverEngine engine = new SolverDay19();
        assertEquals(scenario.expectedOutput(), engine.solvePart2(scenario.input()));
    }
}