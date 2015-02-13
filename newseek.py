def minimum(one,two):
	min = two
	if min > one:
		return str(one), str(two)
	return str(two), str(one)
def placing(one, two):
	diff = ''
	min1, min2 = minimum(one, two)
	if min1 != min2 :
		diff += str(min1)+'-'+str(min2)+' '
	return diff

def lyginu(int0,int1,zint0,zint1,chk0,chk1,zchk0,zchk1):
	diff = ''
	x = y = 0
	notfound = ''
	if int(zint0) < int(chk1):
		diff += placing(int0,int1)
		notfound += int1+'-'+zint0+' '
		diff += placing(chk1,zint1)
		y += 2
		x += 1
	elif int(zchk0) < int(int1):
		diff += placing(chk0,int0)
		notfound += chk1+'-'+zchk0+' '
		diff += placing(int1,zchk1)
		x += 2
		y += 1
	else:
		x += 1
		y += 1
		diff += placing(int(chk0),int(int0))
		diff += placing(int(chk1),int(int1))
	return diff, notfound, x,y
	
def cloop(binds,cbind):
	print '----------------------zeba--------------------'
	differs = ''
	a = b = 0 
	differs = ''
	notf = ''
	x = y = 0
	chint = cbind[a].split('-')
	interval = binds[b].split('-')
	while interval != [''] or chint != [''] :
		zchint = cbind[a+1].split('-')
		zinterval = binds[b+1].split('-')	
		if int(interval[0]) > int(chint[1]):
			a += 1
			notf += chint[0]+'-'+ chint[1] + ' '
			differs += chint[0]+'-'+ chint[1] + ' '
		elif int(chint[0]) > int(interval[1]):
			print differs	
			b+= 1
			notf += interval[0]+'-'+ interval[1] + ' '
			differs += interval[0]+'-'+ interval[1] + ' '
		elif abs(int(interval[0])-int(interval[1]))<2 and abs(int(interval[1]) - int(chint[1])) < 3:
			b += 1
			differs += chint[0]+'-'+ chint[1] + ' '
		elif abs(int(chint[1]) - int(chint[0])) < 2 and abs(int(chint[1]) - int(interval[1])) < 3:
			a += 1
			differs += interval[0]+'-'+ interval[1] + ' '
		else:
			if zinterval == [''] or zchint == ['']:
				if zinterval == ['']:
					zinterval = ('1000','1001')
				if zchint == ['']:
					zchint = ('1000','1001')
				mystr1, mystr2 ,x, y = lyginu(interval[0],interval[1],zinterval[0],zinterval[1],chint[0],chint[1],zchint[0],zchint[1])
				differs += mystr1
				notf += mystr2
				mystr = mystr2.split('-')
				#print differs
				a += x
				b += y
				return differs, notf
			
			mystr1, mystr2 ,x, y = lyginu(interval[0],interval[1],zinterval[0],zinterval[1],chint[0],chint[1],zchint[0],zchint[1])
			differs += mystr1
			notf += mystr2
			a += x
			b += y
		chint = cbind[a].split('-')
		interval = binds[b].split('-')		
def Changes(bindl,m):
	Diflist = []
	checkseek = bindl[0].split(' ')
#	checkseek = checkseek[:len(checkseek)-1]
	groupseek = bindl[1:]
	NotfLenList = []
	diffempty = []
	notfempty = []
	DiffLenList = []
	for x in groupseek:
		difflen = ''
		notflen = ''
		x = x.split(' ')
		diff, empty= cloop(x,checkseek)
		Diflist.append(empty)
		lengths = diff.split(' ')
		for x in lengths:
			mystr = x.split('-')
			try:
				if (int(mystr[1])- int(mystr[0]) ) > m:
					difflen += mystr[0] + '-' + mystr[1]+' '
			except IndexError:
				difflen += ''
		if difflen == '':
			diffempty.append(1)
		else:
			diffempty.append(0)
		DiffLenList.append(difflen)
		lengths = empty.split(' ')
		for x in lengths:
			mystr = x.split('-')
			try:
				if (int(mystr[1])- int(mystr[0]) ) > m:
					notflen += mystr[0] + '-' + mystr[1]+' '
			except IndexError:
				notflen += ''
		if notflen == '':
			notfempty.append(1)
		else:
			notfempty.append(0)
		NotfLenList.append(notflen)
	return Diflist, NotfLenList, notfempty, DiffLenList, diffempty
