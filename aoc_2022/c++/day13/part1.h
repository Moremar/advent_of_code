#pragma once
#include "../Common/Utils.h"


namespace Day13 {

    enum class ValueType_t {
        integer_e,
        list_e
    };

    class Value {
    public:
        Value(int intValue) : type(ValueType_t::integer_e), intValue(intValue) {};
        Value(std::vector<Value> listValue) : type(ValueType_t::list_e), listValue(listValue) {};

        // operator overload
        std::strong_ordering operator<=>(const Value& o) const;
        bool operator==(const Value& o) const = default;

    private:
        ValueType_t type;
        int intValue { -1 };
        std::vector<Value> listValue {};
    };


    std::vector<std::pair<Value, Value>> parse(const std::string& filename);


    namespace Part1 {

        Value parseValue(const string& valueStr);

        int solve(const std::vector<std::pair<Value, Value>>& packets);

    }
}
