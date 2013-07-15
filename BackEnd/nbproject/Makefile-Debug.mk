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
	${OBJECTDIR}/Tests/DataGeneratorTest.o \
	${OBJECTDIR}/backend.o


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
LDLIBSOPTIONS=-lcppunit

# Build Targets
.build-conf: ${BUILD_SUBPROJECTS}
	"${MAKE}"  -f nbproject/Makefile-${CND_CONF}.mk ${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/libBackEnd.so

${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/libBackEnd.so: ${OBJECTFILES}
	${MKDIR} -p ${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}
	${LINK.cc} -shared -o ${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/libBackEnd.so -fPIC ${OBJECTFILES} ${LDLIBSOPTIONS} 

${OBJECTDIR}/Rand/DataGenerator.o: Rand/DataGenerator.cpp 
	${MKDIR} -p ${OBJECTDIR}/Rand
	${RM} $@.d
	$(COMPILE.cc) -g -I/usr/include/cppunit -fPIC  -MMD -MP -MF $@.d -o ${OBJECTDIR}/Rand/DataGenerator.o Rand/DataGenerator.cpp

${OBJECTDIR}/Tests/DataGeneratorTest.o: Tests/DataGeneratorTest.cpp 
	${MKDIR} -p ${OBJECTDIR}/Tests
	${RM} $@.d
	$(COMPILE.cc) -g -I/usr/include/cppunit -fPIC  -MMD -MP -MF $@.d -o ${OBJECTDIR}/Tests/DataGeneratorTest.o Tests/DataGeneratorTest.cpp

${OBJECTDIR}/backend.o: backend.cpp 
	${MKDIR} -p ${OBJECTDIR}
	${RM} $@.d
	$(COMPILE.cc) -g -I/usr/include/cppunit -fPIC  -MMD -MP -MF $@.d -o ${OBJECTDIR}/backend.o backend.cpp

# Subprojects
.build-subprojects:

# Clean Targets
.clean-conf: ${CLEAN_SUBPROJECTS}
	${RM} -r ${CND_BUILDDIR}/${CND_CONF}
	${RM} ${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/libBackEnd.so

# Subprojects
.clean-subprojects:

# Enable dependency checking
.dep.inc: .depcheck-impl

include .dep.inc
