package org.moremar.aoc;

import org.junit.jupiter.api.Test;
import org.moremar.aoc.common.AocException;
import org.moremar.aoc.solvers.ISolverEngine;
import org.moremar.aoc.solvers.SolverDay18;
import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SolverDay18Test {

    @Test
    void solvePart1() throws AocException {
        final String input = """
                set a 1
                add a 2
                mul a a
                mod a 5
                snd a
                set a 0
                rcv a
                jgz a -1
                set a 1
                jgz a -2
                """;
        AocScenario scenario = new AocScenario(Arrays.asList(input.split("\n")), "4");
        ISolverEngine engine = new SolverDay18();
        assertEquals(scenario.expectedOutput(), engine.solvePart1(scenario.input()));
    }

    @Test
    void solvePart2() throws AocException {
        final String input = """
                snd 1
                snd 2
                snd p
                rcv a
                rcv b
                rcv c
                rcv d
                """;
        AocScenario scenario = new AocScenario(Arrays.asList(input.split("\n")), "3");
        ISolverEngine engine = new SolverDay18();
        assertEquals(scenario.expectedOutput(), engine.solvePart2(scenario.input()));
    }
}