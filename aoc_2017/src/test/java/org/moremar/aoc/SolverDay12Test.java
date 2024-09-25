package org.moremar.aoc;

import org.junit.jupiter.api.Test;
import org.moremar.aoc.common.AocException;
import org.moremar.aoc.solvers.ISolverEngine;
import org.moremar.aoc.solvers.SolverDay02;
import org.moremar.aoc.solvers.SolverDay12;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SolverDay12Test {

    static final String INPUT = """
            0 <-> 2
            1 <-> 1
            2 <-> 0, 3, 4
            3 <-> 2, 4
            4 <-> 2, 3, 6
            5 <-> 6
            6 <-> 4, 5
            """;

    @Test
    void solvePart1() throws AocException {
        AocScenario scenario = new AocScenario(List.of(INPUT.split("\n")), "6");
        ISolverEngine engine = new SolverDay12();
        assertEquals(scenario.expectedOutput(), engine.solvePart1(scenario.input()));
    }

    @Test
    void solvePart2() throws AocException {
        AocScenario scenario = new AocScenario(List.of(INPUT.split("\n")), "2");
        ISolverEngine engine = new SolverDay12();
        assertEquals(scenario.expectedOutput(), engine.solvePart2(scenario.input()));
    }
}