#pragma once

// include headers or data structures used across all puzzles
#include <algorithm>
#include <iostream>
#include <list>
#include <map>
#include <numeric>   // std::accumulate
#include <regex>
#include <set>
#include <sstream>   // ostringstream
#include <fstream>   // ofstream
#include <string>
#include <tuple>
#include <utility>  // operations on pairs
#include <vector>

#include "AdventException.hpp"
#include "md5.hpp"

using std::list;
using std::map;
using std::multiset;
using std::make_pair;
using std::pair;
using std::set;
using std::string;
using std::tuple;
using std::vector;

using Coordinates = pair<int, int>;

/**
 * Concatenate a string and a char
 */
string operator +(const string &s, const char &c);

/**
 * Concatenate two strings
 */
string operator +(const string &s, const string &s2);

/**
 * Trim a string
 */
string trim(const string& str, const string& chars = "\t\n\v\f\r ");

/**
 * Split a string on a delimiter
 */
vector<string> split(const string &s, const string &delim);

/**
 * Remove all occurences of a substring from a string
 */
string removeSubstr(const string &s, const string &substring);

/**
 * Get a vector of all not-empty lines of a file
 */
vector<string> getFileLines(const string &fileName);

/**
 * Term by term sum of 2 pairs of int
 */
Coordinates operator +(const Coordinates &x, const Coordinates &y);

/**
 * multiply both terms of a pair by an int
 */
Coordinates operator *(const Coordinates &x, int i);

/**
 * Manhattan distance between 2 points
 */
int manhattan(const Coordinates &p1, const Coordinates &p2);

/**
 * Check if an element is included in a vector
 */
template<class T, class U>
bool in(vector<T> v, T e) {
    return find(v.begin(), v.end(), e) == v.end();
}
