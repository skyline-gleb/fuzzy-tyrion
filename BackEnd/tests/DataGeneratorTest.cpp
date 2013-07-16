/*
 * File:   DataGeneratorTest.cpp
 * Author: user
 *
 * Created on Jul 15, 2013, 1:33:43 PM
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

