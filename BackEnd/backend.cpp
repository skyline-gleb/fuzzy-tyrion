#include "Rand/DataGenerator.h"


extern "C" {

    char * StringGenerate(const int _length) {

        DataGenerator gen;
        std::string str = (gen.randomlyGenerateString(_length));
        char* pres;
        pres = new char[str.size() + 1];
        int i;
        for (i = 0; i < str.size(); ++i)
            pres[i] = str[i];
        pres[i] = 0;
        
        return pres;
    }
}
