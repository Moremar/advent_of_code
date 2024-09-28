package org.moremar.aoc.solvers;

import org.moremar.aoc.common.AocException;

import java.util.*;

public class SolverDay23 implements ISolverEngine {

    private static class Program {
        private final List<String[]> myCommands;
        private final Map<String, Long> myRegisters = new HashMap<>();
        private int myPointer = 0;
        private int myMulCount = 0;
        private boolean myComplete = false;

        public Program(List<String[]> commands, boolean debug) {
            myCommands = commands;
            myRegisters.put("a", debug ? 0L : 1L);
            for (String register : List.of("b", "c", "d", "e", "f", "g", "h")) {
                myRegisters.put(register, 0L);
            }
        }

        public boolean isNotComplete() {
            return !myComplete;
        }

        public int getMulCount() {
            return myMulCount;
        }

        public void runNextInstruction() throws AocException {
            String[] command = myCommands.get(myPointer);
            switch (command[0]) {
                case "set":
                    myRegisters.put(command[1], resolve(command[2]));
                    break;
                case "sub":
                    myRegisters.put(command[1], myRegisters.getOrDefault(command[1], (long) 0)
                            - resolve(command[2]));
                    break;
                case "mul":
                    myRegisters.put(command[1], myRegisters.getOrDefault(command[1], (long) 0)
                            * resolve(command[2]));
                    ++myMulCount;
                    break;
                case "prm":
                    if (!isPrime(resolve(command[1]))) {
                        myRegisters.put(command[2], 0L);
                    }
                    break;
                case "jnz":
                    if (resolve(command[1]) != 0) {
                        myPointer += (int) resolve(command[2]) - 1;
                    }
                    break;
                default:
                    throw new AocException("Unknown command : " + command[0]);
            }
            ++myPointer;
            if (myPointer >= myCommands.size() || myPointer < 0) {
                myComplete = true;
            }
        }

        static boolean isPrime(long n) {
            if (n <= 1) return false;
            if (n == 2 || n == 3) return true;
            if (n % 2 == 0 || n % 3 == 0) return false;
            // check all other cases
            for (int i = 5; i <= Math.sqrt(n); i = i + 6) {
                if (n % i == 0 || n % (i + 2) == 0) return false;
            }
            return true;
        }

        private long resolve(String param) {
            if (param.charAt(0) >= 'a' && param.charAt(0) <= 'z') {
                return myRegisters.getOrDefault(param, (long) 0);
            } else {
                return Long.parseLong(param);
            }
        }
    }

    public SolverDay23() {
        super();
    }

    @Override
    public String solvePart1(List<String> lines) throws AocException {
        final List<String[]> commands = parseInput(lines);
        final Program program = new Program(commands, true);
        while (program.isNotComplete()) {
            program.runNextInstruction();
        }
        return String.valueOf(program.getMulCount());
    }

    /*
     * For this part 2, the program runs for a very long time in a triple nested loop.
     * We need to analyze the behavior of the instructions to understand what it does.
     * The 2 inner nested loops make variables e and d loop from 2 to (b-1),
     * which is very big in part 2.
     * For each combination of e and d, it checks if b = e * d, and sets f to 0 if it is.
     * It is basically looking for a pair of divisors of b different from (1, b).
     * At the end of this double loop, f will be 1 if b is prime, and 0 otherwise.
     *
     * To solve this problem, we create a "prm X Y" instruction that sets Y to 0
     * only when X is not prime.
     * Then we replace the double nested loop :
     *
     *      set d 2
     *      set e 2
     *      set g d
     *      mul g e
     *      sub g b
     *      jnz g 2
     *      set f 0
     *      sub e -1
     *      set g e
     *      sub g b
     *      jnz g -8
     *      sub d -1
     *      set g d
     *      sub g b
     *      jnz g -13
     *
     * by the prm instruction : prm b f
     */
    @Override
    public String solvePart2(List<String> lines) throws AocException {
        final List<String[]> commands = parseInput(lines);
        // replace the inner 2 nested loops by the prm instruction, and update
        // the jump value in the last instruction accordingly
        final List<String[]> improvedCommands = new ArrayList<>(commands.subList(0, 9));
        improvedCommands.add(new String[]{ "prm", "b", "f" });
        improvedCommands.addAll(commands.subList(24, 31));
        improvedCommands.add(new String[]{ "jnz", "1", "-9" });

        final Program program = new Program(improvedCommands, false);
        while (program.isNotComplete()) {
            program.runNextInstruction();
        }
        return String.valueOf(program.myRegisters.get("h"));
    }

    /**
     * Parse the input lines
     */
    public List<String[]> parseInput(List<String> lines) throws AocException {
        return lines.stream().map(s -> s.split(" ")).toList();
    }
}