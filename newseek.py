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

def lyginu(dval,int0,int1,zint0,zint1,chk0,chk1,zchk0,zchk1):
	diff = ''
	x = y = 0
	notfound = ''
	if int(zint0) < int(chk1):
		if abs(int(int0)-int(int1)) >= dval:
			diff += placing(int0,int1)
		notfound += int1+'-'+zint0+' '
		if abs(int(chk1)-int(zint1)) >= dval:
			diff += placing(chk1,zint1)
		y += 2
		x += 1
	elif int(zchk0) < int(int1):
		if abs(int(chk0)-int(int0)) >= dval:
			diff += placing(chk0,int0)
		notfound += chk1+'-'+zchk0+' '
		if abs(int(int1)-int(zchk1)) >= dval:
			diff += placing(int1,zchk1)
		x += 2
		y += 1
	elif int(int1) < int(chk0):
		y += 1
		if abs(int(int1)-int(chk0)) >= dval:
			diff += placing(int1,int0)
		notfound += placing(int1,int0)

	elif int(chk1) < int(int0):
		x += 1
		if abs(int(chk1)-int(int0)) >= dval:	
			diff += placing(chk1,chk0)
		notfound += placing(chk1,chk0)
	else:
		x += 1
		y += 1
		if abs(int(chk0)-int(int0)) >= dval:
			diff += placing(int(chk0),int(int0))
		if abs(int(chk1)-int(int1)) >= dval:
			diff += placing(int(chk1),int(int1))
	return diff, notfound, x,y
	
def cloop(binds,cbind, chval):
#	print '---------------------zeba--------------------'
	a = b = 0  ## raides nurodancios pozicija intervalam paimti
	differs = '' ## Irasomi besiskiriantys intervalai, sekos
	notf = ''    ## Nerasti intervalai
	x = y = 0	## tas ats kas a,b tik naudojama funkcijai "lyginu".
	chint = cbind[a].split('-')       ## Tikrinimo intervalas.
	interval = binds[b].split('-')	  ## Vienas is grupes atstovo intervalas.
	#return differs ,[]
	while interval != [''] or chint != [''] :
		if interval == [''] or chint == ['']:
			if chint == ['']:
				if abs(int(interval[0])-int(interval[1])) >= chval:
					differs += interval[0] +'-'+interval[1]
				notf += interval[0] +'-'+interval[1]	
			if interval == ['']:
				if abs(int(chint[0])-int(chint[1])) >= chval:
					differs += chint[0] + '-'+ chint[1]
				notf += chint[0] + '-'+ chint[1]
			return differs, notf
		
		zinterval = binds[b+1].split('-')
		zchint = cbind[a+1].split('-')
		if zinterval == [''] or zchint == ['']:
			'''	Tuo atveju jei intervalas tarp bruksnio yra tuscias [''] '''
			if zinterval == ['']:
				zinterval = ('1000','1001')
			if zchint == ['']:
				zchint = ('1000','1001')
			mystr1, mystr2 ,x, y = lyginu(chval,interval[0],interval[1],zinterval[0],zinterval[1],chint[0],chint[1],zchint[0],zchint[1])
			differs += mystr1
			notf += mystr2
			mystr = mystr2.split('-')
			a += x
			b += y
			return differs, notf

		if int(interval[0]) > int(chint[1]): 			# Intervalas didesnis uz tikrinama intervala.
			mystr = chint[0]+'-'+ chint[1] + ' '
			a += 1
			notf += mystr
			check = differs[(len(differs)-len(mystr)):]
			if check.rstrip(' ') != mystr.rstrip(' '):
				if abs(int(chint[1])-int(chint[0])) >= chval:
					differs += mystr

		elif int(chint[0]) > int(interval[1]):			# Tikrinimo intervalas didesni uz intervala.
			b+= 1
			notf += interval[0]+'-'+ interval[1] + ' '
			if abs(int(interval[0])-int(interval[1])) >= chval and interval != chint:
				differs += interval[0]+'-'+ interval[1] + ' '
		elif abs(int(interval[0])-int(interval[1]))< abs(int(chint[1]) - int(chint[0])) and abs(int(interval[1]) - int(chint[1])) < 3:
			b += 1
			a += 1
			if abs(int(chint[1])-int(chint[0])) >= chval and interval != chint:
				if int(chint[0]) > int(interval[0]):
					differs += interval[0]+'-'+ chint[0] + ' '
				elif int(chint[0]) < int(interval[0]):
					differs += chint[0]+'-'+interval[0] + ' '
				if int(chint[1]) > int(interval[1]):
					differs += interval[1]+'-'+ chint[1] + ' '
				elif int(chint[1]) < int(interval[1]):
					differs += chint[1]+'-'+interval[1] + ' '				

		elif abs(int(chint[1]) - int(chint[0])) < abs(int(interval[0])-int(interval[1])) and abs(int(chint[1]) - int(interval[1])) < 3:
			a += 1
			b += 1
			if interval != chint:
				if int(chint[0]) > int(interval[0]) and abs(int(chint[0]) - int(interval[0])) >= chval:
					differs += interval[0]+'-'+ chint[0] + ' '
				elif int(chint[0]) < int(interval[0]) and abs(int(chint[0]) - int(interval[0])) >= chval:
					differs += chint[0]+'-'+interval[0] + ' '
				if int(chint[1]) > int(interval[1]) and abs(int(chint[1]) - int(interval[1])) >= chval:
					differs += interval[1]+'-'+ chint[1] + ' '
				elif int(chint[1]) < int(interval[1]) and abs(int(chint[1]) - int(interval[1])) >= chval:
					differs += chint[1]+'-'+interval[1] + ' '

		else:
			mystr1, mystr2 ,x, y = lyginu(chval,interval[0],interval[1],zinterval[0],zinterval[1],chint[0],chint[1],zchint[0],zchint[1])
			differs += mystr1
			differs += mystr2
			notf += mystr2
			a += x
			b += y
		chint = cbind[a].split('-')
		interval = binds[b].split('-')		

