TEST_DIR = ./tests
INP_DIR = ./inputs
OUT_DIR = ./outputs

IN_FILES=$(wildcard ./inputs/*.in)
OUT_FILES=${IN_FILES:./inputs/%.in=./outputs/%.out}
TEST_DIFF=${OUT_FILES:./outputs/%.out=./outputs/%.diff}
TEST_FILES=${OUT_FILES:./outputs/%.out=/stud3/2012/lutu0929/5darb/tests/%}

all: test 

test: ${TEST_DIFF}

./outputs/%.diff: ./outputs/%.out
	./tstdiff $^ > $@	

./outputs/%.out: ./inputs/%.in
	./ciftofasta $^ > $@

link: ${TEST_FILES}


/stud3/2012/lutu0929/5darb/tests/%: /stud3/2012/lutu0929/5darb/outputs/%.out
	ln -s $^ $@

clean:
	rm -f outputs/*.out

distclean:
	rm -f outputs/*.diff
