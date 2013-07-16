/*
 * File:   DataMutatorTest.h
 * Author: golovin
 *
 * Created on 16.07.2013, 12:15:47
 */

#ifndef DATAMUTATORTEST_H
#define	DATAMUTATORTEST_H

#include <cppunit/extensions/HelperMacros.h>

class DataMutatorTest : public CPPUNIT_NS::TestFixture {
    CPPUNIT_TEST_SUITE(DataMutatorTest);

    CPPUNIT_TEST(testMutateInt32);

    CPPUNIT_TEST_SUITE_END();

public:
    DataMutatorTest();
    virtual ~DataMutatorTest();
    void setUp();
    void tearDown();

private:
    void testMutateInt32();

};

#endif	/* DATAMUTATORTEST_H */