def Changes(bindl,dval):
	Diflist = []
	checkseek = bindl[0].split(' ')
	groupseek = bindl[1:]
	NotfLenList = []
	diffempty = []
	notfempty = []
	DiffLenList = []
	count = 0
	diffempty.append(0)
	notfempty.append(0)
	for x in groupseek:
		count += 1
		
		difflen = ''
		notflen = ''
		x = x.split(' ')
		diff, empty= cloop(x,checkseek,dval)
		if diff != '':
			print 'Differences', count
			print diff
		if empty != '':
			print 'Notfounds', count
			print empty
		Diflist.append(empty)
		lengths = diff.split(' ')
		for x in lengths:
			mystr = x.split('-')
			try:
				if (int(mystr[1])- int(mystr[0]) ) >= dval:
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
				if (int(mystr[1])- int(mystr[0]) ) > dval:
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
	''' #Check 
	for x in range(0,len(gamal)):
		print 'printing', count
		print baltlist[x].rstrip('\n')
		print gamal[x]
		print betal[x]
		print alfal[x],'\n'
	'''
	# Write to outdiff file
	for x in range(0,len(gamal)):
		output.write(baltlist[x])	
		output.write(bcolors.FAIL+'kilpos '+bcolors.RESET+gamal[x]+'\n')
		output.write(bcolors.YELLOW+'beta '+betal[x]+bcolors.RESET+'\n')
		output.write(bcolors.GREEN+'alfa '+alfal[x]+bcolors.RESET+'\n')
	
	Names = baltlist[1:]	
	measure = -1
	print bcolors.FAIL+'kilpos '+bcolors.RESET
	Diffgama, NotfgamaLen, notfgempty ,DiffgamaLen, diffgempty = Changes(gamal,measure)
	
	print bcolors.GREEN+'alfa '+bcolors.RESET
	Diffalfa, NotfalfaLen, notfaempty, DiffalfaLen, diffaempty = Changes(alfal,measure)
	
	print bcolors.YELLOW+'beta '+bcolors.RESET
	Diffbeta, NotfbetaLen, notfbempty, DiffbetaLen, diffbempty = Changes(betal,measure)
		
	outch.write("-----------------Main-Diffs----------------------\n")
	outdiff.write(bcolors.FAIL+"-----------------Main-Diffs----------------------\n"+bcolors.RESET)
	for x in range(0,len(Diffgama)):
		z = 0
		w = 0
		if not notfgempty[x] or not notfaempty[x] or not notfbempty[x]:
			outch.write( Names[x])
		if not diffgempty[x] or not diffaempty[x] or not diffbempty[x]:
			outdiff.write(Names[x])
		#output.write( Names[x]+ '\n')
		#+bcolors.FAIL +"Bend Doesn't exits: "+bcolors.RESET,Diffgama[x], '\n'
		if not notfgempty[x]:
			w = 1
			outch.write( bcolors.GREEN+"Bend length differences by "+str(measure)+' +- '+bcolors.RESET +NotfgamaLen[x] +'\n')
		if not diffgempty[x]:
			z = 1
			outdiff.write(bcolors.GREEN+"Bend length differences by "+str(measure)+' +- '+bcolors.RESET +DiffgamaLen[x] +'\n')
		#outch.write( bcolors.GREEN+"Alfa Doesn't exits: "+bcolors.RESET, Diffalfa[x], '\n'
		if not notfaempty[x]:
			w = 1
			outch.write( bcolors.GREEN+"Alfa length differences by "+str(measure)+' +- '+bcolors.RESET+ NotfalfaLen[x] + '\n')
		if not diffaempty[x]:
			z = 1
			outdiff.write(bcolors.GREEN+"Alfa length differences by "+str(measure)+' +- '+bcolors.RESET+ DiffalfaLen[x] + '\n')
		#outch.write( bcolors.YELLOW+"Beta Doesn't exits: "+bcolors.RESET, Diffbeta[x], '\n'
		if not notfbempty[x]:
			w = 1
			outch.write( bcolors.YELLOW+"Beta length differences by "+str(measure)+' +- '+bcolors.RESET+ NotfbetaLen[x]+'\n'+'\n')
		if not diffbempty[x]:
			z = 1
			outdiff.write(bcolors.YELLOW+"Beta length differences by "+str(measure)+' +- '+bcolors.RESET+ DiffalfaLen[x]+'\n')
		
		if z == 1:
			outdiff.write('\n')
		if w == 1:
			outch.write('\n')
		
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
'''
atstout = open('atst.colored','w')
atstdiff = open('atst.diff','w')
atstch = open('atst.ch','w')
atstout.write(bcolors.GREEN + '			Alfa helix H '+ bcolors.YELLOW + ' Beta strand E '+ bcolors.RESET+' Bend -'+'\n')
spalv(fdssp,fdnot,atstout,0,atstdiff,atstch,1)
print bcolors.FAIL+'skirtinga seka'+bcolors.RESET
'''
for x in range(1,16):
	f1 = open('../dssp/'+str(x),'r')
	f2 = open('../notdssp/'+str(x),'r')
	outdssp = open(str(x)+'.colored','w')
	outdiff = open(str(x)+'.diff','w')
	outch = open(str(x)+'.ch','w')
	outdssp.write(bcolors.GREEN + '			Alfa helix '+ bcolors.YELLOW + ' Beta strand '+ bcolors.RESET+'\n')
	if x == 1:
		spalv(f1,f2,outdssp,x,outdiff,outch,0)

