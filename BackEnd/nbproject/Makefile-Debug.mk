#
# Generated Makefile - do not edit!
#
# Edit the Makefile in the project folder instead (../Makefile). Each target
# has a -pre and a -post target defined where you can add customized code.
#
# This makefile implements configuration specific macros and targets.


# Environment
MKDIR=mkdir
CP=cp
GREP=grep
NM=nm
CCADMIN=CCadmin
RANLIB=ranlib
CC=gcc
CCC=g++
CXX=g++
FC=gfortran
AS=as

# Macros
CND_PLATFORM=GNU-Linux-x86
CND_DLIB_EXT=so
CND_CONF=Debug
CND_DISTDIR=dist
CND_BUILDDIR=build

# Include project Makefile
include Makefile

# Object Directory
OBJECTDIR=${CND_BUILDDIR}/${CND_CONF}/${CND_PLATFORM}

# Object Files
OBJECTFILES= \
	${OBJECTDIR}/Rand/DataGenerator.o \
	${OBJECTDIR}/backend.o

# Test Directory
TESTDIR=${CND_BUILDDIR}/${CND_CONF}/${CND_PLATFORM}/tests

# Test Files
TESTFILES= \
	${TESTDIR}/TestFiles/f1

# C Compiler Flags
CFLAGS=

# CC Compiler Flags
CCFLAGS=
CXXFLAGS=

# Fortran Compiler Flags
FFLAGS=

# Assembler Flags
ASFLAGS=

# Link Libraries and Options
LDLIBSOPTIONS=

