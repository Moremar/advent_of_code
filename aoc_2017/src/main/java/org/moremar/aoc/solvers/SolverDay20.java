package org.moremar.aoc.solvers;

import org.moremar.aoc.common.AocException;
import org.moremar.aoc.common.Coord3D;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class SolverDay20 implements ISolverEngine {

    private static class Particle {
        public int id;
        public Coord3D p;
        public Coord3D v;
        public Coord3D a;

        public Particle(int id, Coord3D p, Coord3D v, Coord3D a) {
            this.id = id;
            this.p = p;
            this.v = v;
            this.a = a;
        }
    }

    public SolverDay20() {
        super();
    }

    @Override
    public String solvePart1(List<String> lines) throws AocException {
        List<Particle> particles = parseInput(lines);

        // The acceleration is the main factor deciding how fast particles
        // move away from the origin, so we find the one with the smallest manhattan distance
        // the input file has only one particle with the smallest acceleration vector (it actually
        // has a null acceleration <0, 0, 0> so no need to implement a logic to compare multiple particles
        int bestParticleId = particles.size() - 1;
        long bestManhattan = particles.getLast().a.manhattan();
        for (Particle particle : particles) {
            if (particle.a.manhattan() <= bestManhattan) {
                bestParticleId = particle.id;
                bestManhattan = particle.a.manhattan();
            }
        }

        return String.valueOf(bestParticleId);
    }

    @Override
    public String solvePart2(List<String> lines) throws AocException {
        List<Particle> particles = parseInput(lines);

        // we run a few rounds and keep track of each particle that exploded.
        // I ran the simulation on 1'000'000 ticks, but actually we already get the
        // correct result after a few dozens ticks (in my case, the last explosions occur on tick 39)
        Set<Integer> exploded = new HashSet<>();
        for (int tick = 1; tick < 1000; ++tick) {
            final Map<Coord3D, Integer> particleLocations = new HashMap<>();
            for (Particle particle : particles) {
                if (exploded.contains(particle.id)) {
                    continue;
                }
                particle.v = particle.v.add(particle.a);
                particle.p = particle.p.add(particle.v);
                if (particleLocations.containsKey(particle.p)) {
                    // another particle is at the same location, they both explode !
                    exploded.add(particle.id);
                    exploded.add(particleLocations.get(particle.p));
                } else {
                    particleLocations.put(particle.p, particle.id);
                }
            }
        }
        return String.valueOf(particles.size() - exploded.size());
    }

    /**
     * Parse the input lines
     */
    private List<Particle> parseInput(List<String> lines) throws AocException {
        List<Particle> particles = new LinkedList<>();
        Pattern pattern = Pattern.compile("p=<(-?\\d+),(-?\\d+),(-?\\d+)>, "
                                              + "v=<(-?\\d+),(-?\\d+),(-?\\d+)>, "
                                              + "a=<(-?\\d+),(-?\\d+),(-?\\d+)>");
        int particleId = 0;
        for (String line : lines) {
            final Matcher matcher = pattern.matcher(line);
            if (!matcher.matches()) {
                throw new AocException("Could not parse line : " + line);
            }
            final Coord3D position = new Coord3D(
                    Integer.parseInt(matcher.group(1)),
                    Integer.parseInt(matcher.group(2)),
                    Integer.parseInt(matcher.group(3)));
            final Coord3D velocity = new Coord3D(
                    Integer.parseInt(matcher.group(4)),
                    Integer.parseInt(matcher.group(5)),
                    Integer.parseInt(matcher.group(6)));
            final Coord3D acceleration = new Coord3D(
                    Integer.parseInt(matcher.group(7)),
                    Integer.parseInt(matcher.group(8)),
                    Integer.parseInt(matcher.group(9)));
            particles.add(new Particle(particleId++, position, velocity, acceleration));
        }
        return particles;
    }
}