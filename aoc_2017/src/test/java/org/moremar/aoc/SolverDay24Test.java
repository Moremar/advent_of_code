package org.moremar.aoc;

import org.junit.jupiter.api.Test;
import org.moremar.aoc.common.AocException;
import org.moremar.aoc.solvers.ISolverEngine;
import org.moremar.aoc.solvers.SolverDay24;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SolverDay24Test {

    static final String INPUT = """
            0/2
            2/2
            2/3
            3/4
            3/5
            0/1
            10/1
            9/10
            """;

    @Test
    void solvePart1() throws AocException {
        AocScenario scenario = new AocScenario(List.of(INPUT.split("\n")), "31");
        ISolverEngine engine = new SolverDay24();
        assertEquals(scenario.expectedOutput(), engine.solvePart1(scenario.input()));
    }

    @Test
    void solvePart2() throws AocException {
        AocScenario scenario = new AocScenario(List.of(INPUT.split("\n")), "19");
        ISolverEngine engine = new SolverDay24();
        assertEquals(scenario.expectedOutput(), engine.solvePart2(scenario.input()));
    }
}