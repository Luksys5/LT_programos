#--*-Makefile -*-------------------------------------------------------------
#$Revision$ 
#$Author$
#$Date$
#$URL$
#--*-------------------------------------------------------------------------

IN=./inputs
TST=./tests
OUT=./outputs

INPUTS=${wildcard ${IN}/*.cif}
TESTS=${INPUTS:${IN}/%.cif=${TST}/%.tst}
OUTPUTS=${INPUTS:${IN}/%.cif=${OUT}/%.out}
DIFFS=${TESTS:${TST}/%.tst=${OUT}/%.diff}

all: ${TESTS} ${OUTPUTS} ${DIFFS}

${TST}/%.tst: ${IN}/%.cif
	[ -f $@ ] || ./tools/testclash 0.01 $< | sort > $@ 2>&1
	[ -f $@ ] && touch $@


${OUT}/%.out: ${IN}/%.cif
	./pdbclashes 0.01 $< | sort > $@ 2>&1


${OUT}/%.diff: ${OUT}/%.out ${TST}/%.tst
	diff $^ > $@	


clean:
	rm -rf ./outputs/*.diff

distclean: clean
	rm -rf ./outputs/*
