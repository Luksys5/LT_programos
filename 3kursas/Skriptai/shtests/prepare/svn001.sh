#!/bin/sh
#------------------------------------------------------------------------------
#$Author: saulius $
#$Date: 2010-03-11 09:29:43 +0200 (Kt, 11 Kov 2010) $
#$Revision: 193 $
#$URL: svn://saulius-grazulis.lt/scripts/shtests/prepare/svn001.sh $
#------------------------------------------------------------------------------
#*
# Test for the 'prepare' script.
# Check how newly created directories are committed to Subversion
# repositories.
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
DIR=$(cd ${DIR}; pwd)

BASE=$(basename $0 .sh)

TSTDIR=${DIR}/outputs/${BASE}

REPO=${TSTDIR}/repo
WORK=${TSTDIR}/work
TMPL=${DIR}/templates

rm -rf ${TSTDIR}
mkdir -p ${TSTDIR}

svnadmin create --fs-type fsfs ${REPO}

(
    ## set -x
    svn co file:///${REPO} ${WORK}
)

TEMPLATE=setup

(
    ## set -x

    cd ${WORK}

    basename `pwd`

    ${prepare} --template-dir ${TMPL} ${TEMPLATE}

    echo ""
    ls -1a ${TEMPLATE}

    TEST_FILE=${TEMPLATE}/file.txt

    echo ""
    echo === ${TEST_FILE} ===
    cat ${TEST_FILE}

    svn update

    echo ""
    echo "=== Subversion log message: ==="

    svn log | tail -n2 | head -n1
)

## rm -rf ${TSTDIR}
