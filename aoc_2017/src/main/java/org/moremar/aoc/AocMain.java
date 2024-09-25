package org.moremar.aoc;

import org.moremar.aoc.common.AocException;
import org.moremar.aoc.solvers.Solver;

public class AocMain {
    public static void main(String[] args) {
        // run the AOC solver for each day
        try {
            for (int day = 1; day <= 12; ++day) {
                Solver solver = new Solver(day, AocMain.class.getClassLoader());
                solver.solve();
            }
        } catch (AocException e) {
            throw new RuntimeException(e);
        }
    }
}