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


template < typename T >
T DataGenerator::randomlyGenerateString(const int len){
    srand(time(0));
    T str;
    for(int i = 0; i < len; i++) {
        str.push_back(rand() % 256);
    }
}