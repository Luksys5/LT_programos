MY_LIST=$(wildcard outputs/list)
IN_FILES=$(wildcard ./inputs/*.inp)
OUT_FILES=${IN_FILES:./inputs/%.inp=./outputs/%.out}
OUT_SUMS=outputs/sums
OUT_SAME=outputs/pasikartoja

.PHONY: clean all

all: ${OUT_SAME}

${OUT_SAME}: ${OUT_SUMS}
	./2pasikartoja $^ > $@

./outputs/%.out: ./inputs/%.inp
	sha1sum $< > $@

${OUT_SUMS}: ${OUT_FILES}
	./sortlist $^ > $@

distclean: clean
	rm -f ${OUT_SAME}

clean:
	rm -f ${OUT_FILES}
	rm -f ${OUT_SUMS}
