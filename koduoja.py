#!usr/local/bin/python
from check import *
import os
def readncalc(dict,length):
	myfile = raw_input("Failo pavadinimas: ")
	with open(myfile,"r") as f:
		while True:
			c = f.read(1)
			if not c:
				sort(dict, length)	
				return dict, myfile
			try:
				dict[c] += 1
			except KeyError:
				dict[c] = 1
			length += len(c)# - tarpas
	f.close()
	return dict, myfile
def sort(dict, length):
	import collections
	for i in dict:
        	dict[i] = float(dict.get(i))/float(length)
        os.system('rm -f filelength')
        with open('filelength','w') as f:
                f.write(str(length))
	od = collections.OrderedDict(sorted(dict.items()))
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
			for i in range(0,kodelen):
				buves = buves * 2
				if buves  >= float(1):
					buves -= 1
					kodas += "1"
				else:
					kodas += "0"
		dict[x]=str(kodas)
	return dict
def shannon(dict):
        import math
	z=0
	prob = float(0)
	code = ''
	tmp = 0
	for x in dict:
		length = int(math.log(1/dict.get(x),2))+1
		if prob == float(0):
			code = '0'*length
		else:
			tmp = prob
			for i in range(0,length):
				if z ==0:
					print i
				tmp = tmp * 2
				if tmp >= 1:
					code +='1'
					tmp -= 1
				else:
					code +='0'
		prob += dict.get(x)	
		dict[x] = code	
		code = ''
		z=1		
	return dict
def pailgina(dict,didz):
	for x in dict:
		like = "0"*(10-len(dict.get(x)))
		dict[x]=like+dict.get(x)
	return dict
def viskas(dict,length):
	dict, somefile = readncalc(dict,length)
	check(dict)
	dict = shannon(dict)
	return dict, somefile
