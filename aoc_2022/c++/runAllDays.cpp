#include <algorithm>  // std::transform
#include <chrono>
#include <iostream>
#include <cstdlib>    // system

using namespace std;

enum class platform_t {
    unix_e    = 0,
    windows_e = 1
};

int main(int argc, char* argv[]) {

    const auto startTime = chrono::high_resolution_clock::now();

    // extract platform
    string platformStr {};
    if (argc > 1) platformStr = argv[1];
    transform(platformStr.begin(), platformStr.end(), platformStr.begin(), ::toupper);
    const auto platform = platformStr == "WINDOWS" ? platform_t::windows_e : platform_t::unix_e;

    // run the binaries for all days
    for (int i = 1; i <= 25; ++i) {
        const string paddedNumber = (i < 10 ? "0" : "") + to_string(i);
        const string command = platform == platform_t::windows_e
                             ? "day" + paddedNumber + "\\Release\\day" + paddedNumber + ".bin.exe"
                             : "day" + paddedNumber + "/day" + paddedNumber + ".bin";
        cout << endl << "DAY " << paddedNumber << " : " << command << endl;
        system(command.c_str());
    }

    // report total execution time
    const auto endTime  = chrono::high_resolution_clock::now();
    const auto duration = duration_cast<chrono::seconds>(endTime - startTime).count();
    cout << endl << "All days solutions took " << duration << " seconds to complete." << endl << endl;

    return 0;
}
