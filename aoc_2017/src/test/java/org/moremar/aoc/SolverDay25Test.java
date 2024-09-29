package org.moremar.aoc;

import org.junit.jupiter.api.Test;
import org.moremar.aoc.common.AocException;
import org.moremar.aoc.solvers.ISolverEngine;
import org.moremar.aoc.solvers.SolverDay25;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SolverDay25Test {

    static final String INPUT = """
            Begin in state A.
            Perform a diagnostic checksum after 6 steps.
            
            In state A:
              If the current value is 0:
                - Write the value 1.
                - Move one slot to the right.
                - Continue with state B.
              If the current value is 1:
                - Write the value 0.
                - Move one slot to the left.
                - Continue with state B.
           
            In state B:
              If the current value is 0:
                - Write the value 1.
                - Move one slot to the left.
                - Continue with state A.
              If the current value is 1:
                - Write the value 1.
                - Move one slot to the right.
                - Continue with state A.
            """;

    @Test
    void solvePart1() throws AocException {
        AocScenario scenario = new AocScenario(List.of(INPUT.split("\n")), "3");
        ISolverEngine engine = new SolverDay25();
        assertEquals(scenario.expectedOutput(), engine.solvePart1(scenario.input()));
    }
}