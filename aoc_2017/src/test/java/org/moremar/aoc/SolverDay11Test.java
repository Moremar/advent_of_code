package org.moremar.aoc;

import org.junit.jupiter.api.Test;
import org.moremar.aoc.common.AocException;
import org.moremar.aoc.solvers.ISolverEngine;
import org.moremar.aoc.solvers.SolverDay11;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SolverDay11Test {

    @Test
    void solvePart1() throws AocException {
        List<AocScenario> scenarios = Arrays.asList(
                new AocScenario(List.of("ne,ne,ne"), "3"),
                new AocScenario(List.of("ne,ne,sw,sw"), "0"),
                new AocScenario(List.of("ne,ne,s,s"), "2"),
                new AocScenario(List.of("se,sw,se,sw,sw"), "3")
        );
        for (AocScenario scenario : scenarios) {
            ISolverEngine engine = new SolverDay11();
            assertEquals(scenario.expectedOutput(), engine.solvePart1(scenario.input()));
        }
    }

    @Test
    void solvePart2() throws AocException {
        List<AocScenario> scenarios = Arrays.asList(
                new AocScenario(List.of("ne,ne,ne"), "3"),
                new AocScenario(List.of("ne,ne,sw,sw"), "2"),
                new AocScenario(List.of("ne,ne,s,s"), "2"),
                new AocScenario(List.of("se,sw,se,sw,sw"), "3")
        );
        for (AocScenario scenario : scenarios) {
            ISolverEngine engine = new SolverDay11();
            assertEquals(scenario.expectedOutput(), engine.solvePart2(scenario.input()));
        }
    }
}