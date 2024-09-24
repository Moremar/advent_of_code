package org.moremar.aoc;

import org.junit.jupiter.api.Test;
import org.moremar.aoc.common.AocException;
import org.moremar.aoc.solvers.ISolverEngine;
import org.moremar.aoc.solvers.SolverDay10;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SolverDay10Test {

    @Test
    void solvePart1() throws AocException {
        SolverDay10 engine = new SolverDay10();
        int[] nodes = { 0, 1, 2, 3, 4};
        int[] lengths = { 3, 4, 1, 5 };
        var state = engine.applyRound(nodes, lengths, new SolverDay10.State(0, 0));
        assertEquals(4, state.position());
        assertEquals(4, state.skipSize());
        assertEquals(3, nodes[0]);
        assertEquals(4, nodes[1]);
    }

    @Test
    void solvePart2() throws AocException {
        List<AocScenario> scenarios = Arrays.asList(
                new AocScenario(List.of(""), "a2582a3a0e66e6e86e3812dcb672a272"),
                new AocScenario(List.of("AoC 2017"), "33efeb34ea91902bb2f59c9920caa6cd"),
                new AocScenario(List.of("1,2,3"), "3efbe78a8d82f29979031a4aa0b16a9d"),
                new AocScenario(List.of("1,2,4"), "63960835bcdc130f0b66d7ff4f6a5a8e")
        );
        for (AocScenario scenario : scenarios) {
            ISolverEngine engine = new SolverDay10();
            assertEquals(scenario.expectedOutput(), engine.solvePart2(scenario.input()));
        }
    }
}