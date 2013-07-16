#include "Rand/DataGenerator.h"
#include <assert.h>
#include <limits.h>
#include <float.h>

extern "C" {

    char * generate_string(const int _length = 10) {
        DataGenerator gen;
        std::string str = (gen.randomlyGenerateString<std::string>(_length));
        char* pres = (char*)str.c_str();
        return pres;
    }
    
    wchar_t * generate_wstring(const int _length = 10) {
        DataGenerator gen;
        std::wstring wstr = (gen.randomlyGenerateString<std::wstring>(_length));
        wchar_t* pres = (wchar_t*)wstr.c_str();
        return pres;
    }
    
    short generate_short(const short _min = SHRT_MIN, const short _max = SHRT_MAX){
        DataGenerator gen;
        short res = gen.randomlyGenerateNumber<short>(_min, _max);
        return res;
    }
    
    ushort generate_ushort(const ushort _min = 0, const ushort _max = USHRT_MAX){
        DataGenerator gen;
        ushort res = gen.randomlyGenerateNumber<ushort>(_min, _max);
        return res;
    }
    
    int generate_int32(const int _min = INT_MIN, const int _max = INT_MIN){
        DataGenerator gen;
        int res = gen.randomlyGenerateNumber<int>(_min, _max);
        return res;
    }
    
    uint generate_uint32(const uint _min = 0, const uint _max = UINT_MAX){
        DataGenerator gen;
        uint res = gen.randomlyGenerateNumber<uint>(_min, _max);
        return res;
    }
    
    
    long long generate_int64(const long long _min = LLONG_MIN, const long long _max = LLONG_MAX){
        DataGenerator gen;
        long long res = gen.randomlyGenerateNumber<long long>(_min, _max);
        return res;
    }
    unsigned long long generate_uint64(const unsigned long long _min = 0, const unsigned long long _max = ULLONG_MAX){
        DataGenerator gen;
        unsigned long long res = gen.randomlyGenerateNumber<unsigned long long>(_min, _max);
        return res;
    }
    
    float generate_float(const float _min = FLT_MIN, const float _max = FLT_MAX){
        DataGenerator gen;
        float res = gen.randomlyGenerateNumber<float>(_min, _max);
        return res;
    }
    
    double generate_double(const double _min = DBL_MIN, const double _max = DBL_MAX){
        DataGenerator gen;
        double res = gen.randomlyGenerateNumber<double>(_min, _max);
        return res;
    }
    
    long double generate_long_double(const long double _min = LDBL_MIN, const long double _max = LDBL_MAX){
        DataGenerator gen;
        long double res = gen.randomlyGenerateNumber<long double>(_min, _max);
        return res;
    }
}
