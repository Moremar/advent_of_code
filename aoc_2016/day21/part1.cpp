#include "part1.hpp"

using namespace std;


string swapPos(const string &pwd, size_t pos1, size_t pos2) {
        string nextPwd = pwd;
        nextPwd[pos1] = pwd.at(pos2);
        nextPwd[pos2] = pwd.at(pos1);
        return nextPwd;
}

string swapLetter(const string &pwd, char letter1, char letter2) {
        string nextPwd = pwd;
        replace( nextPwd.begin(), nextPwd.end(), letter1, '!'     );
        replace( nextPwd.begin(), nextPwd.end(), letter2, letter1 );
        replace( nextPwd.begin(), nextPwd.end(), '!',     letter2 );
        return nextPwd;
}

string rotateLeft(const string &pwd, size_t times) {
    if (times == 0) return pwd;
    return pwd.substr(times) + pwd.substr(0, times);
}

string rotateRight(const string &pwd, size_t times) {
    if (times == 0) return pwd;
    size_t splitIdx = pwd.size() - times;
    return pwd.substr(splitIdx) + pwd.substr(0, splitIdx);
}

string rotateBased(const string &pwd, char letter) {
    size_t idx = pwd.find(letter);
    size_t rotateTimes =  1 + idx + (idx >= 4 ? 1 : 0);
    rotateTimes = rotateTimes % pwd.size();
    size_t splitIdx = pwd.size() - rotateTimes;
    return pwd.substr(splitIdx) + pwd.substr(0, splitIdx);
}

string oppositeBased(const string &pwd, char letter) {
    // no bijection here, but know we need to rotate a number of times so we try each
    for (size_t i = 0; i < pwd.size(); i++) {
        const string attempt = Part1::processInstruction(Instruction("RotateRight", to_string(i)[0], ' '), pwd);
        const string rotated = Part1::processInstruction(Instruction("RotateBased", letter, ' '), attempt);
        if (rotated == pwd) return attempt;
    }
    throw AdventException("No oppositite found");
}

string reverse(const string &pwd, size_t pos1, size_t pos2) {
    ostringstream oss;
    for (size_t i = 0;      i < pos1;       ++i)  oss << pwd[i];
    for (size_t i = pos1;   i < pos2+1;     ++i)  oss << pwd[pos1 + pos2 - i];
    for (size_t i = pos2+1; i < pwd.size(); ++i)  oss << pwd[i];
    return oss.str();
}

string move(const string &pwd, size_t pos1, size_t pos2) {
    ostringstream oss;
    if (pos1 < pos2) {
        oss << pwd.substr(0, pos1) << pwd.substr(pos1+1, pos2-pos1) << pwd.at(pos1) << pwd.substr(pos2+1);
    } else {
        oss << pwd.substr(0, pos2) << pwd.at(pos1) << pwd.substr(pos2, pos1-pos2) << pwd.substr(pos1+1);
    }
    return oss.str();
}

string Part1::processInstruction(const Instruction &instr, const string &pwd) {
    size_t numX = "0123456789"s.find(instr.X) ? static_cast<size_t>(instr.X - '0') : 0;
    size_t numY = "0123456789"s.find(instr.Y) ? static_cast<size_t>(instr.Y - '0') : 0;
    if (instr.type == "SwapPos")       return swapPos(pwd, numX, numY);
    if (instr.type == "SwapLetter")    return swapLetter(pwd, instr.X, instr.Y);
    if (instr.type == "RotateLeft")    return rotateLeft(pwd, numX);
    if (instr.type == "RotateRight")   return rotateRight(pwd, numX);
    if (instr.type == "RotateBased")   return rotateBased(pwd, instr.X);
    if (instr.type == "OppositeBased") return oppositeBased(pwd, instr.X);
    if (instr.type == "Reverse")       return reverse(pwd, numX, numY);
    if (instr.type == "Move")          return move(pwd, numX, numY);   
    throw AdventException("Unkown command " + instr.type);
}

string Scrambler::scramble(const string &clearPwd) {
    string pwd = clearPwd;
    for (const auto &instr: myInstructions) {
        pwd = Part1::processInstruction(instr, pwd);
    }
    return pwd;
}

pair<string, vector<Instruction>> Part1::parse(const string &fileName) {
    const auto lines = getFileLines(fileName); 
    string clearPwd = lines[0];

    regex swapPosRgx("swap position ([0-9]) with position ([0-9])");
    regex swapLetterRgx("swap letter ([a-z]) with letter ([a-z])");
    regex rotateLeftRgx("rotate left ([0-9]) step");
    regex rotateRightRgx("rotate right ([0-9]) step");
    regex rotateBasedRgx("rotate based on position of letter ([a-z])");
    regex reverseRgx("reverse positions ([0-9]) through ([0-9])");
    regex moveRgx("move position ([0-9]) to position ([0-9])");

    vector<Instruction> instructions;
    for (size_t i = 1; i < lines.size(); ++i) {
        smatch match;
        if (regex_search(lines[i].begin(), lines[i].end(), match, swapPosRgx)) {
            instructions.emplace_back("SwapPos", string(match[1])[0], string(match[2])[0]);
        } else if (regex_search(lines[i].begin(), lines[i].end(), match, swapLetterRgx)) {
            instructions.emplace_back("SwapLetter", string(match[1])[0], string(match[2])[0]);
        } else if (regex_search(lines[i].begin(), lines[i].end(), match, rotateLeftRgx)) {
            instructions.emplace_back("RotateLeft", string(match[1])[0], ' ');
        } else if (regex_search(lines[i].begin(), lines[i].end(), match, rotateRightRgx)) {
            instructions.emplace_back("RotateRight", string(match[1])[0], ' ');
        } else if (regex_search(lines[i].begin(), lines[i].end(), match, rotateBasedRgx)) {
            instructions.emplace_back("RotateBased", string(match[1])[0], ' ');
        } else if (regex_search(lines[i].begin(), lines[i].end(), match, reverseRgx)) {
            instructions.emplace_back("Reverse", string(match[1])[0], string(match[2])[0]);
        } else if (regex_search(lines[i].begin(), lines[i].end(), match, moveRgx)) {
            instructions.emplace_back("Move", string(match[1])[0], string(match[2])[0]);
        } else {
            throw AdventException("Unknown instruction : " + lines[i]);
        }
    }
    return { clearPwd, instructions };
}

string Part1::solve(const pair<string, vector<Instruction>> &input) {
    Scrambler scrambler(input.second);
    return scrambler.scramble(input.first);
}
