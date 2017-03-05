#!/bin/sh
INPUT="$1"
OUTPUT="$2"
jmol --script $INPUT
echo "$INPUT"
