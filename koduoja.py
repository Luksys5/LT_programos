#!usr/local/bin/python
def readncalc(dict,length):
	myfile = raw_input("Failo pavadinimas: ")
	f=open(myfile,"r")
	lines = f.readlines()
	tarpas = 0
	for x in lines:
		x=x.rstrip('\n')
		for i in range(0,len(x)):
			if i !='\s':
				try:
					dict[x[i]] += 1
				except KeyError:
					dict[x[i]] = 1
			else:
				tarpas += 1
		length += len(x)-tarpas
	for i in dict:	
		dict[i] = float(dict.get(i))/float(length)
	dict = sort(dict)
	f.close()
	return dict, length, myfile
def sort(dict):
	import collections
	od = collections.OrderedDict(sorted(dict.items()))
	return od
def shannon(dict,length):
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
		#print newprob
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
def pailgina(dict,didz):
	for x in dict:
		like = "0"*(10-len(dict.get(x)))
		dict[x]=like+dict.get(x)
	return dict
def viskas(dict,somefile,length,):
	dict, length, somefile = readncalc(dict,length)
	dict = shannon(dict,length)
	return dict, somefile
