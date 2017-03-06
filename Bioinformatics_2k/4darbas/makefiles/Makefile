#Makefil'as sukuria failą outputs/ direktorijoje pasikartojantys, kuris parodo pasikartojančius failus inputs/ direktorijoje
# USAGE: make 
#	make all
#Sugeneruotus failus ištrinti: make clean distclean
IN_FILES=$(wildcard ./inputs/*)
OUT_FILES=${IN_FILES:./inputs/%=./outputs/%.out}
OUT_SAME=./outputs/pasikartoja
OUT_SUMS=./outputs/sums

.PHONY: all clean distclean

all: ${OUT_SAME}

${OUT_SAME}: ${OUT_SUMS}
	./2pasikartoja $^ > $@

${OUT_SUMS}: ${OUT_FILES}
	./sortlist $^ > $@

./outputs/%.out: ./inputs/%
	sha1sum $< > $@

clean:
	rm -rf ${OUT_SUMS} ${OUT_FILES}

distclean:
	rm -rf ${OUT_SAME} 
