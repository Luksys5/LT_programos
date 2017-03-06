#!/bin/sh
#------------------------------------------------------------------------------
#$Author: saulius $
#$Date: 2010-03-11 09:29:43 +0200 (Kt, 11 Kov 2010) $
#$Revision: 193 $
#$URL: svn://saulius-grazulis.lt/scripts/shtests/prepare/multi002.sh $
#------------------------------------------------------------------------------
#*
# Test for the 'prepare' script.
#
# Test whether '.setup' script is called correctly when multiple
# working directories are created.
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

TEMPLATES="first second third"

cd ${TSTDIR}

basename `pwd`

rm -rf ${TEMPLATES}

${prepare} --no-svn --template-dir ../templates \
    ${TEMPLATES} -- --option1 --opt2 arg2 arg3

for TEMPLATE in ${TEMPLATES}
do

  echo ""
  ls -1a ${TEMPLATE}

  TEST_FILE=${TEMPLATE}/file.txt

  echo ""
  echo === ${TEST_FILE} ===
  cat ${TEST_FILE}

done
