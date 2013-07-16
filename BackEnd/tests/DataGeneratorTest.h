/*
 * File:   DataGeneratorTest.h
 * Author: user
 *
 * Created on Jul 15, 2013, 1:33:43 PM
 */

#ifndef DATAGENERATORTEST_H
#define	DATAGENERATORTEST_H

#include <cppunit/extensions/HelperMacros.h>

class DataGeneratorTest : public CPPUNIT_NS::TestFixture {
    CPPUNIT_TEST_SUITE(DataGeneratorTest);

    CPPUNIT_TEST(testRandomlyGenerateInt32);
    CPPUNIT_TEST(testRandomlyGenerateFloat);
    CPPUNIT_TEST(testRandomlyGenerateDouble);

    CPPUNIT_TEST_SUITE_END();

public:
    DataGeneratorTest();
    virtual ~DataGeneratorTest();
    void setUp();
    void tearDown();

private:
    void testRandomlyGenerateInt32();
    void testRandomlyGenerateFloat();
    void testRandomlyGenerateDouble();

};

#endif	/* DATAGENERATORTEST_H */

