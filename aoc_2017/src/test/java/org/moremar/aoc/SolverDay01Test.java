package org.moremar.aoc;

import org.junit.jupiter.api.Test;
import org.moremar.aoc.common.AocException;
import org.moremar.aoc.solvers.ISolverEngine;
import org.moremar.aoc.solvers.SolverDay01;

import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class SolverDay01Test {

    @Test
    void solvePart1() throws AocException {
        List<AocScenario> scenarios = Arrays.asList(
                new AocScenario(List.of("1122"), "3"),
                new AocScenario(List.of("1111"), "4"),
                new AocScenario(List.of("1234"), "0"),
                new AocScenario(List.of("91212129"), "9")
        );
        for (AocScenario scenario : scenarios) {
            ISolverEngine engine = new SolverDay01();
            assertEquals(scenario.expectedOutput(), engine.solvePart1(scenario.input()));
        }
    }

    @Test
    void solvePart2() throws AocException {
        List<AocScenario> scenarios = Arrays.asList(
                new AocScenario(List.of("1212"), "6"),
                new AocScenario(List.of("1221"), "0"),
                new AocScenario(List.of("123425"), "4"),
                new AocScenario(List.of("123123"), "12"),
                new AocScenario(List.of("12131415"), "4")
        );
        for (AocScenario scenario : scenarios) {
            ISolverEngine engine = new SolverDay01();
            assertEquals(scenario.expectedOutput(), engine.solvePart2(scenario.input()));
        }
    }
}