import math
def creatingcode(bits):
	n=1
	zod={}
	length=len(bits)
	while((int(math.pow(2,n))+1)<(length+n)):
		n=n+1
	
	print "Cia prasideda kodas: ",  n
	sumbins=[]
	Dbins = []
	Cbins=[]
	mybins=[]
	newstring=''
	Ccode = ''
	last=0
	for b in range(1,length+n+1):
		mystr=bin(b)[2:]
		mystr=("0"*(n-len(mystr)))+mystr
		mybins.append(mystr)
	kartai=0
	pozs = []
	for z in range(0,n):
		pozs.append(int(math.pow(2,z))-1)
	nr = 0
	for x in mybins:
		if nr not in pozs:
			Dbins.append(mybins[nr])
		else:
			Cbins.append(mybins[nr])
	
		nr += 1
	print 'Databins: ', Dbins
	print 'Checkbins:', Cbins
	for i in range(0,n):
		poz=int(math.pow(2,i))
		mystr = mybins[poz-1]
		nr = 0
		myint = 0
		for x in Dbins:
			if x[n-1-i] == '1':
				myint += int(bits[nr])
			nr += 1
		mystr = (str(myint%2))
		Ccode += mystr
		print  i, '\'iasis', mystr
		mynr = 0
	print "Ccode: ", Ccode
	last = 0
	for i in range(0,n):
		poz=int(math.pow(2,i))
		#print 'poz: ', poz
		if len(newstring) == (poz-1) :
			newstring+=Ccode[i]
		else:
			newstring += bits[last:poz-1-i]
			newstring += Ccode[i]
			last = poz-1-i
	newstring += bits[last:]
	return newstring
		
mybits='01000011'
newbits = creatingcode(mybits)
print 'newbits: ', newbits
