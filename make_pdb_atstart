#!/usr/bin/python
# ARGV for files to change
import sys, re
print 'Programa pakeitusi pdb faila isaugo i faila: failo numeris+failo vardas jei input: 1czd_C.pdb output: 11czd_C.pdb'
for i in range(1, len(sys.argv)):
	f = open( sys.argv[i], 'r')
	flines = f.readlines()
	fo = open( '1'+sys.argv[i], 'w' )
	count = 0
	myint = 0
	oldint = 0
	for x in flines:
		if not re.match('^\s*$', x[22:27]):
			if count == 0:
				myint = int(x[22:27])
				oldint = int(x[22:27])
				count = 1
			else:
				myint = int(x[22:27])
				if myint != oldint:
					count = myint - oldint
			fo.write(x[:22]+str(count)+(' '*(5-len(str(count))))+x[27:])
		else:
			fo.write(x)	
