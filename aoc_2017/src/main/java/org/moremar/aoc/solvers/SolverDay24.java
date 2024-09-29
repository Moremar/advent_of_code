package org.moremar.aoc.solvers;

import org.moremar.aoc.common.AocException;
import java.util.*;

public class SolverDay24 implements ISolverEngine {

    private static class Component {

        public int id;
        public List<Integer> ports;
        public int strength;

        public Component(int id, List<Integer> ports) {
            this.id = id;
            this.ports = ports;
            this.strength = ports.stream().reduce(0, Integer::sum);
        }
    }

    private static class Bridge {

        public int port = 0;
        public int strength = 0;
        public List<Integer> components = new LinkedList<>();

        public Bridge(){}

        public Bridge(List<Integer> components, int port, int strength) {
            this.components = components;
            this.port = port;
            this.strength = strength;
        }

        protected Bridge extend(Component component) {
            if (!component.ports.contains(port) || components.contains(component.id)) {
                return null;
            }
            List<Integer> extendedComponents = new LinkedList<>(components);
            extendedComponents.add(component.id);
            int nextPort = component.ports.get(0) == port ? component.ports.get(1) : component.ports.get(0);
            return new Bridge(extendedComponents, nextPort, strength + component.strength);
        }
    }

    public SolverDay24() {
        super();
    }

    @Override
    public String solvePart1(List<String> lines) throws AocException {
        final List<Component> components = parseInput(lines);
        final Deque<Bridge> toCheck = new LinkedList<>();
        toCheck.add(new Bridge());
        int maxStrength = 0;
        while (!toCheck.isEmpty()) {
            final Bridge currBridge = toCheck.pollFirst();
            for (Component component : components) {
                final Bridge extendedBridge = currBridge.extend(component);
                if (extendedBridge != null) {
                    maxStrength = Math.max(maxStrength, extendedBridge.strength);
                    toCheck.add(extendedBridge);
                }
            }
        }
        return String.valueOf(maxStrength);
    }

    @Override
    public String solvePart2(List<String> lines) throws AocException {
        final List<Component> components = parseInput(lines);
        final Deque<Bridge> toCheck = new LinkedList<>();
        toCheck.add(new Bridge());
        int maxStrength = 0;
        int maxLength = 0;
        while (!toCheck.isEmpty()) {
            final Bridge currBridge = toCheck.pollFirst();
            for (Component component : components) {
                final Bridge extendedBridge = currBridge.extend(component);
                if (extendedBridge != null) {
                    if (extendedBridge.components.size() > maxLength) {
                        maxLength = extendedBridge.components.size();
                        maxStrength = extendedBridge.strength;
                    } else if (extendedBridge.components.size() == maxLength) {
                        maxStrength = Math.max(maxStrength, extendedBridge.strength);
                    }
                    toCheck.add(extendedBridge);
                }
            }
        }
        return String.valueOf(maxStrength);
    }

    /**
     * Parse the input lines
     */
    private List<Component> parseInput(List<String> lines) {
        List<Component> components = new ArrayList<>();
        for (int i = 0; i < lines.size(); ++i) {
            String[] portsStr = lines.get(i).split("/");
            components.add(new Component(i,
                    List.of(Integer.parseInt(portsStr[0]), Integer.parseInt(portsStr[1]))
            ));
        }
        return components;
    }
}