#!/usr/bin/bash
#--*Makefile--*
CC=g++
CF= -lm
CO=./bins_out/machine
BIN=./bin/trap_simp.cc
TST=./test_bins/test
OUT=./out/diff.out

all: ./bins_out/bin_out ./tests_out/test_out ${OUT}
./bins_out/bin_out:
	$(CC) $(CF) -o ${CO} ${BIN}
	${CO} > $@

./tests_out/test_out:
	${TST} > $@

${OUT}: ./bins_out/bin_out ./tests_out/test_out
	diff $^ > $@ 

clean:
	rm -rf ./bins_out/bin_out ./tests_out/test_out
