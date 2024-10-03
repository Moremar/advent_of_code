# Advent of Code 2016
C++ solutions to Advent of Code 2016 puzzles :
https://adventofcode.com/2016/

# Build using the Makefile

```
make          # create the executable for each day
make day01    # create and execute the executable for a given day
make clean    # remove all executables
```

# Old structure using XCode

The code was originally organized with a XCode structure so it can be built and executed from XCode.  
The structure was updated to use a Makefile instead, so it is lighter and no longer relies on XCode.  
This section is just kept here only as a memo to know how to use setup a C++ project to build with XCode.

### XCode tree structure
 - each day is a folder with a subfolder for each part.
 - each part has its own Xcode target (since there can be only 1 main in each target).

### Steps for each new day
- create the dated folder and add inside the data files : data.txt and sample.txt (if any)
- create in the dated folder a folder for each part
- inside each part folder :
    - create a main.cpp (copy an existing and change the date of the data file)
    - create partX.hpp and partX.cpp
- for each part, create an Xcode target (File > New > Target)
- set the working directory to the top of the project (Product > Scheme > Edit) so the data file can be read
- Ensure each required cpp file is ticked in "Target Membership" frame (usually common/Utils.cpp and partX.cpp)
