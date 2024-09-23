package org.moremar.aoc;

import java.util.stream.IntStream;
import java.util.stream.Stream;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class AocMain {
    public static void main(String[] args) {
        try {
            for (int day = 1; day <= 3; ++day) {
                Solver solver = new Solver(day);
                solver.solve();
            }
        } catch (AocException e) {
            throw new RuntimeException(e);
        }
    }
}