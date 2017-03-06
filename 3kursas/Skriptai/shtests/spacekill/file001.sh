#!/bin/bash
#------------------------------------------------------------------------------
#$Author: saulius $
#$Date: 2007-07-09 21:01:25 +0300 (Pr, 09 Lie 2007) $
#$Revision: 101 $
#$URL: svn://saulius-grazulis.lt/scripts/shtests/spacekill/file001.sh $
#------------------------------------------------------------------------------
#*
# Test for the 'spacekill' script.
# This a very simple test for the basic functionality.
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

# This test just runs the script on an input file and outputs the
# result to the stdout.

${spacekill} ${TEST_FILE}

# Thats it.
