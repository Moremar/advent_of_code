package org.moremar.aoc.common;

import java.util.Arrays;
import java.util.List;

public record Coord(int x, int y) {

    public static final Coord UP = new Coord(0, 1);
    public static final Coord DOWN = new Coord(0, -1);
    public static final Coord LEFT = new Coord(-1, 0);
    public static final Coord RIGHT = new Coord(1, 0);

    public Coord add(Coord c) {
        return new Coord(x + c.x, y + c.y);
    }

    /**
     * Get the 8 adjacent coordinates (including diagonals)
     */
    public List<Coord> adjacent8() {
        return Arrays.asList(
            add(UP), add(DOWN), add(LEFT), add(RIGHT),
            add(UP.add(LEFT)), add(UP.add(RIGHT)), add(DOWN.add(LEFT)), add(DOWN.add(RIGHT)));
    }
}
