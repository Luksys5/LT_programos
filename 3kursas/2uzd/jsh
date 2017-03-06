#!/bin/sh
# Draws jmol script picture.

# USAGE:
#    $0 command input.pdb output.png

set -ue
echo $#
if [ "$#" != 3 ]
then
	echo commands: hbonds, cartoon, wireframe
	echo $0 command input.pdb output.png
	exit;
fi
COMMAND="$1"
INPUT_FILE="$2"
OUTPUT_FILE="$3"
echo $1
if [ "$COMMAND" = "hbonds" ]
then
jmol --nodisplay --script - <<EOF
	load ${INPUT_FILE}
	select all;
	color structure;
	calculate hbonds;
	hbonds 0.1;
	center selected;
	write png "${OUTPUT_FILE}"
	cartoon only;
	write png "str${OUTPUT_FILE}"
EOF
elif [ "$COMMAND" =  "wireframe" ]
then
jmol --nodisplay --script - <<EOF
	load ${INPUT_FILE}
	select all;
	spacefill 0.1
	wireframe on;
	color cpk;
	write png "${OUTPUT_FILE}"
	spacefill 1.5
	write png "2${OUTPUT_FILE}"
EOF
elif [ "$COMMAND" = "cartoon" ]
then 
jmol --nodisplay --script - <<EOF
        load ${INPUT_FILE}
        select all;
        cartoon only
	color structure
        write png "${OUTPUT_FILE}"
EOF
else
	echo Bad commands!
	echo commands: hbonds, cartoon, wireframe
fi

