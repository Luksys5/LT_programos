#!/bin/sh
#------------------------------------------------------------------------------
#$Author: saulius $
#$Date: 2010-03-11 09:29:43 +0200 (Kt, 11 Kov 2010) $
#$Revision: 193 $
#$URL: svn://saulius-grazulis.lt/scripts/shtests/prepare/outdir002.sh $
#------------------------------------------------------------------------------
#*
# Test for the 'prepare' script.
# Check how user-supplied output directories are handled.
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

TEMPLATE=setup
OUTDIR=new-subdir/my-working-dir

cd ${TSTDIR}

basename `pwd`

rm -rf ${OUTDIR}
rm -rf ${TEMPLATE}

${prepare} \
    --no-svn \
    --template-dir ../templates \
    ${TEMPLATE} \
    --output ${OUTDIR}

echo ""
ls -1a ${OUTDIR}

TEST_FILE=${OUTDIR}/file.txt

echo ""
echo === ${TEST_FILE} ===
cat ${TEST_FILE}
