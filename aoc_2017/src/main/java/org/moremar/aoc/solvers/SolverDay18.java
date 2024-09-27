package org.moremar.aoc.solvers;

import org.moremar.aoc.common.AocException;
import java.util.*;

public class SolverDay18 implements ISolverEngine {

    private static class Program {

        private final int myVersion;
        private final List<String[]> myCommands;
        private final Map<String, Long> myRegisters = new HashMap<>();
        private int myPointer = 0;
        private final Deque<Long> myInQueue = new LinkedList<>();
        private Deque<Long> myOutQueue = new LinkedList<>();
        private int mySentCount = 0;
        private boolean myComplete = false;
        private boolean myPaused = false;

        public Program(long id, int version, List<String[]> commands) {
            myVersion = version;
            myCommands = commands;
            myRegisters.put("p", id);
        }

        public boolean canRun() {
            return !myComplete && !(myPaused && myInQueue.isEmpty());
        }

        public int getSentCount() {
            return mySentCount;
        }

        public void setOutQueue(Deque<Long> outQueue) {
            myOutQueue = outQueue;
        }

        public Deque<Long> getInQueue() {
            return myInQueue;
        }

        public void runNextInstruction() throws AocException {
            if (myComplete) {
                throw new AocException("Cannot run an instruction on a complete program");
            }
            String[] command = myCommands.get(myPointer);
            switch (command[0]) {
                case "snd" :
                    myOutQueue.add(resolve(command[1]));
                    ++mySentCount;
                    break;
                case "set":
                    myRegisters.put(command[1], resolve(command[2]));
                    break;
                case "add":
                    myRegisters.put(command[1], myRegisters.getOrDefault(command[1], (long) 0)
                                            + resolve(command[2]));
                    break;
                case "mul":
                    myRegisters.put(command[1], myRegisters.getOrDefault(command[1], (long) 0)
                                            * resolve(command[2]));
                    break;
                case "mod":
                    myRegisters.put(command[1], myRegisters.getOrDefault(command[1], (long) 0)
                                            % resolve(command[2]));
                    break;
                case "rcv":
                    if (myVersion == 1) {  // part 1
                        if (resolve(command[1]) != 0) {
                            if (myOutQueue.isEmpty()) {
                                throw new AocException("No message to poll in the output queue");
                            }
                            myInQueue.add(myOutQueue.pollLast());
                            myComplete = true;
                        }
                    } else {  // part 2
                        if (myInQueue.isEmpty()) {
                            // need an input from the other program, pause here
                            myPaused = true;
                            return; // return to not increment the pointer
                        } else {
                            // an input is available from the other program
                            myPaused = false;
                            myRegisters.put(command[1], myInQueue.pollFirst());
                        }
                    }
                    break;
                case "jgz":
                    if (resolve(command[1]) > 0) {
                        myPointer += (int) resolve(command[2]) - 1;
                    }
                    break;
                default:
                    throw new AocException("Unknown command : " + command[0]);
            }
            if (++myPointer >= myCommands.size()) {
                myComplete = true;
            }
        }

        private long resolve(String param) {
            if (param.charAt(0) >= 'a' && param.charAt(0) <= 'z') {
                return myRegisters.getOrDefault(param, (long) 0);
            } else {
                return Long.parseLong(param);
            }
        }
    }

    public SolverDay18() {
        super();
    }

    @Override
    public String solvePart1(List<String> lines) throws AocException {
        final List<String[]> commands = parseInput(lines);
        final Program program = new Program(0, 1, commands);
        while (program.canRun()) {
            program.runNextInstruction();
        }
        return String.valueOf(program.getInQueue().getFirst());
    }

    @Override
    public String solvePart2(List<String> lines) throws AocException {
        final List<String[]> commands = parseInput(lines);
        final Program program0 = new Program(0, 2, commands);
        final Program program1 = new Program(1, 2, commands);
        program0.setOutQueue(program1.getInQueue());
        program1.setOutQueue(program0.getInQueue());
        while (program0.canRun() || program1.canRun()) {
            // run program as much as possible
            while (program0.canRun()) {
                program0.runNextInstruction();
            }
            // run program 1 as much as possible
            while (program1.canRun()) {
                program1.runNextInstruction();
            }
        }
        return String.valueOf(program1.getSentCount());
    }

    /**
     * Parse the input lines
     */
    public List<String[]> parseInput(List<String> lines) throws AocException {
        return lines.stream().map(s -> s.split(" ")).toList();
    }
}