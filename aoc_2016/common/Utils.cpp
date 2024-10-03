#include <fstream>
#include "Utils.hpp"
#include "AdventException.hpp"

using namespace std;


std::string operator +(const std::string &s, const char &c) {
    std::ostringstream ss;
    ss << s << c;
    return ss.str();
}

std::string operator +(const std::string &s, const string &s2) {
    std::ostringstream ss;
    ss << s << s2;
    return ss.str();
}

vector<string> split(const string &s, const string &delim) {
    vector<string> res;
    string rest = s;
    size_t pos = rest.find(delim);
    while (pos != string::npos) {
        res.push_back(rest.substr(0, pos));
        rest = rest.substr(pos + delim.size());
        pos = rest.find(delim);
    }
    res.push_back(rest.substr(0, pos));  // last part of the string
    return res;
}


string ltrim(const string& str, const string& chars = "\t\n\v\f\r ") {
    string res(str);
    res.erase(0, res.find_first_not_of(chars));
    return res;
}

string rtrim(const string& str, const string& chars = "\t\n\v\f\r ") {
    string res(str);
    res.erase(res.find_last_not_of(chars) + 1);
    return res;
}

string trim(const string& str, const string& chars) {
    return ltrim(rtrim(str, chars), chars);
}

string removeSubstr(const string &s, const string &substring) {
    const auto nextPos = s.find(substring);
    if (nextPos == string::npos) {
        return s;
    }
    string updated = s;
    updated.erase(nextPos, substring.length());
    return removeSubstr(updated, substring);
}

vector<string> getFileLines(const string &fileName) {
    vector<string> res;
    ifstream f(fileName);
    if (f) {
        string line;
        while (getline(f, line)) {
            if (line.size() > 0)
                res.push_back(line);
        }
        f.close();
    } else {
        throw AdventException("Unable to open file " + fileName);
    }
    return res;
}

Coordinates operator +(const Coordinates &x, const Coordinates &y) {
    return make_pair(x.first + y.first, x.second + y.second);
}

Coordinates operator *(const Coordinates &x, int i) {
    return make_pair(x.first * i, x.second * i);
}

int manhattan(const Coordinates &p1, const Coordinates &p2) {
    return abs(p1.first - p2.first) + abs(p1.second - p2.second);
}
