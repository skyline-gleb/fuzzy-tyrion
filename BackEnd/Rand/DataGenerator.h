/* 
 * File:   DataGeneratot.h
 * Author: user
 *
 * Created on July 9, 2013, 1:23 PM
 */

#ifndef DATAGENERATOT_H
#define	DATAGENERATOT_H
#include <string>

class DataGenerator {
public:
    DataGenerator();
    std::string randomlyGenerateString(const int len);
    int randomlyGenerateInt32();
    float randomlyGenerateFloat();
private:
    std::string genRandomString(const int len);

};

#endif	/* DATAGENERATOT_H */

