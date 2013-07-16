/*
 * File:   DataMutatorTest.cpp
 * Author: golovin
 *
 * Created on 16.07.2013, 12:15:47
 */

#include "DataMutatorTest.h"
#include "Mut/DataMutator.h"


CPPUNIT_TEST_SUITE_REGISTRATION(DataMutatorTest);

DataMutatorTest::DataMutatorTest()
{
}

DataMutatorTest::~DataMutatorTest()
{
}

void DataMutatorTest::setUp()
{
}

void DataMutatorTest::tearDown()
{
}

void DataMutatorTest::testMutateInt32()
{
    DataMutator dataMutator;
    int value = 925;
    int numberOfMutations = 5;
    
    int result1 = dataMutator.mutateInt32(value, numberOfMutations);
    int result2 = dataMutator.mutateInt32(value, numberOfMutations);
    
    CPPUNIT_ASSERT(result1 != result2);
}