def spalv(dssp,notdssp,output,count,outdiff,outch,flag):
	print bcolors.FAIL+'-----------limitless--------------'+bcolors.RESET
	import os, subprocess
	lines = dssp.readlines()
	betal = [] # Antrines beta str
	alfal = [] # Antrines alfa str
	gamal = [] # kilpos
	length = 0
	baltlist = []
	glen = 0
	blen = 0
	alen = 0
	pavadinimas = ''
	for y in lines:
               	y = y.rstrip('\n')
               	read = notdssp.readline()
               	if('>' in read):
			baltlist.append(read[1:])
			if length != 0:
				if glen > 0:
					gamastr += str(length-glen)+'-'+str(length-1)+' '
					glen = 0
				if blen > 0:
					betastr += str(length-blen)+'-'+str(length-1)+' '
					blen = 0
				if alen > 0:
					alfastr += str(length-alen)+'-'+str(length-1)+' '
					alen = 0
				alfal.append(alfastr)
				betal.append(betastr)
				gamal.append(gamastr)
			glen = 0
                        blen = 0
                        alen = 0			
			alfastr = ''
			betastr = ''
			gamastr = ''
			length = 0
		else:
			for i in range(0,len(y)):
				length += 1
                	        if( y[i] == '-'):
					if alen > 0:
						alfastr += str(length-alen)+'-'+str(length-1)+' '
						alen = 0
					if blen > 0:
						betastr += str(length-blen)+'-'+str(length-1)+' '
						blen = 0
					glen += 1
                			output.write(bcolors.RESET)
                		elif( y[i]=='E'):
					blen += 1
					if alen > 0:
						alfastr += str(length-alen)+'-'+str(length-1)+' '
						alen = 0
					if glen > 0:
						gamastr += str(length-glen)+'-'+str(length-1)+' '
						glen = 0
                	        	output.write(bcolors.YELLOW)
                	       	else:
					alen += 1
					if blen > 0:
						betastr += str(length-blen)+'-'+str(length-1)+' '
                                                blen = 0
					if glen > 0:
						gamastr += str(length-glen)+'-'+str(length-1)+' '
						glen = 0
					output.write(bcolors.GREEN)
	#if glen > 0:
	#	gamastr += str(length-glen)+'-'+str(length-1)+' '
	#if alen > 0:
		#alfastr += str(length-alen)+'-'+str(length-1)+' '
		#alen = 0
	for x in range(0,len(gamal)):
		output.write(baltlist[x])		
		output.write(bcolors.FAIL+'kilpos '+bcolors.RESET+gamal[x]+'\n')
		output.write(bcolors.YELLOW+'beta '+betal[x]+bcolors.RESET+'\n')
		output.write(bcolors.GREEN+'alfa '+alfal[x]+bcolors.RESET+'\n')
	Names = baltlist[1:]
	measure = -1
	
	Diffgama, NotfgamaLen, notfgempty ,DiffgamaLen, diffgempty = Changes(gamal,measure)
	Diffalfa, NotfalfaLen, notfaempty, DiffalfaLen, diffaempty = Changes(alfal,measure)
	Diffbeta, NotfbetaLen, notfbempty, DiffbetaLen, diffbempty = Changes(betal,measure)
	outch.write("-----------------Main-Diffs----------------------\n")
	for x in range(0,len(Diffgama)):
		if not notfgempty[x] and not notfaempty[x] and not notfbempty[x]:
			outch.write( Names[x])
			outdiff.write(Names[x])
	#	output.write( Names[x]+ '\n')
		#+bcolors.FAIL +"Bend Doesn't exits: "+bcolors.RESET,Diffgama[x], '\n'
		if not notfgempty[x]:
			outch.write( bcolors.GREEN+"Bend length differences by "+str(measure)+' +- '+bcolors.RESET +NotfgamaLen[x] +'\n')
			outdiff.write(bcolors.GREEN+"Bend length differences by "+str(measure)+' +- '+bcolors.RESET +DiffgamaLen[x] +'\n')
		#outch.write( bcolors.GREEN+"Alfa Doesn't exits: "+bcolors.RESET, Diffalfa[x], '\n'
		if not notfaempty[x]:
			outch.write( bcolors.GREEN+"Alfa length differences by "+str(measure)+' +- '+bcolors.RESET+ NotfalfaLen[x] + '\n')
			outdiff.write(bcolors.GREEN+"Alfa length differences by "+str(measure)+' +- '+bcolors.RESET+ DiffalfaLen[x] + '\n')
		#outch.write( bcolors.YELLOW+"Beta Doesn't exits: "+bcolors.RESET, Diffbeta[x], '\n'
		if not notfbempty[x]:
			outch.write( bcolors.YELLOW+"Beta length differences by "+str(measure)+' +- '+bcolors.RESET+ NotfbetaLen[x]+'\n'+'\n')
			outdiff.write(bcolors.YELLOW+"Beta length differences by "+str(measure)+' +- '+bcolors.RESET+ DiffalfaLen[x]+'\n'+'\n')

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
atstdiff = open('atst.diff','w')
atstch = open('atst.ch','w')
atstout.write(bcolors.GREEN + '			Alfa helix H '+ bcolors.YELLOW + ' Beta strand E '+ bcolors.RESET+' Bend -'+'\n')
spalv(fdssp,fdnot,atstout,0,atstdiff,atstch,1)
'''for x in range(1,16):
	f1 = open('../dssp/'+str(x),'r')
	f2 = open('../notdssp/'+str(x),'r')
	outdssp = open(str(x)+'.colored','w')
	outdiff = open(str(x)+'.kons','w')
	outch = open(str(x)+'.ch','w')
	outdssp.write(bcolors.GREEN + ' Alfa helix '+ bcolors.YELLOW + ' Beta strand '+ bcolors.RESET+'\n')
	spalv(f1,f2,outdssp,x,outdiff,outch,0)
'''
