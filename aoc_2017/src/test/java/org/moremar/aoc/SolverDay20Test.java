package org.moremar.aoc;

import org.junit.jupiter.api.Test;
import org.moremar.aoc.common.AocException;
import org.moremar.aoc.solvers.ISolverEngine;
import org.moremar.aoc.solvers.SolverDay20;
import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SolverDay20Test {

    @Test
    void solvePart1() throws AocException {
        final String input = """
                p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>
                p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>
                """;
        AocScenario scenario = new AocScenario(Arrays.asList(input.split("\n")), "0");
        ISolverEngine engine = new SolverDay20();
        assertEquals(scenario.expectedOutput(), engine.solvePart1(scenario.input()));
    }

    @Test
    void solvePart2() throws AocException {
        final String input = """
                p=<-6,0,0>, v=<3,0,0>, a=<0,0,0>
                p=<-4,0,0>, v=<2,0,0>, a=<0,0,0>
                p=<-2,0,0>, v=<1,0,0>, a=<0,0,0>
                p=<3,0,0>, v=<-1,0,0>, a=<0,0,0>
                """;
        AocScenario scenario = new AocScenario(Arrays.asList(input.split("\n")), "1");
        ISolverEngine engine = new SolverDay20();
        assertEquals(scenario.expectedOutput(), engine.solvePart2(scenario.input()));
    }
}