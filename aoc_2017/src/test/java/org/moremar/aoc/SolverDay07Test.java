package org.moremar.aoc;

import org.junit.jupiter.api.Test;
import org.moremar.aoc.common.AocException;
import org.moremar.aoc.solvers.ISolverEngine;
import org.moremar.aoc.solvers.SolverDay07;
import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SolverDay07Test {

    String INPUT = """
            pbga (66)
            xhth (57)
            ebii (61)
            havc (66)
            ktlj (57)
            fwft (72) -> ktlj, cntj, xhth
            qoyq (66)
            padx (45) -> pbga, havc, qoyq
            tknk (41) -> ugml, padx, fwft
            jptl (61)
            ugml (68) -> gyxo, ebii, jptl
            gyxo (61)
            cntj (57)
            """;

    @Test
    void solvePart1() throws AocException {
        AocScenario scenario = new AocScenario(Arrays.asList(INPUT.split("\n")), "tknk");
        ISolverEngine engine = new SolverDay07();
        assertEquals(scenario.expectedOutput(), engine.solvePart1(scenario.input()));
    }

    @Test
    void solvePart2() throws AocException {
        AocScenario scenario = new AocScenario(Arrays.asList(INPUT.split("\n")), "60");
        ISolverEngine engine = new SolverDay07();
        assertEquals(scenario.expectedOutput(), engine.solvePart2(scenario.input()));
    }
}