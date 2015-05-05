#--*-Makefile -*-------------------------------------------------------------
#$Revision$ 
#$Author$
#$Date$
#$URL$
#--*-------------------------------------------------------------------------
PWD := $(shell pwd)
PATH := ${PWD}/bin:${PATH}
export PATH

INPUT_DIR=./inputs
OUTPUT_DIR=./outputs
TEST_DIR=./tests

INPUTS=${wildcard ${INPUT_DIR}/*.pdb}
TESTS=${INPUTS:${INPUT_DIR}/%.pdb=${TEST_DIR}/%.tst}
OUTPUTS=${INPUTS:${INPUT_DIR}/%.pdb=${OUTPUT_DIR}/%.out}
DIFS=${TESTS:${TEST_DIR}/%.tst=${OUTPUT_DIR}/%.diff}

all: ${TESTS} ${OUTPUTS} ${DIFS}

${OUTPUT_DIR}/%.diff: ${TEST_DIR}/%.tst ${OUTPUT_DIR}/%.out
	diff -I '#.*' $^ > $@ 2>&1

${TEST_DIR}/%.tst: ${INPUT_DIR}/%.pdb
	[ -f $@ ] || ./tools/dbox $< > $@ 2>&1
# 2>&1
	[ -f $@ ] && touch $@

${OUTPUT_DIR}/%.out: ${INPUT_DIR}/%.pdb
	./pdbboxes $^ > $@ 2>&1
# 2>&1

clean:
	rm -rf ./outputs/*.diff

distclean: clean
	rm -rf ./outputs/*
