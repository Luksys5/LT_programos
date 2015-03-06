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

	diff = ''
	signal = 0
	
	diff += placing(int(ints[0]),int(chk[0]))
	diff += placing(int(ints[1]),int(chk[1]))
	
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
	return diff, signal

def last(op1, op2, opc):
	differ = ''
	if op1 == [''] and opc != ['']:
		differ += op2[0]+'-'+op2[1]+' '+opc[0]+'-'+opc[1]+' '
	elif op1 == ['']:
		differ += op2[0]+'-'+op2[1]+' '
	elif op1 == op2:
		differ += opc[0]+'-'+opc[1]+' '
		return diff
	elif op1 < op2 or op2 < op1:
		if op2[0] > op1[1]:
			differ += op1[0]+'-'+op1[1]+' '+op2[0]+'-'+op2[1]+' '
			return differ
		differ += op2[0]+'-'+op2[1]+' '+op1[0]+'-'+op1[1]+' '
	return differ
def cloop(binds,cbind, chval,name):
	a = b = 0  ## raides nurodancios pozicija intervalam paimti
        differs = '' ## Irasomi besiskiriantys intervalai, sekos
        notf = ''    ## Nerasti intervalai
	s = 0
	print binds
	print cbind
	print ' ------------------+Lyginam+----------------------'
	cbind = cbind.split(' ')
	binds = binds.split(' ')
        x = y = 0       ## tas ats kas a,b tik naudojama funkcijai "lyginu".
        chint = cbind[a].split('-')       ## Tikrinimo intervalas.
        interval = binds[b].split('-')    ## Vienas is grupes atstovo intervalas.
        #return differs ,[]
        while interval != [''] or chint != [''] :
		dvalue = 0
                if interval == [''] or chint == ['']:
			if cbind[a] != binds[b]:
				if chint == ['']:
					differs += interval[0] +'-'+interval[1]+' '
				if interval == ['']:
					differs += chint[0] + '-'+ chint[1]+' '
			return differs, notf

                zinterval = binds[b+1].split('-')
                zchint = cbind[a+1].split('-')
		print 'chint', chint
		print 'intervalas', interval
		print 'z-intervalas', zinterval
                if zinterval == [''] or zchint == ['']:
			print bcolors.FAIL,interval, zinterval, chint ,zchint,bcolors.RESET
                        '''     Tuo atveju jei intervalas tarp bruksnio yra tuscias ['']    '''
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

		elif (int(chint[1]) >= int(interval[0])) and (int(interval[1]) >= int(zchint[0])):
			differs += chint[0]+'-'+interval[0]+' '
			while int(interval[1]) >= int(zchint[0]):
				differs += chint[1]+'-'+zchint[0]+' '
				a += 1
				chint = cbind[a].split('-')
				zchint = cbind[a+1].split('-')
				if zchint == ['']:
					for x in range(b,len(binds)):
						differs += binds[x]+' '
					return differs, notf
			differs += zchint[0]+'-'+zchint[1]+' '
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
					for x in range(b,len(cbind)):
						differs += cbind[x]+' '
					return differs, notf
			differs += placing(int(chint[1]),int(interval[1]))
		#	print bcolors.FAIL+differs+bcolors.RESET
			a += 1
			b += 1

		elif int(interval[0]) > int(chint[1]):
			while int(interval[0]) > int(chint[1]):    # Intervalas didesnis uz tikrinama intervala. INT > CHECK
				zchint = cbind[a+1].split('-')
				differs += cbind[a]+' '
				notf += chint[0]+'-'+chint[1]+' '
				if zchint == ['']:
					for x in range(b,len(binds)):
						differs += binds[x]+' '
					return differs, notf
				a += 1
				chint = cbind[a].split('-')
		
		elif int(chint[0]) > int(zinterval[1]):         # Tikrinimo intervalas didesni uz intervala. CHECK > INT
			while int(chint[0]) > int(interval[1]):
				zinterval = binds[b+1].split('-')
				differs += binds[b]+' '
				if zinterval == ['']:
					for x in range(b,len(cbind)):
						differs +=  cbind[x]+' '
					return differs, notf
				b += 1
				interval = binds[b].split('-')
		elif cbind[a] != binds[b]:
			mystr1, s = lyginu(cbind[a],cbind[a+1],binds[b],binds[b+1])
			differs += mystr1+' '
			a += 1
			b += 1
			if s == 1:
				return differs, notf
		else:
#			print bcolors.FAIL+cbind[a]+bcolors.RESET
			a += 1
			b += 1
                chint = cbind[a].split('-')
                interval = binds[b].split('-')

def Changes(bind,check,dval,name):
	import re
	print '---------------check:'+name.rstrip('\n')+'-------------------'
	
	diff, empty= cloop(check,bind,dval,name)
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
