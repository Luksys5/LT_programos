def maximum(one,two):
	max = two
	if max < one:
		return two, one
	return one, two
def Changes(bindl):
	print bindl[0]
	print bindl[1]
	cbind = bindl[0].split(' ')
	binds = bindl[1].split(' ')	
	a = b = 0
	chint = cbind[a].split('-')
	print 'Tikrinama su ',chint
	interval = binds[b].split('-')
	print 'Intervalas',interval
	while a != len(cbind):
		if chint == [''] or interval == ['']:
			break
		if int(chint[1]) < int(interval[0]):
			a += 1
			print bcolors.FAIL+'truksta kilpos ', chint[0]+'-'+chint[1], bcolors.RESET
			chint = cbind[a].split('-')
			print 'Tikrinama su ',chint
		elif int(interval[1]) < int(chint[0]):
			b += 1
			print bcolors.FAIL+'atsirado kilpa ', interval[0]+'-'+interval[1], bcolors.RESET
			interval = binds[b].split('-')
			print 'Intervalas', interval
		else:
			points = 0
			altint = cbind[a+1].split('-')
			altint2 = binds[b+1].split('-')
			if int(altint[0]) < int(interval[1]):
				intpoints = 0
				altpoints = 0
				for x in range(int(chint[0]),int(chint[1])+1):
					if x >= int(interval[0]) and x <= int(interval[1])+1:
						intpoints += 1
				for x in range(int(altint[0]),int(altint[1])+1):
					if x >= int(interval[0]) and x <= int(interval[1])+1:
						altpoints += 1
				if altpoints > intpoints:
					print intpoints, altpoints
					a += 1
					print bcolors.FAIL+'truksta kilpos ', chint[0]+'-'+chint[1], bcolors.RESET
					chint = cbind[a].split('-')
					print 'Tikrinama su ',chint
			elif int(altint2[0]) < int(chint[1]):
				intpoints = 0
                                altpoints = 0
                                for x in range(int(interval[0]),int(interval[1])+1):
                                        if x >= int(chint[0]) and x <= int(chint[1])+1:
                                                intpoints += 1
                                for x in range(int(altint2[0]),int(altint2[1])+1):
                                        if x >= int(chint[0]) and x <= int(chint[1])+1:
                                                altpoints += 1
                                if altpoints > intpoints:
                                        print intpoints, altpoints
                                        b += 1
                                        print bcolors.FAIL+'atsirado kilpa ', interval[0]+'-'+interval[1], bcolors.RESET
                                        interval = binds[b].split('-')
                                        print 'Tikrinama su ',chint
			else:
				print 'atitiko'
				a += 1
				chint = cbind[a].split('-')
				b += 1
				interval = binds[b].split('-')
				if b > len(cbind):
					break
				print 'Tikrinama su ',chint
				print 'Intervalas ', interval
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
