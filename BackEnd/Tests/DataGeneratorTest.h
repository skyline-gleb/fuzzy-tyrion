/* 
 * File:   DataGeneratorTest.h
 * Author: golovin
 *
 * Created on 15 Июль 2013 г., 11:44
 */

#ifndef DATAGENERATORTEST_H
#define	DATAGENERATORTEST_H

#include <cppunit/TestFixture.h>
#include <cppunit/extensions/HelperMacros.h>

#include "../Rand/DataGenerator.h"

class DataGeneratorTest : public CppUnit::TestFixture {
    CPPUNIT_TEST_SUITE(DataGeneratorTest);
    CPPUNIT_TEST(testGenValue_DifGenerators);
    CPPUNIT_TEST(testGenValue_OneGenerators);
    CPPUNIT_TEST_SUITE_END();
private:
    DataGenerator gen1, gen2;
public:

    void setUp() {
        // инициализация
    }

    void tearDown() {
        // деинициализация
    }

    void testGenValue_DifGenerators()
    {
        CPPUNIT_ASSERT(gen1.randomlyGenerateNumber<int>() !=
                gen2.randomlyGenerateNumber<int>());
    }

    void testGenValue_OneGenerators()
    {
        CPPUNIT_ASSERT(gen1.randomlyGenerateNumber<int>() !=
                gen1.randomlyGenerateNumber<int>());
    }
};

#endif	/* DATAGENERATORTEST_H */

