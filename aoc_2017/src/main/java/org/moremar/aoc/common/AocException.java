package org.moremar.aoc.common;

/**
 * Custom exception class used by all exceptions raised in the AOC solvers
 */
public class AocException extends Exception {
    public AocException(String message) {
        super(message);
    }
}
