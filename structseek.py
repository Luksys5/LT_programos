def spalv(dssp,notdssp,output,count,outkons,outch,flag):
	import os, subprocess
	print bcolors.FAIL+'-----------limitless--------------'+bcolors.RESET
	lines = dssp.readlines()
	betastr = ''
	alfastr = ''
	pavadinimas=''
	proc = 0
	atdssp = ''
	length = 0
	otdssp = ''
	otlst = []
	balt = []
	i = 1
	for y in lines:
		y = y.rstrip('\n')
		read = notdssp.readline()
		if('>' in read):
			balt.append(read[1:].rstrip('\n'))
			proc += 1
			start = 0 
			end = 0
			if otdssp != '':
				otlst.append(otdssp)
		else:
			if start == 0:
				i += 1
			try:
				if y[i] != y[i+1]:
					kilp += 
					start = 0
						
			except IndexError:
				end = i
			if proc < 2:
				atdssp += y	
			else: 
				otdssp += y
	#for y in in range(0,len(otlst)+1):
#		outkons.write(balt[y])
#		for i in 
		
	for y in otlst:
		j = 0
		for i in range(0,len(atdssp)):
			if atdssp[i] != y[i]:
				j += 1
			elif j != 0:
				print  'truksta', atdssp[i-j], 'nuo', i-j+1, 'iki', i
				j = 0
		print atdssp
		print otlst[0]
		return
class bcolors:
	FAIL = '\033[91m'
	BOLD = '\033[95m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RESET = '\033[0m'
fdssp = open('../atst/atst.dssp','r')
fdnot = open('../atst/atst.notdssp','r')
atstout = open('atst.colored','w')
atstkons = open('atst.kons','w')
atstch = open('atst.ch','w')
atstout.write(bcolors.GREEN + ' Alfa helix H '+ bcolors.YELLOW + ' Beta strand E '+ bcolors.RESET+'\n')
spalv(fdssp,fdnot,atstout,0,atstkons,atstch,1)
'''
for x in range(1,16):
	f1 = open('../dssp/'+str(x),'r')
	f2 = open('../notdssp/'+str(x),'r')
	outdssp = open(str(x)+'.colored','w')
	outkons = open(str(x)+'.kons','w')
	outch = open(str(x)+'.ch','w')
	outdssp.write(bcolors.GREEN + ' Alfa helix '+ bcolors.YELLOW + ' Beta strand '+ bcolors.RESET+'\n')
	spalv(f1,f2,outdssp,x,outkons,outch,0)
'''
