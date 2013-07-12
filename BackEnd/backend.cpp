#include "DataGenerator.h"


extern "C"
char * stringGenerate(char *_s) {
    
    DataGenerator gen;
    return (gen.randomlyGenerateData(_s);)
}
