
#include "Utils.h"
#include "AdventException.h"

using namespace std;


vector<string> getFileLines(const string& filePath) {
    vector<string> res;
    ifstream f { filePath };
    if (f) {
        string line;
        while (getline(f, line)) {
            res.push_back(line);
        }
        f.close();
    } else {
        throw AdventException("Unable to open file " + filePath);
    }
    return res;
}

string ltrim(const string& str, const string& chars) {
    string res { str };
    res.erase(0, res.find_first_not_of(chars));
    return res;
}

string rtrim(const string& str, const string& chars) {
    string res { str };
    res.erase(res.find_last_not_of(chars) + 1);
    return res;
}

string trim(const string& str, const string& chars) {
    return ltrim(rtrim(str, chars), chars);
}

vector<string> split(const string& s, const string& delim) {
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

vector<string> regexSplit(const string& s, const regex& pattern) {
  sregex_token_iterator iter(s.begin(), s.end(), pattern, -1);
  sregex_token_iterator end;
  return { iter, end };
}

bool contains(const string& s, const string& sub) {
    return s.find(sub) != string::npos;
}
