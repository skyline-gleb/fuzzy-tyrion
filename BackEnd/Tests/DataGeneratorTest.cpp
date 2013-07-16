/*
 * File:   DataGeneratorTest.cpp
 * Author: golovin
 *
 * Created on 16.07.2013, 9:02:28
 */

#include "DataGeneratorTest.h"
#include "Rand/DataGenerator.h"


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

