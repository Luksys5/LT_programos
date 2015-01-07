#!usr/local/bin/python
from check import *
import operator
import os
def readncalc(dict,length):
	myfile = raw_input("Failo pavadinimas: ")
	with open(myfile,"r") as f:
		while True:
			c = f.read(1)
			if not c:
				sort(dict, length)	
				f.close()
				return dict, myfile
			try:
				dict[c] += 1
			except KeyError:
				dict[c] = 1
			length += len(c)# - tarpas
	f.close()
	return dict, myfile
def sort(dict, length):
	for i in dict:
        	dict[i] = float(dict.get(i))/float(length)
        os.system('rm -f filelength')
        with open('filelength','w') as f:
                f.write(str(length))
	return dict
def bshannon(dict):
	import math
	sum = float(0);
	newprob = float(0)
	for x in dict:
		if dict.get(x)>0:
			kodelen = math.log(1/dict.get(x),2)
			if (kodelen % 1) > 0.0:
		                kodelen = math.trunc(kodelen)+1
		kiek = 0
		if sum != float(0):
			newprob += sum
		sum = dict.get(x)
		if newprob == float(0):
			kodas = "0"*kodelen
		else:
			buves = newprob
			kodas = ""
			for i in range(0,kodelen+1):
				buves = buves * 2
				if buves  >= float(1):
					buves -= 1
					kodas += "1"
				else:
					kodas += "0"
		dict[x]=str(kodas)
	return dict
def sorting(tupl,dict):
	tupl = []
        #check(dict)
        values = []
        for y in sorted(dict.values(), reverse = True):
		if y not in values:
			values.append(y)
	for val in values:
		for x in dict:
			if dict.get(x)==val:
				tupl.append((x,val))

	return tupl
def shannon(dict):
        import math
	prob = float(0)
	code = ''
	tuples = []
	fw = open('probs','w')
	tuples = sorting(tuples, dict)
	for key, val in tuples:
		log = math.log(1/val,2)
		length = int(math.ceil(log))
		if prob == float(0):
			code = '0'*length
		else:
			tmp = prob
			for i in range(0,length):
				tmp = tmp * 2
				if tmp >= 1:
					code +='1'
					tmp -= 1
				else:
					code +='0'
		fw.write(str(val)+' '+str(prob)+' '+code+'\n')
		prob += val
		for x in dict:
			if x == key:
				dict[x] = code	
		code = ''
	fw.write('last: '+str(val)+' '+str(prob)+' '+code+'\n')
	
	return dict
def viskas(dict,length):
	dict, somefile = readncalc(dict,length)
	#checkfile(somefile)
	dict = shannon(dict)
	return dict, somefile
