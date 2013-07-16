/*
 * File:   DataGeneratorTest.h
 * Author: golovin
 *
 * Created on 16.07.2013, 9:02:27
 */

#ifndef DATAGENERATORTEST_H
#define	DATAGENERATORTEST_H

#include <cppunit/extensions/HelperMacros.h>

class DataGeneratorTest : public CPPUNIT_NS::TestFixture {
    CPPUNIT_TEST_SUITE(DataGeneratorTest);

    CPPUNIT_TEST(testRandomlyGenerateString);

    CPPUNIT_TEST_SUITE_END();

public:
    DataGeneratorTest();
    virtual ~DataGeneratorTest();
    void setUp();
    void tearDown();

private:
    void testRandomlyGenerateString();

};

#endif	/* DATAGENERATORTEST_H */

