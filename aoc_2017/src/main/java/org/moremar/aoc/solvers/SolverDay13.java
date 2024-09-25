package org.moremar.aoc.solvers;

import org.moremar.aoc.common.AocException;
import java.util.*;

public class SolverDay13 implements ISolverEngine {

    private record Layer(int depth, int range){}

    public SolverDay13() {
        super();
    }

    @Override
    public String solvePart1(List<String> lines) throws AocException {
        final List<Layer> layers = parseInput(lines);
        return String.valueOf(getSeverity(layers, 0));
    }

    private int getSeverity(List<Layer> layers, int delay) {
        int severity = -1;
        for (Layer layer : layers) {
            // each scanner reaches the top-level periodically
            final int period = 2 * (layer.range - 1);
            if ((layer.depth + delay) % period == 0) {
                // mark the severity as 0, to distinguish the case with no impact (-1)
                // and the case with an impact with severity 0
                if (severity == -1) {
                    severity = 0;
                }
                severity += layer.depth * layer.range;
            }
        }
        return severity;
    }

    @Override
    public String solvePart2(List<String> lines) throws AocException {
        List<Layer> layers = parseInput(lines);
        int delay = 1;
        while (getSeverity(layers, delay) >= 0) {
            ++delay;
        }
        return String.valueOf(delay);
    }

    /**
     * Parse the input lines into layers details
     */
    private List<Layer> parseInput(List<String> lines) throws AocException {
        final List<Layer> layers = new ArrayList<>();
        for (String line : lines) {
            String[] params = line.split(": ");
            layers.add(new Layer(Integer.parseInt(params[0]), Integer.parseInt(params[1])));
        }
        return layers;
    }
}
