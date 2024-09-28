package org.moremar.aoc;

import org.junit.jupiter.api.Test;
import org.moremar.aoc.common.AocException;
import org.moremar.aoc.solvers.ISolverEngine;
import org.moremar.aoc.solvers.SolverDay22;
import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SolverDay22Test {

    final static String INPUT = """
            ..#
            #..
            ...
            """;

    @Test
    void solvePart1() throws AocException {
        AocScenario scenario = new AocScenario(Arrays.asList(INPUT.split("\n")), "5587");
        ISolverEngine engine = new SolverDay22();
        assertEquals(scenario.expectedOutput(), engine.solvePart1(scenario.input()));
    }

    @Test
    void solvePart2() throws AocException {
        AocScenario scenario = new AocScenario(Arrays.asList(INPUT.split("\n")), "2511944");
        ISolverEngine engine = new SolverDay22();
        assertEquals(scenario.expectedOutput(), engine.solvePart2(scenario.input()));
    }
}