import math
def creatingcode(bits):
	n=1
	zod={}
	length=len(bits)
	while((int(math.pow(2,n))-1)<=(length+n)):
		n=n+1
	
	print "Cia prasideda kodas: ",  n
	sumbins=[]
	Dbins = []
	Cbins=[]
	mybins=[]
	newstring=''
	Ccode = ''
	last=0
	max = 0
	for b in range(1,length+n+1):
		mystr = bin(b)[2:]
		mystr = ("0"*(n-len(mystr)))+mystr
		mybins.append(mystr)
		if len(mystr) > max:
			max = len(mystr)
	for b in range(0, len(mybins)):
		if len(mybins[b]) != max:
			mybins[b] = ("0"*(max-len(mybins[b])))+mybins[b] 
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
	Ckpoints = []
	for i in range(0,n):
		poz=int(math.pow(2,i))
		Ckpoints.append(poz)
		#print 'poz: ', poz
		if len(newstring) == (poz-1) :
			newstring+=Ccode[i]
		else:
			newstring += bits[last:poz-1-i]
			newstring += Ccode[i]
			last = poz-1-i
	newstring += bits[last:]
	return newstring, n, Ccode, Ckpoints
def badbit(bits,n):
	for i in range(0,n):
		mod = 0
		add= ''
		last = 0
		first = 0
		on = 0
		poz = int(math.pow(2,i))
		if i == 0:
			for x in bits[0::2]:
				if on:
					mod += int(x)		
				on = 1
			newcode = str(mod % 2)	
		else:
			mod = 0
			mybins = bits[poz-1:]
			while(mybins != ''):
				if first==0:
					add += mybins[1:poz]
					first = 1
				else:
					add += mybins[:poz]
				mybins = mybins[poz*2:]
			for x in add:
				mod += int(x)
			newcode += str(mod % 2)
			first = 0
			add = ''
	return newcode	
def Change(bits):
	print 'bitu seka'
	ch = []
#	ch = int(raw_input("0-Jokiu keitimu.Kuri bita pakeisti nuo 1 iki "+str(len(bits))+": "))
	ch.append(14)
	if ch == 0:
		return
	for x in ch:
		if  bits[int(x)-1] == '0':
			bits = bits[:x-1]+'1'+bits[x:]
		else:
			bits = bits[:x-1]+'0'+bits[x:]
	return bits
def Repaircode(Chk, mybits,n):
	code = ''
	pozs = []
	for i in range(0,n):
		poz = int(math.pow(2,i))
		pozs.append(poz)
		code += mybits[poz-1]
	if code == Chk:
		print "kodai sutampa", code
	else:
		print code, Chk
		blogas = 0
		for i in range(0,n):
			if code[i] != Chk[i]:
				blogas+=pozs[i]
		print 'blogas bitas: ', blogas
	return

#mybits=raw_input("Irasykite bitu seka pvz. 01010: ")
mybits = '010100101000010'
print "Irasyta seka: ",mybits
newbits, n, code, pozs = creatingcode(mybits)
print 'seka su kontroliniais sk.: ', newbits
print 'kontroliniu sk. pozicija',pozs
newbits = Change(newbits)
print 'pakeistas', newbits
checkcode = badbit(newbits,n)
print checkcode
Repaircode(checkcode,newbits,n)

