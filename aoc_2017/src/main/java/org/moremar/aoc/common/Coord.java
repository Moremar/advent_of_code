package org.moremar.aoc.common;

import java.util.Arrays;
import java.util.List;
import java.util.Objects;

public record Coord(int x, int y) {

    public static final Coord UP = new Coord(0, 1);
    public static final Coord RIGHT = new Coord(1, 0);
    public static final Coord DOWN = new Coord(0, -1);
    public static final Coord LEFT = new Coord(-1, 0);

    private static final List<Coord> DIRECTIONS = Arrays.asList(UP, RIGHT, DOWN, LEFT);

    public Coord add(Coord c) {
        return new Coord(x + c.x, y + c.y);
    }

    public Coord subtract(Coord c) {
        return new Coord(x - c.x, y - c.y);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Coord coord = (Coord) o;
        return x == coord.x && y == coord.y;
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y);
    }

    /**
     * Get the 4 adjacent coordinates (excluding diagonals)
     */
    public List<Coord> adjacent4() {
        return Arrays.asList(add(UP), add(DOWN), add(LEFT), add(RIGHT));
    }

    /**
     * Get the 8 adjacent coordinates (including diagonals)
     */
    public List<Coord> adjacent8() {
        return Arrays.asList(
            add(UP), add(DOWN), add(LEFT), add(RIGHT),
            add(UP.add(LEFT)), add(UP.add(RIGHT)), add(DOWN.add(LEFT)), add(DOWN.add(RIGHT)));
    }

    public Coord turnRight() throws AocException {
        if (!DIRECTIONS.contains(this)) {
            throw new AocException("Can only be called on a direction");
        }
        return DIRECTIONS.get((DIRECTIONS.indexOf(this) + 1) % 4);
    }

    public Coord turnLeft() throws AocException {
        if (!DIRECTIONS.contains(this)) {
            throw new AocException("Can only be called on a direction");
        }
        return DIRECTIONS.get((DIRECTIONS.indexOf(this) + 3) % 4);
    }
}
