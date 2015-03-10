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

all: ${TESTS} ${DIFS}

${OUTPUT_DIR}/%.diff: ${TEST_DIR}/%.tst ${OUTPUT_DIR}/%.out
	diff $^ > $@

${TEST_DIR}/%.tst: ${INPUT_DIR}/%.pdb
	./dbox $^ > $@
	
${OUTPUT_DIR}/%.out: ${INPUT_DIR}/%.pdb
	./pdbboxes $^ > $@
clean:
	rm -rf ./tests/*
distclean:
	rm -rf ./outputs/*
