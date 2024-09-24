package org.moremar.aoc;

import org.junit.jupiter.api.Test;
import org.moremar.aoc.common.AocException;
import org.moremar.aoc.solvers.ISolverEngine;
import org.moremar.aoc.solvers.SolverDay09;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SolverDay09Test {

    @Test
    void solvePart1() throws AocException {
        List<AocScenario> scenarios = Arrays.asList(
                new AocScenario(List.of("{}"), "1"),
                new AocScenario(List.of("{{{}}}"), "6"),
                new AocScenario(List.of("{{},{}}"), "5"),
                new AocScenario(List.of("{{{},{},{{}}}}"), "16"),
                new AocScenario(List.of("{<a>,<a>,<a>,<a>}"), "1"),
                new AocScenario(List.of("{{<ab>},{<ab>},{<ab>},{<ab>}}"), "9"),
                new AocScenario(List.of("{{<!!>},{<!!>},{<!!>},{<!!>}}"), "9"),
                new AocScenario(List.of("{{<a!>},{<a!>},{<a!>},{<ab>}}"), "3")
        );
        for (AocScenario scenario : scenarios) {
            ISolverEngine engine = new SolverDay09();
            assertEquals(scenario.expectedOutput(), engine.solvePart1(scenario.input()));
        }
    }

    @Test
    void solvePart2() throws AocException {
        List<AocScenario> scenarios = Arrays.asList(
                new AocScenario(List.of("<>"), "0"),
                new AocScenario(List.of("<random characters>"), "17"),
                new AocScenario(List.of("<<<<>"), "3"),
                new AocScenario(List.of("<{!>}>"), "2"),
                new AocScenario(List.of("<!!>"), "0"),
                new AocScenario(List.of("<!!!>>"), "0"),
                new AocScenario(List.of("<{o\"i!a,<{i<a>"), "10")
        );
        for (AocScenario scenario : scenarios) {
            ISolverEngine engine = new SolverDay09();
            assertEquals(scenario.expectedOutput(), engine.solvePart2(scenario.input()));
        }
    }
}