#include <iostream>
#include <string>

using namespace std;

extern "C" {

    char * func(char *_s) {
        std::cout << "print cpp extern func 'C': " << _s << std::endl;

        return _s;
    }
}