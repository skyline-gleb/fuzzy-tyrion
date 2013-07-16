/*
 * File:   DataGeneratorTest.cpp
 * Author: golovin
 *
 * Created on 16.07.2013, 9:02:28
 */

#include "DataGeneratorTest.h"
#include "../Rand/DataGenerator.h"


CPPUNIT_TEST_SUITE_REGISTRATION(DataGeneratorTest);

DataGeneratorTest::DataGeneratorTest()
{
}

DataGeneratorTest::~DataGeneratorTest()
{
}

void DataGeneratorTest::setUp()
{
}

void DataGeneratorTest::tearDown()
{
}

void DataGeneratorTest::testRandomlyGenerateString()
{
    const int len = 5;
    DataGenerator dataGenerator1, dataGenerator2;
    std::string result1 = dataGenerator1.randomlyGenerateString(len);
    std::string result2 = dataGenerator2.randomlyGenerateString(len);
    if (result1 != result2) {
        CPPUNIT_ASSERT(true);
    }
}

void DataGeneratorTest::testRandomlyGenerateInt32()
{
    DataGenerator dataGenerator;
    CPPUNIT_ASSERT(dataGenerator.randomlyGenerateNumber<int>(1, 1) == 1);
}

void DataGeneratorTest::testRandomlyGenerateFloat()
{
    DataGenerator dataGenerator;
    CPPUNIT_ASSERT( (dataGenerator.randomlyGenerateNumber<float>(10.f, 10.f) - 10) <= 1 );

}

void DataGeneratorTest::testRandomlyGenerateDouble()
{
        DataGenerator dataGenerator;
    CPPUNIT_ASSERT( (dataGenerator.randomlyGenerateNumber<double>(10.d, 10.d) - 10) <= 1 );

}

