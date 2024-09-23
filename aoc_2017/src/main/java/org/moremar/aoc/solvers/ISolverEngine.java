package org.moremar.aoc.solvers;

import org.moremar.aoc.common.AocException;

import java.util.List;

/**
 * Interface for a solver engine that can solve a specific day's puzzle.
 * There is an implementation for each day of the AOC event.
 */
public interface ISolverEngine {

    /**
     * Get the solution of the puzzle's part 1
     */
    String solvePart1(List<String> lines) throws AocException;

    /**
     * Get the solution of the puzzle's part 2
     */
    String solvePart2(List<String> lines) throws AocException;
}
