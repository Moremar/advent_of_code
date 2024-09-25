package org.moremar.aoc;

import org.junit.jupiter.api.Test;
import org.moremar.aoc.common.AocException;
import org.moremar.aoc.solvers.SolverDay16;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SolverDay16Test {

    @Test
    void solvePart1() throws AocException {
        SolverDay16 engine = new SolverDay16();
        List<SolverDay16.DanceMove> danceMoves = engine.parseInput(List.of("s1,x3/4,pe/b"));
        var state = engine.getStateAfterOneDance(danceMoves, 5);
        assertEquals("baedc", state);
    }

    @Test
    void solvePart2() throws AocException {
        SolverDay16 engine = new SolverDay16();
        List<SolverDay16.DanceMove> danceMoves = engine.parseInput(List.of("s1,x3/4,pe/b"));
        var state = engine.getStateAfterMultipleDances(danceMoves, 5, 2);
        assertEquals("ceadb", state);
    }
}