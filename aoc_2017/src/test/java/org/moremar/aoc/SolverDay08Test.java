package org.moremar.aoc;

import org.junit.jupiter.api.Test;
import org.moremar.aoc.common.AocException;
import org.moremar.aoc.solvers.ISolverEngine;
import org.moremar.aoc.solvers.SolverDay08;
import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SolverDay08Test {

    final static String INPUT = """
            b inc 5 if a > 1
            a inc 1 if b < 5
            c dec -10 if a >= 1
            c inc -20 if c == 10
            """;

    @Test
    void solvePart1() throws AocException {
        AocScenario scenario = new AocScenario(Arrays.asList(INPUT.split("\n")), "1");
        ISolverEngine engine = new SolverDay08();
        assertEquals(scenario.expectedOutput(), engine.solvePart1(scenario.input()));
    }

    @Test
    void solvePart2() throws AocException {
        AocScenario scenario = new AocScenario(Arrays.asList(INPUT.split("\n")), "10");
        ISolverEngine engine = new SolverDay08();
        assertEquals(scenario.expectedOutput(), engine.solvePart2(scenario.input()));
    }
}