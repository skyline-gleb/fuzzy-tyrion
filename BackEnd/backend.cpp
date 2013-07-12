#include "Rand/DataGenerator.h"


extern "C" {

    char * generateString(const int _length = 10) {

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
    
    int generateInt32(const int _min = 0, const int _max = 1000)
    {
        DataGenerator gen;
        return gen.randomlyGenerateInt32();
    }
}
