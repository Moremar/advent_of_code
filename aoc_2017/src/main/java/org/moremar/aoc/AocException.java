package org.moremar.aoc;

/**
 * Custom exception class used by all exceptions raised in the AOC solvers
 */
public class AocException extends Exception {
    AocException(String message) {
        super(message);
    }
}
