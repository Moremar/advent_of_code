
#pragma once

#include "Coord.h"
#include "Coord3D.h"

#include <algorithm>   // std::max_element
#include <array>
#include <cassert>
#include <chrono>
#include <cmath>       // abs
#include <compare>     // <=> operator
#include <complex>
#include <deque>
#include <fstream>     // std::ifstream
#include <iostream>    // std::cout
#include <map>
#include <numeric>     // std::reduce, std::iota
#include <optional>
#include <ranges>      // std::views
#include <regex>
#include <set>
#include <sstream>     // ostringstream
#include <string>
#include <utility>     // std::pair
#include <vector>

using std::string;
using std::vector;


/**
 * Return the lines of a file
 */
vector<string> getFileLines(const string& filePath);

/**
 * Trim a string
 */
string trim(const string& str, const string& chars = "\t\n\v\f\r ");

/**
 * Split a string on a delimiter
 */
vector<string> split(const string &s, const string &delim);

/*
 * Split a string on a regex pattern
 */
vector<std::string> regexSplit(const std::string& s, const std::regex& pattern);

/**
 * Return true if the string contains the substring
 */
bool contains(const string& s, const string& sub);
