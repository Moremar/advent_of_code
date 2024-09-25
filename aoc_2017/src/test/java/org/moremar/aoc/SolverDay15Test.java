package org.moremar.aoc;

import org.junit.jupiter.api.Test;
import org.moremar.aoc.common.AocException;
import org.moremar.aoc.solvers.ISolverEngine;
import org.moremar.aoc.solvers.SolverDay15;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SolverDay15Test {

    static final String INPUT = """
            Generator A starts with 65
            Generator B starts with 8921
            """;

    @Test
    void solvePart1() throws AocException {
        AocScenario scenario = new AocScenario(List.of(INPUT.split("\n")), "588");
        ISolverEngine engine = new SolverDay15();
        assertEquals(scenario.expectedOutput(), engine.solvePart1(scenario.input()));
    }

    @Test
    void solvePart2() throws AocException {
        AocScenario scenario = new AocScenario(List.of(INPUT.split("\n")), "309");
        ISolverEngine engine = new SolverDay15();
        assertEquals(scenario.expectedOutput(), engine.solvePart2(scenario.input()));
    }
}