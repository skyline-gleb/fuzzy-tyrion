/* 
 * File:   DataGeneratot.cpp
 * Author: user
 * 
 * Created on July 9, 2013, 1:23 PM
 */

#include "DataGenerator.h"
#include "types.h"
#include <iostream>
#include <cstdlib>
#include <sstream>
#include <climits>
#define SIZE 100

DataGenerator::DataGenerator() {
}

std::list<std::string> DataGenerator::randomlyGenerateData(const Type &type, const int numGeneration){

    std::list<std::string> data;
    
    switch(type){
        case STRING :{
            for(int i = 0; i < numGeneration; i++){
                data.push_back(genRandomString(rand() % SIZE));
            }
        }
        break;
        case INT32 : {
            
            for(int i = 0; i < numGeneration; i++){ 
                std::stringstream sstr;
                int number = (rand() << 30) | (rand() << 15) | rand();
                sstr << number;
                std::string s;
                sstr >> s;
                data.push_back(s);
            }
        }
        case FLOAT : {
            const int MIN = -2;
            const int MAX = 3;
            const int PRECISION = 10000;
            for(int i = 0; i < numGeneration; i++){ 
                std::stringstream sstr;

                float randomNumber;
                randomNumber = MIN + (rand()%((MAX - MIN) * PRECISION + 1)) / (float)PRECISION;
                sstr << randomNumber;
                std::string s;
                sstr >> s;
                data.push_back(s);
            }
        }
        
    }
    return data;
//    for(std::list<std::string>::iterator it = data.begin(); it != data.end(); it++){
//        std::cout << *it << std::endl; 
//    }
}

std::string DataGenerator::genRandomString(const int len) {
    std::string str;
    for (int i = 0; i < len; i++) {
        str.push_back(rand() % 256);
    }
    return str;
}



