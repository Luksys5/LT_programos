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
def Changes(bindl):
	Diflist = []
	checkseek = bindl[0].split(' ')
#	checkseek = checkseek[:len(checkseek)-1]
	groupseek = bindl[1:]
	for x in groupseek:
		x = x.split(' ')
		diff, empty = cloop(x,checkseek)
		Diflist.append(empty)
	return Diflist
def spalv(dssp,notdssp,output,count,outkons,outch,flag):
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
	Diffgama = Changes(gamal)
	Diffalfa = Changes(alfal)
	Diffbeta = Changes(betal)
	for x in range(0,len(Diffgama)):
		print Names[x]+bcolors.FAIL+"Bend Doesn't exits: "+bcolors.RESET,Diffgama[x], '\n'
		print bcolors.GREEN+"Alfa Doesn't exits: "+bcolors.RESET, Diffalfa[x], '\n'
		print bcolors.YELLOW+"Beta Doesn't exits: "+bcolors.RESET, Diffbeta[x], '\n'
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
atstout.write(bcolors.GREEN + '			Alfa helix H '+ bcolors.YELLOW + ' Beta strand E '+ bcolors.RESET+' Bend -'+'\n')
spalv(fdssp,fdnot,atstout,0,atstkons,atstch,1)
'''for x in range(1,16):
	f1 = open('../dssp/'+str(x),'r')
	f2 = open('../notdssp/'+str(x),'r')
	outdssp = open(str(x)+'.colored','w')
	outkons = open(str(x)+'.kons','w')
	outch = open(str(x)+'.ch','w')
	outdssp.write(bcolors.GREEN + ' Alfa helix '+ bcolors.YELLOW + ' Beta strand '+ bcolors.RESET+'\n')
	spalv(f1,f2,outdssp,x,outkons,outch,0)
'''
