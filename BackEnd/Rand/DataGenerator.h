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
    template < typename T >
    T randomlyGenerateString(const int len){
        srand(time(0));
        T str;
        for(int i = 0; i < len; i++) {
                str.push_back(rand() % 256);
        }
        return str;
    }

    template< typename T >
    T randomlyGenerateNumber(T min, T max) {
        srand(time(0));
        return min + (T)((double(rand())/RAND_MAX)*(max - min + 1));
    }

};

#endif	/* DATAGENERATOT_H */

