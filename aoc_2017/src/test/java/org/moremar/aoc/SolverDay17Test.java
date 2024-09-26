package org.moremar.aoc;

import org.junit.jupiter.api.Test;
import org.moremar.aoc.common.AocException;
import org.moremar.aoc.solvers.ISolverEngine;
import org.moremar.aoc.solvers.SolverDay17;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SolverDay17Test {

    @Test
    void solvePart1() throws AocException {
        AocScenario scenario = new AocScenario(List.of("3"), "638");
        ISolverEngine engine = new SolverDay17();
        assertEquals(scenario.expectedOutput(), engine.solvePart1(scenario.input()));
    }

    // no example provided in the question for part 2
}