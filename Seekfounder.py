def maximum(one,two):
	max = two
	if max < one:
		return two, one
	return one, two

def cloop(binds,cbind):
	differs = ''
	a = b = 0
	chint = cbind[a].split('-')
	interval = binds[b].split('-')
	while a != len(cbind) or b != len(binds):
		if interval == ['']:
			differs += chint[0]+'-'+chint[1]+' '
			return differs
		if chint == ['']:

			differs += interval[0]+'-'+interval[1]+' '
			return differs
		if int(chint[1]) < int(interval[0]):
			a += 1
			differs += chint[0]+'-'+chint[1]+' '
			chint = cbind[a].split('-')
		elif int(interval[1]) < int(chint[0]):
			print interval[0]
			print interval[1]
			print differs
			'''     Masyne klaida cia       '''
			b += 1
			mystr = interval[0]+'-'+interval[1]+' '
			differs += mystr
			interval = binds[b].split('-')
		else:
			zchint = cbind[a+1].split('-')
			zinterval = binds[b+1].split('-')
			if zinterval == ['']:
				differs += zchint[0]+'-'+zchint[1]+' '
				return differs
			if zchint == ['']:
				differs += zinterval[0]+'-'+zinterval[1]+' '
				return differs
			if int(zchint[0]) < int(interval[1]):
				intpoints = 0
				altpoints = 0
				for x in range(int(chint[0]),int(chint[1])+1):
					if x >= int(interval[0]) and x <= int(interval[1])+1:
						intpoints += 1
				for x in range(int(zchint[0]),int(zchint[1])+1):
					if x >= int(interval[0]) and x <= int(interval[1])+1:
						altpoints += 1
				if altpoints > intpoints:
					a += 1
					differs += chint[0]+'-'+chint[1]+' '
					chint = cbind[a].split('-')
			elif int(zinterval[0]) < int(chint[1]):
			#	print chint, interval
				
				'''	Masyne klaida cia 	'''
				intpoints = 0
                                altpoints = 0
                                for x in range(int(interval[0]),int(interval[1])+1):
                                        if x >= int(chint[0]) and x <= int(chint[1])+1:
                                                intpoints += 1
                                for x in range(int(zinterval[0]),int(zinterval[1])+1):
                                        if x >= int(chint[0]) and x <= int(chint[1])+1:
                                                altpoints += 1
                                if altpoints > intpoints:
                                        b += 1
                                        differs = interval[0]+'-'+interval[1], bcolors.RESET+' '
                                        interval = binds[b].split('-')
				elif altpoints == intpoints:
					b += 2
					interval = binds[b].split('-')
			else:
				a += 1
				chint = cbind[a].split('-')
				b += 1
				interval = binds[b].split('-')
	return differs
def Changes(bindl):
	Diflist = []
	checkseek = bindl[0].split(' ')
#	checkseek = checkseek[:len(checkseek)-1]
	groupseek = bindl[1:]
	for x in groupseek:
		x = x.split(' ')
		#x = x[:len(x)-1]
		print x
		print checkseek, '\n'
		mystr = cloop(x,checkseek)
		Diflist.append(mystr)
		print mystr
	return
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
	Changes(gamal)
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
