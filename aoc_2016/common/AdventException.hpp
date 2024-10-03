#ifndef AdventException_hpp
#define AdventException_hpp

#include <string>
#include <stdexcept>


class AdventException : public std::runtime_error {
public:
    AdventException(const std::string& msg) : runtime_error(msg) {}
};

#endif /* AdventException_hpp */
