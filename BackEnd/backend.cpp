#include "Rand/DataGenerator.h"
#include "Mut/DataMutator.h"
#include <assert.h>

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
    
    short generate_short(const short _min = 0, const short _max = 1000){
        DataGenerator gen;
        short res = gen.randomlyGenerateNumber<short>(_min, _max);
        return res;
    }
    
    ushort generate_unsigned_short(const ushort _min = 0, const ushort _max = 1000){
        DataGenerator gen;
        ushort res = gen.randomlyGenerateNumber<ushort>(_min, _max);
        return res;
    }
    
    int generate_int32(const int _min = 0, const int _max = 1000){
        DataGenerator gen;
        int res = gen.randomlyGenerateNumber<int>(_min, _max);
        return res;
    }
    
    uint generate_unsigned_int32(const uint _min = 0, const uint _max = 1000){
        DataGenerator gen;
        uint res = gen.randomlyGenerateNumber<uint>(_min, _max);
        return res;
    }
    
    
    long long generate_int64(const long long _min = 0, const long long _max = 1000){
        DataGenerator gen;
        long long res = gen.randomlyGenerateNumber<long long>(_min, _max);
        return res;
    }
    unsigned long long generate_unsigned_int64(const unsigned long long _min = 0, const unsigned long long _max = 1000){
        DataGenerator gen;
        unsigned long long res = gen.randomlyGenerateNumber<unsigned long long>(_min, _max);
        return res;
    }
    
    float generate_float(const float _min = 0, const float _max = 1000){
        DataGenerator gen;
        float res = gen.randomlyGenerateNumber<float>(_min, _max);
        return res;
    }
    
    double generate_double(const double _min = 0, const double _max = 1000){
        DataGenerator gen;
        double res = gen.randomlyGenerateNumber<double>(_min, _max);
        return res;
    }
    
    long double generate_long_double(const long double _min = 0, const long double _max = 1000){
        DataGenerator gen;
        long double res = gen.randomlyGenerateNumber<long double>(_min, _max);
        return res;
    }
    
    int mutate_int32(int _value, int _numberOfMutations = 10)
    {
        DataMutator mut;
        
        int res = mut.mutateInt32(_value, _numberOfMutations);
        
        return res;
    }
}
