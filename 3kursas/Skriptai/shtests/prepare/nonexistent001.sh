#!/bin/sh
#------------------------------------------------------------------------------
#$Author: saulius $
#$Date: 2010-03-11 09:29:43 +0200 (Kt, 11 Kov 2010) $
#$Revision: 193 $
#$URL: svn://saulius-grazulis.lt/scripts/shtests/prepare/nonexistent001.sh $
#------------------------------------------------------------------------------
#*
# Test for the 'prepare' script.
# Check whether non-existent templates are reported properly.
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

TEMPLATE=non-existent-template

cd ${TSTDIR}

basename `pwd`

${prepare} \
    --template-dir ../templates \
    ${TEMPLATE} \
    --no-svn \
    2>&1 \
| sed -e 's,^/.*/prepare,/path/to/prepare,'
