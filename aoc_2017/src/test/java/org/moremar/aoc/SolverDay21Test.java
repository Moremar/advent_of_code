package org.moremar.aoc;

import org.junit.jupiter.api.Test;
import org.moremar.aoc.common.AocException;
import org.moremar.aoc.solvers.SolverDay21;
import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SolverDay21Test {

    static final String INPUT = """
        ../.# => ##./#../...
        .#./..#/### => #..#/..../..../#..#
        """;

    @Test
    void solvePart1() throws AocException {
        SolverDay21 engine = new SolverDay21();
        var rules = engine.parseInput(Arrays.asList(INPUT.split("\n")));
        String[] world = { ".#.", "..#", "###" };
        int lightsOn = engine.transform(world, rules, 2);
        assertEquals(12, lightsOn);
    }

    // part 2 uses the same function as part 1
}