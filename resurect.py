import os, subprocess
'''
failas veikia tik ten kur visi .pdb ir ./dali_sp.pl 
siuo atveju visos grupes yra direktorijoje duomenys/
Komentarai
	readall() - perskaito kiekviena baltyma is failu 0-15 ir suraso i viena faila 
	check() - patikrina ar nera daugiau pasikartojanciu ir visus tinkamus meta i viena faila
	clusetering() - skaito visas grupes is 0-15 failu ir meta 2struktura meta i atskirus failus 
'''
def clustering(out,path,skriptai):
	fh = open(path+'duomenys/atstovai','r')
	for x in range(1,16):
		atstovai = fh.readline()
		atstovai = atstovai.rstrip('\n')
		os.system(path+"dali_sp.pl -i "+atstovai+' -l '+skriptai+str(x)+'alt -m '+out+str(x)+"atstovas")
	return
def all(out,path,skriptai):
	fr = open(skriptai+"/atstovai","r")	
	one = fr.readline()
	one = one.rstrip("\n")
	next = fr.readlines()
	fw = open("all","w")
	for x in next:
		x = x.rstrip("\n")
		fw.write(x+'\n')
	os.system(path+"dali_sp.pl -i "+one+' -l all -m '+out)
	return
def readall():
	fw = open('allpdb','w')
	for y in range(1,16):
		f = open(str(y),'r')
		line = f.readline()
		lines = f.readlines()
		splited = line.split(":")
		mystr = splited[1].split(" ")
		fw.write(mystr[0]+'\n')
		for x in lines:
			x = x.split(" ")
			fw.write(x[0]+'\n')
		f.close()
	fw.close()
	return
def check():
	f = open('allpdb','r')
	lines = f.readlines()
	xi = 0
	yi = 0
	z = 0	
	visada = 0
	fc = open('checkedpdb','w')
	for x in lines:
		for y in lines:
			if yi>xi:
				visada +=1
				if str(x) != str(y):
					z += 1
			yi += 1
		xi+=1
		print z,visada
		if z==visada:
			print z,visada
			fc.write(str(x))
		visada = 0
		z = 0
		yi = 0
	return
def dsspnot(out):
	for x in range(1,16):
		f = open(out+str(x)+'atstovas')	
	return
output = raw_input("output filedir & name, like /home/user/file")
path1 = "./"
skripts = raw_input(" duomenys /home/lukas/pdb/visi/duomenys/ ")
number = raw_input("choose number from 1 to 5 \n 1: checkpdb list \n 2: read all groups \n 3: impose dali with list  \n 4: dali with list with loop and list \n 5: make dssp and notdssp files ")
if int(str(number.rstrip())) == 5:
	dsspnot(output)		

if int(str(number.rstrip())) == 3:
#	clustering(output,path1,skripts)
	all(output,path1,skripts)
