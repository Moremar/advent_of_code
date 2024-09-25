package org.moremar.aoc;

import org.junit.jupiter.api.Test;
import org.moremar.aoc.common.AocException;
import org.moremar.aoc.solvers.ISolverEngine;
import org.moremar.aoc.solvers.SolverDay14;
import java.util.List;
import static org.junit.jupiter.api.Assertions.assertEquals;

class SolverDay14Test {

    @Test
    void solvePart1() throws AocException {
        AocScenario scenario = new AocScenario(List.of("flqrgnkx"), "8108");
        ISolverEngine engine = new SolverDay14();
        assertEquals(scenario.expectedOutput(), engine.solvePart1(scenario.input()));
    }

    @Test
    void solvePart2() throws AocException {
        AocScenario scenario = new AocScenario(List.of("flqrgnkx"), "1242");
        ISolverEngine engine = new SolverDay14();
        assertEquals(scenario.expectedOutput(), engine.solvePart2(scenario.input()));
    }
}