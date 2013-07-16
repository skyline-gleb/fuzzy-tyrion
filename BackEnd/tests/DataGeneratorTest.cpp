/*
 * File:   newtestclass.cpp
 * Author: user
 *
 * Created on Jul 15, 2013, 4:58:45 PM
 */

#include "newtestclass.h"


CPPUNIT_TEST_SUITE_REGISTRATION(newtestclass);

newtestclass::newtestclass()
{
}

newtestclass::~newtestclass()
{
}

void newtestclass::setUp()
{
}

void newtestclass::tearDown()
{
}

void newtestclass::testMethod()
{
    CPPUNIT_ASSERT(true);
}

void newtestclass::testFailedMethod()
{
    CPPUNIT_ASSERT(false);
}

