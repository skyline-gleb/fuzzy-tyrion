#include "Rand/DataGenerator.h"
#include <assert.h>

extern "C" {

    char * generate_string(const int _length = 10) {
        
        assert(_length > 0 && _length <= 2147483647);
        
        DataGenerator gen;
        std::string str = (gen.randomlyGenerateString<std::string>(_length));
        
        assert(str.size() > 0 && str.size() <= _length);
        
        char* pres = (char*)str.c_str();
        return pres;
    }
    
    int generate_int32(const int _min = 0, const int _max = 1000)
    {
        assert(_min < _max);
        assert(_min >= -2147483648 && _max <= 2147483647);
        
        DataGenerator gen;
        int res = gen.randomlyGenerateNumber<int>(_min, _max);
        assert(res >= _min && res <= _max);
        
        return res;
    }
}
