#include <iostream>
#include <string>
#include <jsoncpp/json.h>

#include "jsonparse.h"

using namespace std;

extern "C"
char * func(char *_s) {
    std::cout << "print cpp extern func 'C': " << _s << std::endl;

    jsonParse(_s);
    
    return _s;
}