def minimum(one,two):
	if two > one:
		return str(one), str(two)
	return str(two), str(one)

def placing(one, two):
	diff = ''
	min1, min2 = minimum(one, two)
	if min1 != min2 :
		diff += str(min1)+'-'+str(min2)+' '
	return diff

def lyginu(check, zcheck,interv,zinterv):
	chk = check.split('-')
	ints = interv.split('-')
	zchk = zcheck.split('-')
	zints = zinterv.split('-')
	x = 0
	y = 0
	diff = ''
	signal = 0
	if int(chk[1]) <  int(ints[0]):
		diff += placing(int(chk[0]),int(chk[1]))
		x =1
	elif int(ints[1]) < int(chk[0]):
		diff += placing(int(ints[0]),int(ints[1]))
		y = 1
	else:
		diff += placing(int(ints[0]),int(chk[0]))
		diff += placing(int(ints[1]),int(chk[1]))
		x = y = 1
	
	if zinterv == ['']:
		try:
			number = int(zchk[0])
			diff += chk[0]+'-'+zchk[0]+' '
		except ValueError:
			diff += ''
		signal = 1
	if zcheck == ['']:
		try:
			number = int(zints[0])
			diff += zints[0]+'-'+zints[0]+' '
		except ValueError:
			diff += ''
		signal = 1
	return diff, signal, x, y

def last(op1, op2, opc):
	differ = ''
	print bcolors.FAIL,op1,op2,opc,bcolors.RESET
	if op1 == [''] and opc != ['']:
		print bcolors.FAIL,op1,op2,opc,bcolors.RESET
		differ += op2[0]+'-'+op2[1]+' '+opc[0]+'-'+opc[1]+' '
	elif op1 == ['']:
		differ += op2[0]+'-'+op2[1]+' '
	elif op1 == op2 and opc != ['']: 
		differ += opc[0]+'-'+opc[1]+' '
		return diff
	elif op1 < op2 or op2 < op1:
		if op2[0] > op1[1]:
			differ += op1[0]+'-'+op[1]+' '+op2[0]+'-'+op2[1]+' '
			return differ
		differ += op2[0]+'-'+op2[1]+' '+op1[0]+'-'+op1[1]+' '
	return differ
