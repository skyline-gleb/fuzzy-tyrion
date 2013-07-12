/* 
 * File:   DataGeneratot.h
 * Author: user
 *
 * Created on July 9, 2013, 1:23 PM
 */

#ifndef DATAGENERATOT_H
#define	DATAGENERATOT_H
#include <list>
#include <string>
#include "types.h"

class DataGenerator {
public:
    DataGenerator();
    std::list<std::string> randomlyGenerateData(const Type &type, const int numGeneration);
private:
    std::string genRandomString(const int len);

};

#endif	/* DATAGENERATOT_H */

