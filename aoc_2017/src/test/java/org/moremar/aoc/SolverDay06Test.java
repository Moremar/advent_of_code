package org.moremar.aoc;

import org.junit.jupiter.api.Test;
import org.moremar.aoc.common.AocException;
import org.moremar.aoc.solvers.ISolverEngine;
import org.moremar.aoc.solvers.SolverDay06;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SolverDay06Test {

    @Test
    void solvePart1() throws AocException {
        AocScenario scenario = new AocScenario(List.of("0\t2\t7\t0"), "5");
        ISolverEngine engine = new SolverDay06();
        assertEquals(scenario.expectedOutput(), engine.solvePart1(scenario.input()));
    }

    @Test
    void solvePart2() throws AocException {
        AocScenario scenario = new AocScenario(List.of("0\t2\t7\t0"), "4");
        ISolverEngine engine = new SolverDay06();
        assertEquals(scenario.expectedOutput(), engine.solvePart2(scenario.input()));
    }
}