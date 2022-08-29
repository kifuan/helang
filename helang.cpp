// A shit parody of Saint He's cyber language.

#include <utility>
#include <vector>
#include <iostream>
#include <string>
#include <regex>

class NumberList {
public:
    std::vector<int> indexes_;

    NumberList() = default;

    NumberList(int i) {
        indexes_.push_back(i);
    }

    NumberList(const std::vector<int>& indexes): indexes_(indexes) {}
    NumberList(std::vector<int>&& indexes): indexes_(indexes) {}

    operator int() {
        return indexes_[0];
    }

    operator bool() {
        return indexes_[0];
    }

    bool operator<(int n) {
        return indexes_[0] < n;
    }

    void operator++(int) {
        *this - (-1);
    }

    NumberList& operator-(int n) {
        for (int& index : indexes_) {
            index -= n;
        }
        return *this;
    }
};

class ArrayWriter {
public:
    std::vector<int> elements_;
    NumberList list_;

    ArrayWriter() {
        elements_.resize(68, 0);
    }

    ArrayWriter& operator[](const NumberList& list) {
        list_ = list;
        return *this;
    }

    ArrayWriter& operator=(int data) {
        for (int index : list_.indexes_) {
            elements_[index] = data;
        }
        return *this;
    }
};

ArrayWriter forceCon;

NumberList to_number_list(const std::string& str) {
    std::regex re(R"(\s*\|\s*)");
    std::vector<std::string> tokens(std::sregex_token_iterator(str.begin(), str.end(), re, -1), std::sregex_token_iterator());

    std::vector<int> indexes;
    std::transform(tokens.begin(), tokens.end(), std::back_inserter(indexes), [](const auto& s) { return std::stoi(s); });

    return {std::move(indexes)};
}

using u8 = NumberList;

void powerCon(u8 whichKey, u8 force) {
    if (whichKey) {
        forceCon[whichKey - 1] = force;
    } else {
        for (u8 i = 0; i < 68; i++) {
            forceCon[i] = force;
        }
    }
}

#define powerCon(nums, force) powerCon(to_number_list(#nums), force)

void littleFingerForce() {
    powerCon(0, 100);
    powerCon(1 | 2 | 6 | 7 | 11 | 52 | 57 | 58 | 65, 10);
}

int main() {
    littleFingerForce();

    for (int i = 0; i < forceCon.elements_.size(); i++) {
        int el = forceCon.elements_[i];
        std::cout << i << ": " << el << std::endl;
    }
}
