#--*-Makefile -*-------------------------------------------------------------
#$Revision: 70 $
#$Author: lutu0929 $
#$Date: 2014-12-29 11:59:03 +0200 (Pr, 29 Grd 2014) $
#$URL: file:///stud3/2012/lutu0929/project/repoz/branches/skaiciavimo-uzduotis/Makefile $
#--*-------------------------------------------------------------------------
PWD := $(shell pwd)
PATH := ${PWD}/bin:${PATH} ### begaline rekukrsija
export PATH

INPUT_DIR = ./inputs-data
OUTPUT_DIR = ./results

INPUT_PDBX = ${wildcard ${INPUT_DIR}/*.cif}
OUTPUT_FAS = ${INPUT_PDBX:${INPUT_DIR}/%.cif=${OUTPUT_DIR}/%.fa}
COUNTS = ${OUTPUT_FAS:${OUTPUT_DIR}/%.fa=${OUTPUT_DIR}/%.cnt} 
FREQ =${COUNTS:${OUTPUT_DIR}/%.cnt=${OUTPUT_DIR}/%.fq}
OUTPUT = $(cat ${OUTPUT_DIR}/1axc.cnt)
ALL = 0


all: count frq

frq: ${FREQ}

count: ${COUNTS}

${OUTPUT_DIR}/%.fq: ${OUTPUT_DIR}/%.cnt
	./countsfq $^ > $@

${OUTPUT_DIR}/%.cnt: ${OUTPUT_DIR}/%.fa
	grep -v ">" $< | fold -w 1 | wc -l > $@
	
${OUTPUT_DIR}/%.fa: ${INPUT_DIR}/%.cif
	./ciftofasta $^ > $@
		
clean:
	rm -rf ${OUTPUT_FAS}
distclean:
	rm -rf ${COUNTS}
	rm -rf ${FREQ}
