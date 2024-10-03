# make            # Build all executables
# make day01      # Build the executable for day 1 and execute it
# make clean      # Remove all executables


CC = g++

# -Wall              # activate some waning flags
# -Wextra            # activate some additional warning flags
# -Werror            # treat all warnings as errors
# -Wsign-conversion  # check implicit signed/unsigned conversion
# -pedantic          # reject all compiler extensions (compiler-specific not in C++ standard)
# -Ixxx              # use xxx as a header folder
# -std=c++2a         # use C++20 standard
CFLAGS  = -W -Wall -Wextra -Werror -pedantic -Wsign-conversion -g -Icommon -std=c++2a
 
# The build targets are the executable for each day
TARGETS = bin/day01.bin \
          bin/day02.bin \
          bin/day03.bin \
          bin/day04.bin \
          bin/day05.bin \
		  bin/day06.bin \
		  bin/day07.bin \
		  bin/day08.bin \
		  bin/day09.bin \
		  bin/day10.bin \
		  bin/day11.bin \
		  bin/day12.bin \
		  bin/day13.bin \
		  bin/day14.bin \
		  bin/day15.bin \
		  bin/day16.bin \
		  bin/day17.bin \
		  bin/day18.bin \
		  bin/day19.bin \
		  bin/day20.bin \
		  bin/day21.bin \
		  bin/day22.bin \
		  bin/day23.bin \
		  bin/day24.bin \
		  bin/day25.bin

# When running "make", build the executable for each day
all: $(TARGETS)

# Artificial targets that always need to be re-executed when called
# When running "make day01" it will always execute that executable
.PHONY: day01 day02 day03 day04 day05 day06 day07 day08 day09 day10 day11 day12 day13 \
        day14 day15 day16 day17 day18 day19 day20 day21 day22 day23 day24 day25

day01: bin/day01.bin
	./$<

day02: bin/day02.bin
	./$<

day03: bin/day03.bin
	./$<

day04: bin/day04.bin
	./$<

day05: bin/day05.bin
	./$<

day06: bin/day06.bin
	./$<

day07: bin/day07.bin
	./$<

day08: bin/day08.bin
	./$<

day09: bin/day09.bin
	./$<

day10: bin/day10.bin
	./$<

day11: bin/day11.bin
	./$<

day12: bin/day12.bin
	./$<

day13: bin/day13.bin
	./$<

day14: bin/day14.bin
	./$<

day15: bin/day15.bin
	./$<

day16: bin/day16.bin
	./$<

day17: bin/day17.bin
	./$<

day18: bin/day18.bin
	./$<

day19: bin/day19.bin
	./$<

day20: bin/day20.bin
	./$<

day21: bin/day21.bin
	./$<

day22: bin/day22.bin
	./$<

day23: bin/day23.bin
	./$<

day24: bin/day24.bin
	./$<

day25: bin/day25.bin
	./$<

# Create the executable for a given day
bin/%.bin: %/part1.o %/part2.o %/main.o common/Utils.o common/md5.o
	$(CC) $(CFLAGS) -o $@ $^

# Create any .o file from its cpp file
%.o : %.cpp
	$(CC) $(CFLAGS) -o $@ -c $<

# explicitly mention the headers included so the .o are rebuilt if these header change
# here we only add some dependencies, the actual command to run is above in the wildcard
%/part1.o: %/part1.hpp common/utils.hpp
%/part2.o: %/part1.hpp %/part2.hpp common/Utils.hpp

clean:
	$(RM) bin/*