#--*-Makefile -*-------------------------------------------------------------
#$Revision: 168 $ 
#$Author: Lukas_Tutkus $
#$Date: 2015-03-29 23:09:25 +0300 (Sk, 29 Kov 2015) $
#$URL: svn://saulius-grazulis.lt/praktikos-darbai-2015/Lukas_Tutkus/trunk/vadd/Makefile $
#--*-------------------------------------------------------------------------
#	
#	Raw direktorijoje-rankiniu būdu įrašyti rezultatai.
#	./addprops-rezultatų primoje eilutėje įrašo svn Id ir išsaugo.
#	Rezultatai lyginami su ./vadd STDOUT.
#
PWD := $(shell pwd)
PATH := ${PWD}/bin:${PATH}
export PATH

INPUT_DIR=./inputs
OUTPUT_DIR=./outputs
RAW_DIR=./raw

INPUTS=${wildcard ${INPUT_DIR}/*.dat}
TESTS=${wildcard ${RAW_DIR}/*.tst}

OUTPUTS=${INPUTS:${INPUT_DIR}/%.dat=${OUTPUT_DIR}/%.dat}
DIFS=${TESTS:${RAW_DIR}/%.tst=${OUTPUT_DIR}/%.diff}

all: ${DIFS}

${OUTPUT_DIR}/%.diff: ${TEST_DIR}/%.tst ${OUTPUT_DIR}/%.dat
	diff $^ > $@

${OUTPUT_DIR}/%.dat: ${INPUT_DIR}/%.dat
	./vadd $^ > $@

clean:
	rm -rf outputs/*

