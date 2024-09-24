package org.moremar.aoc.solvers;

import org.moremar.aoc.common.AocException;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.List;

/**
 * Solver for a given day of the AOC event.
 * It parses the input file into lines, and delegates the solving to the right engine
 * for the day being solved.
 */
public class Solver {

    private final int myDay;
    private final ClassLoader myClassLoader;

    public Solver(int day, ClassLoader classLoader) {
        myDay = day;
        myClassLoader = classLoader;
    }

    /**
     * Get the list of lines in the input file for this day's puzzle
     */
    private List<String> getInputLines() throws AocException {
        final String inputFilePath = "input/day" + (myDay < 10 ? "0" : "") + myDay + ".txt";
        InputStream inputStream = myClassLoader.getResourceAsStream(inputFilePath);
        if (inputStream == null) {
            throw new AocException("Cannot find input file " + inputFilePath);
        }
        return new BufferedReader(new InputStreamReader(inputStream)).lines().toList();
    }

    /**
     * Compute the solution of both parts of this day's puzzle and print them on the screen
     */
    public void solve() throws AocException {
        final ISolverEngine solverEngine = getSolverEngine();
        final List<String> lines = getInputLines();
        System.out.println("Day " + myDay + ": "
                          + solverEngine.solvePart1(lines) + " | "
                          + solverEngine.solvePart2(lines));
    }

    /**
     * Get the engine implementation for this day's puzzle
     */
    private ISolverEngine getSolverEngine() throws AocException {
        return switch (myDay) {
            case 1 -> new SolverDay01();
            case 2 -> new SolverDay02();
            case 3 -> new SolverDay03();
            case 4 -> new SolverDay04();
            case 5 -> new SolverDay05();
            case 6 -> new SolverDay06();
            case 7 -> new SolverDay07();
            case 8 -> new SolverDay08();
            case 9 -> new SolverDay09();
            case 10 -> new SolverDay10();
            default -> throw new AocException("No solver implementation for day " + myDay);
        };
    }
}