# Build Targets
.build-conf: ${BUILD_SUBPROJECTS}
	"${MAKE}"  -f nbproject/Makefile-${CND_CONF}.mk ${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/libBackEnd.${CND_DLIB_EXT}

${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/libBackEnd.${CND_DLIB_EXT}: ${OBJECTFILES}
	${MKDIR} -p ${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}
	${LINK.cc} -o ${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/libBackEnd.${CND_DLIB_EXT} ${OBJECTFILES} ${LDLIBSOPTIONS} -shared -fPIC

${OBJECTDIR}/Rand/DataGenerator.o: Rand/DataGenerator.cpp 
	${MKDIR} -p ${OBJECTDIR}/Rand
	${RM} $@.d
	$(COMPILE.cc) -g -fPIC  -MMD -MP -MF $@.d -o ${OBJECTDIR}/Rand/DataGenerator.o Rand/DataGenerator.cpp

${OBJECTDIR}/backend.o: backend.cpp 
	${MKDIR} -p ${OBJECTDIR}
	${RM} $@.d
	$(COMPILE.cc) -g -fPIC  -MMD -MP -MF $@.d -o ${OBJECTDIR}/backend.o backend.cpp

# Subprojects
.build-subprojects:

# Build Test Targets
.build-tests-conf: .build-conf ${TESTFILES}
<<<<<<< HEAD
${TESTDIR}/TestFiles/f1: ${TESTDIR}/tests/newtestclass1.o ${TESTDIR}/tests/newtestrunner1.o ${OBJECTFILES:%.o=%_nomain.o}
	${MKDIR} -p ${TESTDIR}/TestFiles
	${LINK.cc}   -o ${TESTDIR}/TestFiles/f1 $^ ${LDLIBSOPTIONS} `cppunit-config --libs` `cppunit-config --libs`   


${TESTDIR}/tests/newtestclass1.o: tests/newtestclass1.cpp 
	${MKDIR} -p ${TESTDIR}/tests
	${RM} $@.d
	$(COMPILE.cc) -g -I/usr/include/cppunit `cppunit-config --cflags` -MMD -MP -MF $@.d -o ${TESTDIR}/tests/newtestclass1.o tests/newtestclass1.cpp


${TESTDIR}/tests/newtestrunner1.o: tests/newtestrunner1.cpp 
	${MKDIR} -p ${TESTDIR}/tests
	${RM} $@.d
	$(COMPILE.cc) -g -I/usr/include/cppunit `cppunit-config --cflags` -MMD -MP -MF $@.d -o ${TESTDIR}/tests/newtestrunner1.o tests/newtestrunner1.cpp
=======
${TESTDIR}/TestFiles/f1: ${TESTDIR}/Tests/DataGeneratorTest.o ${TESTDIR}/Tests/newtestrunner.o ${OBJECTFILES:%.o=%_nomain.o}
	${MKDIR} -p ${TESTDIR}/TestFiles
	${LINK.cc}   -o ${TESTDIR}/TestFiles/f1 $^ ${LDLIBSOPTIONS} -lcppunit 


${TESTDIR}/Tests/DataGeneratorTest.o: Tests/DataGeneratorTest.cpp 
	${MKDIR} -p ${TESTDIR}/Tests
	${RM} $@.d
	$(COMPILE.cc) -g -I. -MMD -MP -MF $@.d -o ${TESTDIR}/Tests/DataGeneratorTest.o Tests/DataGeneratorTest.cpp


${TESTDIR}/Tests/newtestrunner.o: Tests/newtestrunner.cpp 
	${MKDIR} -p ${TESTDIR}/Tests
	${RM} $@.d
	$(COMPILE.cc) -g -I. -MMD -MP -MF $@.d -o ${TESTDIR}/Tests/newtestrunner.o Tests/newtestrunner.cpp
>>>>>>> develop


${OBJECTDIR}/Rand/DataGenerator_nomain.o: ${OBJECTDIR}/Rand/DataGenerator.o Rand/DataGenerator.cpp 
	${MKDIR} -p ${OBJECTDIR}/Rand
	@NMOUTPUT=`${NM} ${OBJECTDIR}/Rand/DataGenerator.o`; \
	if (echo "$$NMOUTPUT" | ${GREP} '|main$$') || \
	   (echo "$$NMOUTPUT" | ${GREP} 'T main$$') || \
	   (echo "$$NMOUTPUT" | ${GREP} 'T _main$$'); \
	then  \
	    ${RM} $@.d;\
<<<<<<< HEAD
	    $(COMPILE.cc) -g -I/usr/include/cppunit -fPIC  -Dmain=__nomain -MMD -MP -MF $@.d -o ${OBJECTDIR}/Rand/DataGenerator_nomain.o Rand/DataGenerator.cpp;\
=======
	    $(COMPILE.cc) -g -fPIC  -Dmain=__nomain -MMD -MP -MF $@.d -o ${OBJECTDIR}/Rand/DataGenerator_nomain.o Rand/DataGenerator.cpp;\
>>>>>>> develop
	else  \
	    ${CP} ${OBJECTDIR}/Rand/DataGenerator.o ${OBJECTDIR}/Rand/DataGenerator_nomain.o;\
	fi

${OBJECTDIR}/backend_nomain.o: ${OBJECTDIR}/backend.o backend.cpp 
	${MKDIR} -p ${OBJECTDIR}
	@NMOUTPUT=`${NM} ${OBJECTDIR}/backend.o`; \
	if (echo "$$NMOUTPUT" | ${GREP} '|main$$') || \
	   (echo "$$NMOUTPUT" | ${GREP} 'T main$$') || \
	   (echo "$$NMOUTPUT" | ${GREP} 'T _main$$'); \
	then  \
	    ${RM} $@.d;\
<<<<<<< HEAD
	    $(COMPILE.cc) -g -I/usr/include/cppunit -fPIC  -Dmain=__nomain -MMD -MP -MF $@.d -o ${OBJECTDIR}/backend_nomain.o backend.cpp;\
=======
	    $(COMPILE.cc) -g -fPIC  -Dmain=__nomain -MMD -MP -MF $@.d -o ${OBJECTDIR}/backend_nomain.o backend.cpp;\
>>>>>>> develop
	else  \
	    ${CP} ${OBJECTDIR}/backend.o ${OBJECTDIR}/backend_nomain.o;\
	fi

# Run Test Targets
.test-conf:
	@if [ "${TEST}" = "" ]; \
	then  \
	    ${TESTDIR}/TestFiles/f1 || true; \
	else  \
	    ./${TEST} || true; \
	fi

# Clean Targets
.clean-conf: ${CLEAN_SUBPROJECTS}
	${RM} -r ${CND_BUILDDIR}/${CND_CONF}
	${RM} ${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/libBackEnd.${CND_DLIB_EXT}

# Subprojects
.clean-subprojects:

# Enable dependency checking
.dep.inc: .depcheck-impl

include .dep.inc