def cloop(cbind,binds, chval,name):
	a = b = 0  ## raides nurodancios pozicija intervalam paimti
        differs = '' ## Irasomi besiskiriantys intervalai, sekos
        notf = ''    ## Nerasti intervalai
	s = 0
	print cbind
	print binds
	print ' ------------------+Lyginam+----------------------'
	cbind = cbind.split(' ')
	binds = binds.split(' ')
        x = y = 0       ## tas ats kas a,b tik naudojama funkcijai "lyginu".
        chint = cbind[a].split('-')       ## Tikrinimo intervalas.
        interval = binds[b].split('-')    ## Vienas is grupes atstovo intervalas.
        #return differs ,[]
	s = 0
        while interval != [''] or chint != [''] :
		dvalue = 0
                if interval == [''] or chint == ['']:
			if cbind[a] != binds[b]:
				if chint == ['']:
					differs += interval[0] +'-'+interval[1]
				if interval == ['']:
					differs += chint[0] + '-'+ chint[1]
			return differs, notf
		print interval, chint
		zinterval = binds[b+1].split('-')
		zchint = cbind[a+1].split('-')

		if zinterval == [''] or zchint == ['']:
			#print bcolors.FAIL,interval, zinterval, chint ,zchint,bcolors.RESET
			'''Tuo atveju jei intervalas tarp bruksnio yra tuscias ['']  '''   
			if binds[b] == cbind[a]:
				if zinterval == [''] and zchint != ['']:
					differs += cbind[a+1]+' '
				if zchint == [''] and zinterval != ['']:
					differs += binds[b+1]+' '
					
			else:
				if int(chint[1]) < int(interval[0]):
					differs += cbind[a]+' '
					differs += last(zchint,interval,zinterval)
				elif int(interval[1]) < int(chint[0]):
					differs += binds[b]+' '
					differs += last(zinterval, chint,zchint)
				else:
					if zinterval == [''] and zchint != ['']:
						if int(chint[1]) >= int(interval[0]) and int(interval[1]) >= int(zchint[0]):
							differs += placing(int(chint[0]),int(interval[0]))
							differs += placing(int(chint[1]),int(zchint[0]))
							differs += placing(int(interval[1]), int(zchint[1]))
							print 'shi* happens', interval
							return differs, notf
					elif zchint == [''] and zinterval != ['']:
						if int(interval[1]) >= int(chint[0]) and int(chint[1]) >= int(zinterval[0]):
							differs += placing(int(interval[0]),int(chint[0]))
							differs += placing(int(interval[1]),int(zinterval[0]))
							differs += placing(int(chint[1]), int(zinterval[1]))
							print 'shi* doesnt happen'
							return differs, notf
					differs += placing(int(chint[0]),int(interval[0]))
					differs += placing(int(chint[1]),int(interval[1]))
					try:
						differs += zchint[0]+'-'+zchint[1]+' '
					except IndexError:
						if zinterval == ['']:
							return differs, notf
						differs += zinterval[0]+'-'+zinterval[1]+' '
			return differs, notf 
		if int(interval[0]) > int(zchint[1]):
			while int(interval[0]) > int(zchint[1]):    # Intervalas didesnis uz tikrinama intervala. INT > CHECK
				differs += cbind[a]+' '
				notf += chint[0]+'-'+chint[1]+' '
				if zchint == ['']:
					for x in range(b,len(binds)):
						differs += binds[x]+' '
					return differs, notf
				a += 1
				chint = cbind[a].split('-')
				zchint = cbind[a+1].split('-')	

		elif int(chint[0]) > int(zinterval[1]):		# Tikrinimo intervalas didesni uz intervala. CHECK > INT
			while int(chint[0]) > int(interval[1]):
				differs += binds[b]+' '
				if zinterval == ['']:
					for x in range(a,len(cbind)):
						differs +=  cbind[x]+' '
					return differs, notf
				b+=1
				interval = binds[b].split('-')
                                zinterval = binds[b+1].split('-')

		elif (int(chint[1]) >= int(interval[0])) and (int(interval[1]) >= int(zchint[0])):
			differs += placing(int(chint[0]),int(interval[0]))
			while int(interval[1]) >= int(zchint[0]):
				differs += chint[1]+'-'+zchint[0]+' '
				a += 1
				chint = cbind[a].split('-')
				zchint = cbind[a+1].split('-')
				if zchint == ['']:			##Jei paskutinis tikrinimo intervalas mazesnis uz lyginama
					differs += placing(int(chint[1]),int(interval[1]))
					for x in range(b+1,len(binds)):
						differs += binds[x]+' '
					return differs, notf
			differs += placing(int(chint[1]),int(interval[1]))
			a += 1
			b += 1

		elif (int(interval[1]) >= int(chint[0])) and (int(chint[1]) >= int(zinterval[0])):
			differs += placing(int(interval[0]),int(chint[0]))
			while int(chint[1]) >= int(zinterval[0]):
				differs += interval[1]+'-'+zinterval[0]+' '
				b += 1
				interval = binds[b].split('-')
				zinterval = binds[b+1].split('-')
				if zinterval == ['']:				## Jei paskutinis intervalas uzejo uz ribu.
					differs += placing(int(chint[1]),int(interval[1]))
					for x in range(a+1,len(cbind)):
						differs += cbind[x]+' '
					return differs, notf
			differs += placing(int(chint[1]),int(interval[1]))
			a += 1
			b += 1

		elif cbind[a] != binds[b]:
			print chint,bcolors.FAIL,interval,bcolors.RESET
			mystr1, s, x, y = lyginu(cbind[a],cbind[a+1],binds[b],binds[b+1])
			differs += mystr1
			a += x
			b += y
			if s == 1:
				return differs, notf
		else:
#			print bcolors.FAIL+cbind[a]+bcolors.RESET
			a += 1
			b += 1
                chint = cbind[a].split('-')
                interval = binds[b].split('-')

def Changes(bindl,check,dval,name):
	import re
	print '---------------check:'+name.rstrip('\n')+'-------------------'

	diff, empty= cloop(bindl,check,dval,name)
	return diff, empty

def spalv(myfile,outch,measure):
	line = myfile.readline()
	lines = myfile.readlines()
	Names = line
	alfal = []
	for x in lines:
		alfal.append(x.rstrip('\n'))
	
