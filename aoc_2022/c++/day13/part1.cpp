#include "part1.h"

using namespace std;


namespace Day13 {

    strong_ordering Value::operator<=>(const Value& o) const {
        // compare 2 integers
        if (type == ValueType_t::integer_e && o.type == ValueType_t::integer_e) {
            return intValue <=> o.intValue;
        }
        // compare integer with list
        if (type == ValueType_t::integer_e) {
            return Value{ vector<Value>{ *this } } <=> o;
        }
        // compare list with integer
        if (o.type == ValueType_t::integer_e) {
            return *this <=> Value{ vector<Value>{ o } };
        }
        // compare 2 lists : compare elements one by one
        int i = 0;
        while (i < listValue.size() && i < o.listValue.size()) {
            const auto compare = listValue[i] <=> o.listValue[i];
            if (compare != strong_ordering::equal) {
                return compare;
            }
            ++i;
        }
        // if we reach here, all elements have been compared, the shortest list is inferior
        if (listValue.size() < o.listValue.size()) {
            return strong_ordering::less;
        }
        if (listValue.size() > o.listValue.size()) {
            return strong_ordering::greater;
        }
        return strong_ordering::equal;
    }


    vector<pair<Value, Value>> parse(const string& filename) {
        vector<pair<Value, Value>> packets {};
        const auto lines = getFileLines(filename);
        int line_i = 0;
        while (line_i < lines.size()) {
            const auto val1 = Part1::parseValue(lines[line_i++]);
            const auto val2 = Part1::parseValue(lines[line_i++]);
            packets.emplace_back(val1, val2);
            ++line_i;  // empty line
        }
        return packets;
    }


    namespace Part1 {

        Value parseValue(const string& valueStr) {
            // integer value
            if (valueStr[0] != '[') {
                return { stoi(valueStr) };
            }
            // list value
            vector<Value> listValue {};
            int start_i = 1;   // skip initial '['       
            int curr_i = start_i;
            int depth = 0;     // used to find the corresponding closing square bracket
            while (curr_i < valueStr.size()) {
                if ( (valueStr[curr_i] == ',' && depth == 0)              // end of value
                  || (valueStr[curr_i] == ']' && depth == 0) ) {          // end of last value
                    if (curr_i != start_i) {
                        listValue.push_back(parseValue(valueStr.substr(start_i, curr_i - start_i)));
                    }
                    start_i = curr_i + 1;
                    curr_i = start_i;
                    continue;                
                }
                if (valueStr[curr_i] == '[') {
                    depth += 1;
                }
                if (valueStr[curr_i] == ']') {
                    depth -= 1;
                }
                ++curr_i;
            }

            return { listValue };
        }


        int solve(const vector<pair<Value, Value>>& packets) {
            vector<int> ordered {};
            for (int i = 0; i < packets.size(); ++i) {
                if (packets[i].first < packets[i].second) {
                    ordered.push_back(i+1);
                }
            }
            return accumulate(ordered.begin(), ordered.end(), 0);
        }

    }
}
