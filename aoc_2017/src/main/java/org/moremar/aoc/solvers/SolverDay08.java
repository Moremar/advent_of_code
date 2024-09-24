package org.moremar.aoc.solvers;

import org.moremar.aoc.common.AocException;
import java.util.*;

public class SolverDay08 implements ISolverEngine {

    private record Instruction(String register, String operator, int value,
                               String condRegister, String condOperator, int condValue) {}


    public SolverDay08() {
        super();
    }

    @Override
    public String solvePart1(List<String> lines) throws AocException {
        final List<Instruction> instructions = parseInput(lines);
        Map<String, Integer> registers = new HashMap<>();
        for (Instruction instr : instructions) {
            executeInstruction(instr, registers);
        }
        OptionalInt maxValue = registers.values().stream().mapToInt(Integer::intValue).max();
        assert maxValue.isPresent();
        return String.valueOf(maxValue.getAsInt());
    }

    private void executeInstruction(Instruction instr, Map<String, Integer> registers) {
        // add the registers with default value 0 if they are not present
        if (!registers.containsKey(instr.register)) {
            registers.put(instr.register, 0);
        }
        if (!registers.containsKey(instr.condRegister)) {
            registers.put(instr.condRegister, 0);
        }
        // check the condition
        boolean condition = switch (instr.condOperator) {
            case ">" -> registers.get(instr.condRegister) > instr.condValue;
            case "<" -> registers.get(instr.condRegister) < instr.condValue;
            case ">=" -> registers.get(instr.condRegister) >= instr.condValue;
            case "<=" -> registers.get(instr.condRegister) <= instr.condValue;
            case "==" -> registers.get(instr.condRegister) == instr.condValue;
            case "!=" -> registers.get(instr.condRegister) != instr.condValue;
            default -> throw new IllegalArgumentException("Invalid operator: " + instr.condOperator);
        };
        // apply the operation if the condition is true
        if (condition) {
            switch (instr.operator) {
                case "inc" -> registers.put(instr.register, registers.get(instr.register) + instr.value);
                case "dec" -> registers.put(instr.register, registers.get(instr.register) - instr.value);
                default -> throw new IllegalArgumentException("Invalid operator: " + instr.operator);
            }
        }
    }

    @Override
    public String solvePart2(List<String> lines) {
        final List<Instruction> instructions = parseInput(lines);
        Map<String, Integer> registers = new HashMap<>();
        int maxRegister = 0;
        for (Instruction instr : instructions) {
            executeInstruction(instr, registers);
            OptionalInt maxValue = registers.values().stream().mapToInt(Integer::intValue).max();
            assert maxValue.isPresent();
            maxRegister = Integer.max(maxRegister, maxValue.getAsInt());
        }
        return String.valueOf(maxRegister);
    }

    private static List<Instruction> parseInput(List<String> lines) {
        List<Instruction> instructions = new ArrayList<>();
        for (String line : lines) {
            String[] parts = line.split(" ");
            instructions.add(new Instruction(parts[0], parts[1], Integer.parseInt(parts[2]),
                                             parts[4], parts[5], Integer.parseInt(parts[6])));
        }
        return instructions;
    }
}