#	print bcolors.FAIL+'kilpos '+bcolors.RESET
	#NotfgamaLen, notfgempty ,DiffgamaLen,diffgempty = Changes(gamal,measure,count,Names)
	print bcolors.GREEN+'alfa '+bcolors.RESET
	Diff, empty = Changes(alfal[0],alfal[1],measure,Names)
	print Diff
	'''
	#print bcolors.YELLOW+'beta '+bcolors.RESET
	#NotfbetaLen, notfbempty, DiffbetaLen, diffbempty = Changes(betal,measure,count,Names)
	#outdiff.write(bcolors.FAIL+"-----------------Main-"+str(count)+"-Diffs----------------------\n"+bcolors.RESET)
	#if all(v is None for v in NotfgamaLen) and all(v is None for v in NotfalfaLen) and all(v is None for v in NotfbetaLen):
#		outch.write("-----------------Main-Diffs----------------------\n")
#	maximum = max(len(DiffgamaLen),len(DiffalfaLen),len(DiffbetaLen))
	for x in range(0,maximum):
		z = 0
		w = 0
		if re.match('^-\s',NotfgamaLen[x]) or NotfgamaLen[x] != '' or re.match('^-\s',NotfalfaLen[x]) or NotfalfaLen[x] != '' or re.match('^-\s',NotfbetaLen[x]) or NotfbetaLen[x] != '':
			outch.write( Names[x])
		if re.match('^-\s',DiffgamaLen[x]) or DiffgamaLen[x] != '' or re.match('^-\s',DiffalfaLen[x]) or DiffalfaLen[x] != '' or re.match('^-\s',DiffalfaLen[x]) or DiffalfaLen[x] != '':
			outdiff.write(Names[x])
		
		if re.match('^-\s',NotfgamaLen[x]) or NotfgamaLen[x] != '':
			w = 1
			outch.write( bcolors.GREEN+"Bend length differences by "+str(measure)+' +- '+bcolors.RESET +NotfgamaLen[x] +'\n')
		if re.match('^-\s',DiffgamaLen[x]) or DiffgamaLen[x] != '':
			z = 1
			outdiff.write(bcolors.GREEN+"Bend length differences by "+str(measure)+' +- '+bcolors.RESET +DiffgamaLen[x] +'\n')
		#outch.write( bcolors.GREEN+"Alfa Doesn't exits: "+bcolors.RESET, Diffalfa[x], '\n'
		if re.match('^-\s',NotfalfaLen[x]) or NotfalfaLen[x] != '':
			w = 1
			outch.write( bcolors.GREEN+"Alfa length differences by "+str(measure)+' +- '+bcolors.RESET+ NotfalfaLen[x] + '\n')
		if re.match('^-\s',DiffalfaLen[x]) or DiffalfaLen[x] != '':
			z = 1
			outdiff.write(bcolors.GREEN+"Alfa length differences by "+str(measure)+' +- '+bcolors.RESET+ DiffalfaLen[x] + '\n')
		#outch.write( bcolors.YELLOW+"Beta Doesn't exits: "+bcolors.RESET, Diffbeta[x], '\n'
		if re.match('^-\s',NotfbetaLen[x]) or NotfbetaLen[x] != '':
			w = 1
			outch.write( bcolors.YELLOW+"Beta length differences by "+str(measure)+' +- '+bcolors.RESET+ NotfbetaLen[x]+'\n')
		if re.match('^-\s',DiffbetaLen[x]) or DiffbetaLen[x] != '':
			z = 1
			outdiff.write(bcolors.YELLOW+"Beta length differences by "+str(measure)+' +- '+bcolors.RESET+ DiffbetaLen[x]+'\n')
		
		if z == 1:
			outdiff.write('\n')
		if w == 1:
			outch.write('\n')
	'''
	return
import re
class bcolors:
	FAIL = '\033[91m'
	BOLD = '\033[95m'
    	BLUE = '\033[94m'
    	GREEN = '\033[92m'
    	YELLOW = '\033[93m'
    	RESET = '\033[0m'
fdssp = open('../atst/atst.dssp','r')
fdnot = open('../atst/atst.notdssp','r')
m = 0
# int(raw_input('Panasumo ivertis: '))
inname = open('seka','r')
outch = open('check.ch','w')
spalv(inname,outch,m)
