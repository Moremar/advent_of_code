package org.moremar.aoc.common;

import java.util.Objects;

public record Coord3D(long x, long y, long z) {

    public Coord3D add(Coord3D c) {
        return new Coord3D(x + c.x, y + c.y, z + c.z);
    }

    public Coord3D subtract(Coord3D c) {
        return new Coord3D(x - c.x, y - c.y, z - c.z);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Coord3D coord3D = (Coord3D) o;
        return x == coord3D.x && y == coord3D.y && z == coord3D.z;
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y, z);
    }

    public long manhattan() {
        return Math.abs(x) + Math.abs(y) + Math.abs(z);
    }
}
