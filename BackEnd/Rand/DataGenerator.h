/* 
 * File:   DataGeneratot.h
 * Author: user
 *
 * Created on July 9, 2013, 1:23 PM
 */

#ifndef DATAGENERATOT_H
#define	DATAGENERATOT_H
#include <string>
#include <cstdlib>
#include <cmath>

class DataGenerator {
public:
    DataGenerator();
    std::string randomlyGenerateString(const int len);

    template< typename T >
    T randomlyGenerateNumber(T min, T max) {
        srand(time(0));
        return min + (T)((double(rand())/RAND_MAX)*(max - min + 1));
    }

};

#endif	/* DATAGENERATOT_H */

