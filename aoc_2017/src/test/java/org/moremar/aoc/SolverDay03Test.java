package org.moremar.aoc;

import org.junit.jupiter.api.Test;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SolverDay03Test {

    @Test
    void solvePart1() throws AocException {
        List<AocScenario> scenarios = Arrays.asList(
                new AocScenario(List.of("12"), "3"),
                new AocScenario(List.of("23"), "2"),
                new AocScenario(List.of("1024"), "31")
        );
        for (AocScenario scenario : scenarios) {
            ISolverEngine engine = new SolverDay03();
            assertEquals(scenario.expectedOutput(), engine.solvePart1(scenario.input()));
        }
    }

    @Test
    void solvePart2() throws AocException {
        List<AocScenario> scenarios = Arrays.asList(
                new AocScenario(List.of("50"), "54"),
                new AocScenario(List.of("700"), "747"),
                new AocScenario(List.of("800"), "806")
        );
        for (AocScenario scenario : scenarios) {
            ISolverEngine engine = new SolverDay03();
            assertEquals(scenario.expectedOutput(), engine.solvePart2(scenario.input()));
        }
    }
}