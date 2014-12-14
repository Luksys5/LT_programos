from check import *
import os
import bitarray
def opencode(dict):	
	f=open("kodai","r")
	lines = f.readlines()
	for x in lines:
		if "++" in x:
			dict["+"] = x[2:] 
		else:
			x = x.split("+")
			dict[x[0]] = x[1].rstrip('\n')
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
	import os
	tmp = ''
	with open('filelength','r') as f:
		tmp += f.readline()
	length = int(tmp)
	bitarr = bitarray.bitarray()
	with open(myfile,'rb') as f:
		bitarr.fromfile(f)
	tmp = ''
	allcode = ''
	keyval(dict,'00')
	os.system('rm -f 2kodas')
	with open('2kodas','w') as fw:
		for x in bitarr.to01():
			allcode += str(x)
			tmp+=str(x)
			if str(tmp) in dict.values():
				for key, value in dict.iteritems():
					if value == tmp:
						#if key != '\n':
						#	key = key.rstrip('\n')
						fw.write(key)
						code += len(key)
				tmp = ''
			if code == length:
				print 'sustojo ties: ', code
				fw.write('\n')
				if key == '\n':
					fw.write('\n')
				#print 'kodas ', code, 'ilgis: ', length 
				fw.close()
				return code
#	print allcode
	fw.close()
	return code
def decode():
	arr = {}
	myfile = 'binfile.bin'
	mycode = 0
	arr = opencode(arr)
	mycode = getcode(myfile,mycode,arr)
#	with open('2kodas','r+') as f:
#		f.seek(-1, os.SEEK_END)
#		f.truncate()	
