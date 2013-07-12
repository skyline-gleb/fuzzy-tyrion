/* 
 * File:   DataGeneratot.cpp
 * Author: user
 * 
 * Created on July 9, 2013, 1:23 PM
 */

#include "DataGenerator.h"
#include <cstdlib>

DataGenerator::DataGenerator() {
}

std::string DataGenerator::randomlyGenerateString(const int len) {
    std::string str;
    for (int i = 0; i < len; i++) {
        str.push_back(rand() % 256);
    }
    return str;
}

int DataGenerator::randomlyGenerateInt32() {
    return (rand() << 30) | (rand() << 15) | rand();
}

float DataGenerator::randomlyGenerateFloat() {
    const int MIN = -2;
    const int MAX = 3;
    const int PRECISION = 10000;
    return MIN + (rand() % ((MAX - MIN) * PRECISION + 1)) / (float) PRECISION;
}
