#include "Rand/DataGenerator.h"


extern "C" {

    char * generateString(const int _length = 10) {

        DataGenerator gen;
        std::string str = (gen.randomlyGenerateString(_length));
        char* pres = (char*)str.c_str();
        return pres;
    }
    
    int generateInt32(const int _min = 0, const int _max = 1000)
    {
        DataGenerator gen;
        return gen.randomlyGenerateInt32();
    }
}
