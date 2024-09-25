package org.moremar.aoc.solvers;

import org.moremar.aoc.common.AocException;
import org.moremar.aoc.common.Coord;
import java.util.*;

public class SolverDay14 implements ISolverEngine {

    private record Layer(int depth, int range){}

    public SolverDay14() {
        super();
    }

    @Override
    public String solvePart1(List<String> lines) throws AocException {
        final String keyString = lines.getFirst();
        int usedSquaresCount = 0;
        for (int i = 0; i < 128; ++i) {
            final String knotHash = SolverDay10.getKnotHash(keyString + "-" + i);
            usedSquaresCount += toBinary(knotHash).replace("0", "").length();
        }
        return String.valueOf(usedSquaresCount);
    }

    private String toBinary(String hexStr) {
        StringBuilder stringBuilder = new StringBuilder();
        for (char c : hexStr.toCharArray()) {
            final int hex = Integer.parseInt(String.valueOf(c), 16);
            final String binStr = String.format("%4s", Integer.toBinaryString(hex))
                                  .replace(' ', '0');
            stringBuilder.append(binStr);
        }
        return stringBuilder.toString();
    }

    @Override
    public String solvePart2(List<String> lines) throws AocException {
        Map<Coord, Integer> disk = new HashMap<>();
        // build the disk
        final String keyString = lines.getFirst();
        for (int i = 0; i < 128; ++i) {
            final String knotHash = SolverDay10.getKnotHash(keyString + "-" + i);
            final String binHash = toBinary(knotHash);
            for (int j = 0; j < 128; ++j) {
                disk.put(new Coord(i, j), Integer.parseInt(String.valueOf(binHash.charAt(j))));
            }
        }
        // count the regions in the disk (by erasing them one by one)
        int regionsCount = 0;
        for (int i = 0; i < 128; ++i) {
            for (int j = 0; j < 128; ++j) {
                final Coord coord = new Coord(i, j);
                if (disk.get(coord) == 1) {
                    ++regionsCount;
                    cleanDiskRegion(disk, coord);
                }
            }
        }
        return String.valueOf(regionsCount);
    }

    private void cleanDiskRegion(Map<Coord, Integer> disk, Coord rootCoord) throws AocException {
        if (disk.get(rootCoord) == 0) {
            throw new AocException("No data to clean on disk at position : " + rootCoord);
        }
        final Deque<Coord> toClean = new LinkedList<>();
        toClean.add(rootCoord);
        while (!toClean.isEmpty()) {
            final Coord coord = toClean.poll();
            if (disk.containsKey(coord) && disk.get(coord) == 1) {
                disk.put(coord, 0);
                toClean.addAll(coord.adjacent4());
            }
        }
    }
}
