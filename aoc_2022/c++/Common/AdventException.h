#pragma once

#include <stdexcept>
#include <string>

class AdventException : public std::runtime_error {
public:
    AdventException(const std::string& msg) : runtime_error(msg) {}
};
