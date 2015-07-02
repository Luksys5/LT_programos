#!/bin/bash
#------------------------------------------------------------------------------
#$Author: saulius $
#$Date: 2007-07-09 21:01:25 +0300 (Pr, 09 Lie 2007) $
#$Revision: 101 $
#$URL: svn://saulius-grazulis.lt/scripts/shtests/spacekill/in-place001.sh $
#------------------------------------------------------------------------------
#*
# Test for the 'spacekill' script.
# A simple test for the in-line file update
#**

set -ue

#BEGIN DEPEND------------------------------------------------------------------

INPUT_SCRIPT=spacekill

#END DEPEND--------------------------------------------------------------------

WD=`pwd`

spacekill=${WD}/${INPUT_SCRIPT}

DIR_NAME=$(dirname $0)
BASENAME=$(basename $0 .sh)

TEST_FILE=${DIR_NAME}/${BASENAME}.inp

# This test prepares a fresh empty subdirectory, copies the test file 
# there, runs an in-place on that copy and outputs the update copy to 
# the stdout.

TMP_DIR="./tmp-${BASENAME}-$$"
mkdir "${TMP_DIR}"

cp ${TEST_FILE} ${TMP_DIR}

(
    cd ${TMP_DIR}
    TEST_BASENAME=$(basename ${TEST_FILE})

    ${spacekill} --in-place ${TEST_BASENAME}

    cat ${TEST_BASENAME}
)

rm -rf "${TMP_DIR}"
