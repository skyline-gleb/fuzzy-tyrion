/*
 * File:   newtestclass1.cpp
 * Author: user
 *
 * Created on Jul 15, 2013, 5:13:13 PM
 */

#include "newtestclass1.h"


CPPUNIT_TEST_SUITE_REGISTRATION(newtestclass1);

newtestclass1::newtestclass1()
{
}

newtestclass1::~newtestclass1()
{
}

void newtestclass1::setUp()
{
}

void newtestclass1::tearDown()
{
}

void newtestclass1::testMethod()
{
    CPPUNIT_ASSERT(true);
}

void newtestclass1::testFailedMethod()
{
    CPPUNIT_ASSERT(false);
}

