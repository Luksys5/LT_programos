#!/bin/sh
#------------------------------------------------------------------------------
#$Author: saulius $
#$Date: 2010-03-11 09:29:43 +0200 (Kt, 11 Kov 2010) $
#$Revision: 193 $
#$URL: svn://saulius-grazulis.lt/scripts/shtests/prepare/simple001.sh $
#------------------------------------------------------------------------------
#*
# Test for the 'prepare' script.
# This a very simple test for the basic functionality.
#**

set -ue

#BEGIN DEPEND------------------------------------------------------------------

INPUT_SCRIPT=prepare

#END DEPEND--------------------------------------------------------------------

unset LANG
unset LC_CTYPE

WD=`pwd`

prepare=${WD}/${INPUT_SCRIPT}

DIR=$(dirname $0)

TSTDIR=${DIR}/outputs

TEMPLATE=simple

cd ${TSTDIR}

basename `pwd`

rm -rf ${TEMPLATE}

${prepare} \
    --template-dir ../templates \
    ${TEMPLATE} \
    --no-svn

echo ""
ls -1a ${TEMPLATE}

TEST_FILE=${TEMPLATE}/file.txt

echo ""
echo === ${TEST_FILE} ===
cat ${TEST_FILE}
