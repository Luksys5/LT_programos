from check import *
import bitarray
def opencode(dict):	
	f=open("kodai","r")
	lines = f.readlines()
	for x in lines:
		if "++" in x:
			dict["+"] = x[2:] 
		else:
			x = x.split("+")
			dict[x[0]] = x[1]
	return dict
def kodas(blist,dict,mystr):
	tmp = ""
	for x in blist:
        	if x == True:
                	tmp+='1'
                else:
			tmp+='0'
		for x in dict:
			if tmp == dict.get(x):
				mystr += x
				tmp = ""
		return mystr
def getcode(myfile,code,dict):
	bitarr = bitarray.bitarray()
	with open(myfile,'rb') as f:
		bitarr.fromfile(f)
	tmp = ""
	for x in bitarr.tobytes():
		print x
		tmp+=x
		if tmp in dict:
			for key, value in dict.iteritems():
				if value == tmp:
					code+=key
	#kazkas vyksta cia blogo print pasiziureti				
			tmp = ''
	return code
def decode():
	arr = {}
	myfile = 'binfile.bin'
	mycode = ''
	arr = opencode(arr)
	check(arr)
	mycode = getcode(myfile,arr,mycode)
	#print mycode
	#check(ar)
