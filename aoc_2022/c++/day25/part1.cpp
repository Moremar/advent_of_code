#include "part1.h"

using namespace std;


namespace Day25 {

    vector<string> parse(const string& filename) {
        return getFileLines(filename);
    }


    namespace Part1 {

        long long snafuToDecimal(const string& snafu) {
            long long result = 0;
            for (int i = 0; i < snafu.size(); ++i) {
                int digit = 0;
                if (snafu[i] == '2')      { digit  = 2; }
                else if (snafu[i] == '1') { digit  = 1; }
                else if (snafu[i] == '-') { digit = -1; }
                else if (snafu[i] == '=') { digit = -2; }
                result = 5 * result + digit;
            }
            return result;
        }

        string decimalToSnafu(const long long n) {
            long long curr = n;
            string result {};
            const map<int, string> snafuDigits { {-2, "="}, {-1, "-"}, {0, "0"}, {1, "1"}, {2, "2"} };
            while (curr > 0) {
                int remainder = curr % 5;
                if (remainder > 2) {
                    remainder -= 5;
                }
                curr = (curr - remainder) / 5;
                result = snafuDigits.at(remainder) + result;
            }
            return result;
        }

        string solve(const vector<string>& snafus) {
            long long result = 0;
            for (const auto& snafu : snafus) {
                result += snafuToDecimal(snafu);
            }
            return decimalToSnafu(result);
        }

    }
}
